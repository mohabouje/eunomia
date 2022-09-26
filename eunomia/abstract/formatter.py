from eunomia.abstract.tool import AbstractToolForLanguage
from eunomia.model.tool import ToolType
from eunomia.model.language import Language


class AbstractFormatter(AbstractToolForLanguage):

    def __init__(self, language: Language) -> None:
        super().__init__(ToolType.Formatter, language)
