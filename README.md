# MercadoFichajesClubesPro

## Descripción del problema - Objetivo 0
Clubes Pro es un modo de juego de FIFA en el cual se enfrentan 11 
vs 11 jugadores y que tiene una comunidad considerable de usuarios.
Existen muchas competiciones para este modo de juego, entre ellas 
la liga oficial [VFO](http://www.vfospain.com/psn/).

Cuando llega el mercado de fichajes y un equipo necesita reforzarse
los capitanes escriben anuncios en Twitter indicando plataforma
(PS4, PC o XBOX) y división del equipo, posiciones buscadas y otros
requisitos. De igual forma, los jugadores que buscan club ponen
tuits indicando su posición, plataforma en la que juegan,
experiencia... Todos esos tuits mencionan a cuentas de ayuda para
ser retuiteados y tener mayor visibilidad. Un [ejemplo](https://twitter.com/p3dr3tti_87/status/1425809287943761929).

Con este método, cuando un jugador busca equipo o viceversa, se
tienen que leer muchos tuits que no tienen nada que ver con lo
buscado, haciendo de esta una tarea muy engorrosa. Además, muchas
veces se prueban jugadores que no se adaptan al equipo por disponibilidad,
estilo de juego u otros factores. 

Con esta aplicación se pretende facilitar la tarea de encontrar
equipo o jugador, tratando de resolver los problemas anteriores.

## Documentación

* [Tipos de usuario interesados en utilizar la aplicación](./docs/usuarios.md)
* [Historias de usuario](./docs/HUs.md)
* [Justificación de la elección de Poetry como task-runner y dependency manager](./docs/task-runner.md)


## Instalación y uso

> **Requisitos:** Es necesario tener la versión 3.8 o superior de python. No se asegura que el proyecto
> funcione con versiones anteriores.

Para instalar este proyecto se debe comenzar por clonar el repositorio. Después se tiene que instalar *poetry* siguiendo las instrucciones de [instalación de poetry](https://python-poetry.org/docs/).

Después se tiene que abrir una terminal en la carpeta del proyecto y ejecutar ` poetry install ` para instalar las dependencias.

En este punto podemos comprobar la sintaxis de los archivos python con

` poetry run check `

