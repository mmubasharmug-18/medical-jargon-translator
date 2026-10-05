from src.config import MAX_NOTE_CHARS


def validate_note(note):
    # returns an error message, or None if the note is fine
    if not note.strip():
        return "Please paste a note first."
    if len(note) > MAX_NOTE_CHARS:
        return f"The note is too long. Keep it under {MAX_NOTE_CHARS} characters."
    return None
