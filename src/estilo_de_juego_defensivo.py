from enum import Enum, auto, unique

@unique # para que no haya valores duplicados
class EstiloDeJuegoDefensivo(Enum):
    """
    Clase para representar el estilo de juego defensivo
    """

    REPLIEGUE = auto()
    EQUILIBRADO = auto()
    PRESION_TRAS_PERDER_POSESION = auto()
    PRESION_CONSTANTE = auto()