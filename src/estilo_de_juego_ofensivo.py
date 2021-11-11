from enum import Enum, auto, unique

@unique # para que no haya valores duplicados
class EstiloDeJuegoOfensivo(Enum):
    """
    Clase para representar el estilo de juego ofensivo
    """

    POSESION = auto()
    EQUILIBRADO = auto()
    BALONES_LARGOS = auto()
    CONTRAATAQUE = auto()