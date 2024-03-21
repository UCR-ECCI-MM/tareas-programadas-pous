# Tarea Programada 1 - Primer Entregable
Elaborado por:
María Fernanda Andrés Monge - C00442
Fabián Calvo Alcázar - B91399
Andres Quesada González - C16105

##  Funcionalidades

**1.  Juego**: se puede jugar dentro de la aplicación, con esta funcionalidad el usuario puede seleccionar la categoría y la cantidad de preguntas que quiere responder. Después de mostrar la pregunta y su respuesta, se le pregunta a la persona si acertó o no y se almacena la respuesta junto con la pregunta y categoría.
**2.  Navegador de preguntas**: Navegar entre las preguntas de cierta categoría, se despliega un listado de las preguntas junto con su respuesta y cuando se jugó. Se puede filtrar.
**3.  Modo repaso**: en esta funcionalidad el usuario puede volver a jugar las preguntas que no acertó hasta el momento. Las preguntas fallidas se almacenan cuando el usuario utiliza la funcionalidad de “Juego”.
**4.  Historial del programa**: se puede ver el historial de cuántas preguntas se han jugado de cada categoría con gráficos a lo largo del programa, se puede filtrar la información.
**5. Estadísticas personales:** se puede acceder a las estadísticas personales, donde se muestran gráficos con la cantidad de preguntas que se aciertan o fallan, el usuario puede seleccionar la categoría que desea ver.

## Estructuras de Datos
Una vez que se haya analizado el archivo, la información se almacenará utilizando data frames. Los data frames son estructuras de datos bidimensionales que almacenan información en forma de tablas. Para este proyecto, utilizaremos la biblioteca de análisis de datos Pandas, junto con su funcionalidad para crear y manejar dataframes. Se crearán principalmente dos dataframes: uno para almacenar la información de las categorías (tabla 1) y otro para las preguntas (tabla 2). Estos dataframes agruparán la información relevante para facilitar el acceso a las preguntas y sus datos. Además, se crearán dataframes adicionales para mantener un registro de las interacciones del modo juego, como parte del desarrollo de la funcionalidad propuesta 5.
### Tabla 1. Data frame de categorías.
|  | **Categoría**|
|--|--|
|1|Categoría 1 |
|...|...  |
|N| Categoría N |

### Tabla 2. Data frame de preguntas.
|   | Categoría  | Fecha | Pregunta | Valor | Respuesta | Ronda | # Show |
|---|------------|-------|----------|-------|-----------|-------|--------|
| 1 | Pregunta 1 |       |          |       |           |       |        |
| … | …          |       |          |       |           |       |        |
| N | Pregunta 2 |       |          |       |           |       |        |
