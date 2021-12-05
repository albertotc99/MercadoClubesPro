from plataforma import Plataforma
from estilo_de_juego_ofensivo import EstiloDeJuegoOfensivo
from estilo_de_juego_defensivo import EstiloDeJuegoDefensivo
from formacion import Formacion

class Equipo:
    """
    Clase para representar un equipo.

    Attributes
    ----------
    nombre : str
        nombre del equipo
    plataforma : Plataforma
        enumerado de la plataforma
    estilo_juego_ofensivo : EstiloDeJuegoOfensivo
        enumerado del estilo de juego ofensivo
    estilo_juego_defensivo : EstiloDeJuegoDefensivo
        enumerado del estilo de juego defensivo
    formacion : Formacion
        enumerado de la formacion

    Methods
    -------
    nombre():
        Devuelve el valor de nombre.
    plataforma():
        Devuelve el valor de plataforma.
    estilo_juego_ofensivo():
        Devuelve el valor del estilo de juego ofensivo.
    estilo_juego_defensivo():
        Devuelve el valor del estilo de juego defensivo.
    formacion():
        Devuelve el valor de la formacion.

    """
    
    def __init__(self, nombre, plataforma, estilo_juego_ofensivo, estilo_juego_defensivo, formacion):
        """
        Construye los atributos necesarios para el objeto de equipo.

        Parameters
        ----------
            nombre : str
                nombre del equipo
            plataforma : Plataforma
                enumerado de la plataforma
            estilo_juego_ofensivo : EstiloDeJuegoOfensivo
                enumerado del estilo de juego ofensivo
            estilo_juego_defensivo : EstiloDeJuegoDefensivo
                enumerado del estilo de juego defensivo
            formacion : Formacion
                enumerado de la formacion
        """
        # Nombre
        self._nombre = nombre
        
        # Plataforma
        if type(plataforma) is Plataforma:
            self._plataforma = plataforma
        else:
            raise TypeError ("La variable 'plataforma' debe ser del tipo Plataforma")
        
        # Estilo de juego ofensivo
        if type(estilo_juego_ofensivo) is EstiloDeJuegoOfensivo:
            self._estilo_juego_ofensivo = estilo_juego_ofensivo
        else:
            raise TypeError ("La variable 'estilo_juego_ofensivo' debe ser del tipo EstiloDeJuegoOfensivo")

        # Estilo de juego defensivo
        if type(estilo_juego_defensivo) is EstiloDeJuegoDefensivo:
            self._estilo_juego_defensivo = estilo_juego_defensivo
        else:
            raise TypeError ("La variable 'estilo_juego_defensivo' debe ser del tipo EstiloDeJuegoDefensivo")

        # Formacion
        if type(formacion) is Formacion:
            self._formacion = formacion
        else:
            raise TypeError ("La variable 'formacion' debe ser del tipo Formacion")

    @property
    def nombre(self):
        """Devuelve el valor de nombre."""
        return self._nombre
    
    @property
    def plataforma(self):
        """Devuelve el valor de plataforma."""
        return self._plataforma

    @property
    def estilo_juego_ofensivo(self):
        """Devuelve el valor del estilo de juego ofensivo."""
        return self._estilo_juego_ofensivo

    @property
    def estilo_juego_defensivo(self):
        """Devuelve el valor del estilo de juego defensivo."""
        return self._estilo_juego_defensivo

    @property
    def formacion(self):
        """Devuelve el valor de la formacion."""
        return self._formacion
