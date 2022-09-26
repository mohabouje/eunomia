from enum import Enum
from stringcase import pascalcase


class Language(Enum):
    Cpp = 0
    Python = 1

    def __str__(self) -> str:
        return pascalcase(self.name)

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def argparse(s: str) -> 'Language':
        try:
            return Language[pascalcase(s)]
        except KeyError:
            raise ValueError(f"Invalid language: {s}")
