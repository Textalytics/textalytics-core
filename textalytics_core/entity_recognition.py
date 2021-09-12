from abc import abstractmethod

from textalytics_core.resources import TextInput, EntityRecognizerOutput


class EntityRecognizer:
    @abstractmethod
    def recognize_entities(self, text_input: TextInput) -> EntityRecognizerOutput:
        pass

class DoNothingEntityRecognizer(EntityRecognizer):
    def recognize_entities(self, text_input: TextInput):
        return EntityRecognizerOutput(entities=[])

