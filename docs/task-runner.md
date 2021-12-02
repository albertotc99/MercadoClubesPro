
# Dependency manager

Según este [PEP](https://www.python.org/dev/peps/pep-0621/), para los proyectos python se debe utilizar el archivo 'pyproject.toml'. Por tanto, utilizaré [**poetry**](https://python-poetry.org/) como gestor de dependencias. 

Poetry es muy utilizado, tiene buena documentación y actualizaciones frecuentes. Permite definir en el archivo de configuración los metadatos del proyecto, así como las dependencias del proyecto y para desarrollo. Además es muy sencillo añadir las dependencias con las ordenes ` poetry add <dependency> ` y ` poetry add -D <dependency> ` para añadir las dependencias de desarrollo. 

Para instalar las dependencias simplemente hay que ejecutar ` poetry install ` y poetry lee el fichero de configuración, resuelve las dependencias y las instala. También crea un fichero 'poetry.lock' que, cuando está presente, asegura que siempre se utilizan las mismas versiones de las dependencias.

# Task runner

Para superar el objetivo 3 es necesaria la elección de un task runner. Tras buscar los disponibles para Python he encontrado e investigado varias alternativas: *poetry, invoke, pypyr y  doit*. 
 
Los **requisitos** que se han considerado para elegir son:
- Actualizaciones recientes (menos de 3 meses) de la herramienta para que no se quede obsoleta en poco tiempo
- Buena documentación
 
## Alternativas

- [**Invoke**](https://www.pyinvoke.org/):
Es una herramienta de ejecución de tareas bastante potente y sencilla. Se utiliza para organizar ejecutables Python de manera se pueda llamar el código como tareas CLI. Se ha inspirado en otros task-runners como make, rake y fabric para conseguir una herramienta sencilla, limpia y potente, y permite ejecutar múltiples tareas en una sola llamada. Tiene buena documentación y una comunidad activa. Su ultima actualización es de hace 1 mes.

- [Pypyr](https://pypyr.io/): es un task-runner que permite ejecutar scripts mediante un fichero de configuración escrito en yaml. Su objetivo es ayudar a automatizar cualquier cosa, combinando scripts de difererentes lenguajes en un solo proceso de trabajo. Trata de hacer lo que Makefile, pero de manera más sencilla. La documentación no parece muy intuitiva, pero su último commit es muy reciente (20/11/2021). 

- [Doit](https://pydoit.org/): es una herramienta utilizada como task-runner y dependency manager. Permite ejecutar tanto comandos/scripts de shell como funciones python. Utiliza un fichero llamado 'dodo.py' en el que se definen las tareas en funciones que comienzan por 'task_'. Después con ejecutar en la terminal ``` doit  ``` se ejecutan todas las tareas definidas en el fichero. También se puede especificar que tarea concreta ejecutar. Es una herramienta bastante intuitiva, con buena documentación y el último commit del repositorio en Github es de hace 3 días (28/11/2021).

- [**Poetry**](https://python-poetry.org/):
**es un gestor de dependencias y no una herramienta de ejecución de tareas**, sin embargo se puede utilizar para ejecutar algunas tareas. Es una herramienta fácil de usar e intuitiva. Utiliza un archivo de configuración llamado 'pyproject.toml' donde se especifican las dependencias y se puede configurar la ejecución de scripts. Esta opción es la que nos permite utilizarlo como "task-runner", haciendo scripts python para la ejecución de tareas como los test o el check de sintaxis. Su última actualización es de hace unos días y tiene buena documentación.

## Elección

Las alternativas que cumplen los requisitos son Invoke, Doit y Poetry, pero se ha optado por **poetry** porque ya está incluido en el proyecto, además de ser intuitivo y fácil de utilizar. En principio será suficiente con la funcionalidad que ofrece para realizar algunas tareas a pesar de ser realmente un gestor de dependencias.
