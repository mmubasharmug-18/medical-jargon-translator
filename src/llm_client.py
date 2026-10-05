import time

from groq import (Groq, AuthenticationError, RateLimitError, APITimeoutError,
                  APIConnectionError, APIStatusError)

from src.config import MODEL, MAX_RETRIES, TIMEOUT_SECONDS, get_api_key
from src.prompts import build_system_prompt, build_user_message


def translate(note, settings, max_retries=MAX_RETRIES):
    client = Groq(api_key=get_api_key(), timeout=TIMEOUT_SECONDS, max_retries=0)
    messages = [
        {"role": "system", "content": build_system_prompt(settings)},
        {"role": "user", "content": build_user_message(note)},
    ]
    for attempt in range(1, max_retries + 1):
        try:
            r = client.chat.completions.create(
                model=MODEL, messages=messages, temperature=0.2,
                max_tokens=2000, reasoning_effort="low",
            )
            text = (r.choices[0].message.content or "").strip()
            if not text:
                raise ValueError("The model sent back an empty answer. Please try again.")
            return text
        except AuthenticationError:
            raise RuntimeError("The API key is not valid. Check GROQ_API_KEY in your .env file.") from None
        except (RateLimitError, APITimeoutError, APIConnectionError) as err:
            if attempt == max_retries:
                raise RuntimeError("The service is busy or unreachable. Try again in a minute.") from None
            wait = 2 ** attempt
            if isinstance(err, RateLimitError):
                wait = float(err.response.headers.get("retry-after", wait))
            time.sleep(wait)
        except APIStatusError as err:
            if err.status_code >= 500 and attempt < max_retries:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"The API returned an error ({err.status_code}).") from None