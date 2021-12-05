from enum import Enum, auto, unique

@unique # para que no haya valores duplicados
class Plataforma(Enum):
    """
    Clase para representar la Plataforma

    """

    PLAYSTATION = auto()
    XBOX = auto()
    PC = auto()
