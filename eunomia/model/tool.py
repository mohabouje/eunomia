from enum import Enum
from stringcase import pascalcase


class ToolType(Enum):
    Linter = 0
    Formatter = 1
    Compiler = 2
    Interpreter = 3
    Debugger = 4
    Profiler = 5
    TestRunner = 6
    Coverage = 7
    Documentation = 8
    BuildSystem = 9
    PackageManager = 10
    VersionControl = 11

    def __str__(self) -> str:
        return pascalcase(self.name)

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def argparse(s: str) -> 'ToolType':
        try:
            return ToolType[pascalcase(s)]
        except KeyError:
            raise ValueError(f"Invalid tool: {s}")
