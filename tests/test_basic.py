import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.prompts import build_system_prompt
from src.samples import SAMPLES
from src.validation import validate_note

BASE = {"level": "Simple", "language": "English", "words": True, "questions": True}


def test_prompt_has_format_and_rules():
    p = build_system_prompt(BASE)
    for heading in ["In short", "What the note says", "Words explained", "Questions to ask your doctor"]:
        assert heading in p
    assert "Do not diagnose" in p
    assert "exactly as written" in p


def test_reading_level_is_used():
    assert "Very simple" in build_system_prompt({**BASE, "level": "Very simple"})


def test_language_is_used():
    assert "Write the answer in Urdu" in build_system_prompt({**BASE, "language": "Urdu"})


def test_sections_can_be_switched_off():
    p = build_system_prompt({**BASE, "words": False, "questions": False})
    assert "Words explained" not in p
    assert "Questions to ask your doctor" not in p


def test_empty_note_rejected():
    assert validate_note("   ") is not None


def test_long_note_rejected():
    assert validate_note("a" * 5000) is not None


def test_normal_note_accepted():
    for note in SAMPLES.values():
        assert validate_note(note) is None