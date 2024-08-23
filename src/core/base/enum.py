from enum import Enum
from typing import Any


class BaseEnum(Enum):
    """
    ex)
        Color.get_by_value('#00FF00')  # Color.GREEN: #00FF00
        Color.values()  # ['#FF0000', '#00FF00', '#0000FF']
        Color.keys()  # ['RED', 'GREEN', 'BLUE']
        Color.items()  # [('RED', '#FF0000'), ('GREEN', '#00FF00'), ('BLUE', '#0000FF')]
        Color.to_dict()  # {'RED': '#FF0000', 'GREEN': '#00FF00', 'BLUE': '#0000FF'}
        Color.has_value('#FF0000')  # True
        Color.has_key('YELLOW')  # False
        Color.RED  # RED: #FF0000
    """

    @classmethod
    def get_by_value(cls, value) -> "BaseEnum":
        for item in cls:
            if item.value == value:
                return item
        raise ValueError(f"{value} is not a valid value for {cls.__name__}")

    @classmethod
    def values(cls) -> list[Any]:
        return [item.value for item in cls]

    @classmethod
    def keys(cls) -> list[str]:
        return [item.name for item in cls]

    @classmethod
    def items(cls) -> list[tuple]:
        return [(item.name, item.value) for item in cls]

    @classmethod
    def to_dict(cls) -> dict[str, Any]:
        return {item.name: item.value for item in cls}

    @classmethod
    def has_value(cls, value: Any) -> bool:
        return value in cls.values()

    @classmethod
    def has_key(cls, key: str) -> bool:
        return key in cls.keys()

    def __str__(self):
        return f"{self.name}: {self.value}"

    def __repr__(self):
        return self.__str__()
