import dataclasses
from abc import ABC, abstractmethod
from typing import List, Optional
from enum import Enum

from ..words import Utterance, Word


# pylint: disable=invalid-name
class TimestampStyle(Enum):
    none = 1
    start = 2
    range = 3
    minute = 4


class SpeakerStyle(Enum):
    none = 1
    change = 2
    always = 3


class ProbabilityStyle(Enum):
    none = 1
    line = 2
    line_75 = 3
    line_50 = 4
    line_25 = 5
    word = 6
    word_75 = 7
    word_50 = 8
    word_25 = 9


class LanguageStyle(Enum):
    none = 1
    change = 2
    always = 3


@dataclasses.dataclass
class TranscriptWriterConfig:
    timestamp_style: TimestampStyle = TimestampStyle.none
    speaker_style: SpeakerStyle = SpeakerStyle.none
    probability_style: ProbabilityStyle = ProbabilityStyle.none
    language_style: LanguageStyle = LanguageStyle.none
    verbose: bool = False


class TranscriptWriter(ABC):
    def __init__(self, config: TranscriptWriterConfig):
        self.config = config

    @abstractmethod
    def open(self, path_no_ext: str):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def write(
        self,
        utterance: Utterance,
        unacknowledged_utterance: Optional[List[Utterance]] = None,
        unconfirmed_words: Optional[List[Word]] = None,
    ):
        pass
