from unittest import TestCase

from textalytics_core.entity_recognition import DoNothingEntityRecognizer
from textalytics_core.resources import TextInput


class TestDoNothingEntityRecognizer(TestCase):
    def test_recognize_entities(self):
        text_inupt = TextInput(source_text = "")
        entity_recognizer = DoNothingEntityRecognizer()
        entities = entity_recognizer.recognize_entities(text_inupt)
        assert entities
        assert len(entities.entities) == 0
