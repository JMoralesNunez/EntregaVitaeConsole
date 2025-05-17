1README.md
1. Nombre del Proyecto
Sistema de Gestión de Hojas de Vida
2. Nombres de los Integrantes y Grupo
Thomas Noriega - Berners Lee

Juan Fernando Puerta - Van Rossum

Miguel Angel Arias - Van Rossum

Jhonatan Morales - Van Rossum

3. Descripción General del Sistema
El Sistema de Gestión de Hojas de Vida es una aplicación en Python que permite gestionar información de hojas de vida de usuarios. El sistema ofrece las siguientes funcionalidades:
Añadir nuevos usuarios: Permite registrar datos personales (nombre, identificación, fecha de nacimiento, celular, dirección, correo), formación académica, experiencia profesional, referencias personales y habilidades adicionales.

Actualizar usuarios existentes: Permite añadir nuevas experiencias o formaciones, editar dirección o número de contacto, y agregar habilidades o referencias.

Filtrar hojas de vida: Filtra usuarios por años de experiencia, título de formación o habilidades específicas, generando archivos JSON con los resultados.

Generar hojas de vida: Crea archivos de texto (hoja_vida_{id}.txt) con la información formateada de cada usuario.

Persistencia de datos: Almacena todos los datos en un archivo JSON (datos.json) para mantener la información entre sesiones.

El sistema utiliza un diccionario (usuarios) para almacenar la información y valida las entradas del usuario con expresiones regulares, verificaciones de formato de fecha y restricciones de longitud.
4. Instrucciones para Ejecutar el Programa
Requisitos previos:
Tener Python 3.6 o superior instalado.

Contar con un editor de texto o IDE (como VS Code, PyCharm, o IDLE).

Asegurarse de que las librerías necesarias estén instaladas (ver sección 5).

Pasos para ejecutar:
Descarga el código:
Clona o descarga el repositorio que contiene el archivo hojas_de_vida.py.

Instala las librerías (si no están incluidas en Python):
bash

pip install -r requirements.txt

O instala manualmente:
bash

pip install re datetime json

Nota: Estas librerías suelen venir incluidas en la instalación estándar de Python.

Ejecuta el programa:
Abre una terminal en el directorio donde está hojas_de_vida.py.

Ejecuta el comando:
bash

python hojas_de_vida.py

Interactúa con el menú:
Selecciona una opción (1-4) para añadir un usuario, actualizar uno existente, filtrar hojas de vida o salir.

Sigue las instrucciones en pantalla para ingresar datos o seleccionar opciones.

Archivos generados:
hoja_vida_{id}.txt: Hojas de vida individuales en formato de texto.

datos.json: Almacena todos los datos de los usuarios.

filtroAños.json, formación.json, habilidades.json: Resultados de los filtros.

5. Librerías Utilizadas y Cómo Instalarlas
El programa utiliza las siguientes librerías estándar de Python, que no requieren instalación adicional si tienes Python instalado:
re: Para validar direcciones y correos electrónicos con expresiones regulares.

datetime: Para validar fechas de nacimiento.

json: Para manejar la persistencia de datos en archivos JSON.

Instalación:
Estas librerías vienen incluidas en la biblioteca estándar de Python. Si por alguna razón no están disponibles, verifica tu instalación de Python o reinstala Python desde python.org.
Si usas un archivo requirements.txt, puedes crearlo con:
plaintext

# requirements.txt
# No se requieren dependencias externas, ya que re, datetime y json son estándar.

6. Ejemplos de Uso o Datos Simulados
Ejemplo 1: Añadir un nuevo usuario
Selecciona la opción 1 en el menú principal.

Ingresa los datos solicitados:

A continuación se le pedirán sus datos personales
Ingresa tu nombre: Ana
Agrega tu número de identidad: 123456789
Ingresa tu fecha de nacimiento (DD/MM/AA): 15/05/1995
Ingresa tu número de celular: 3001234567
Ingresa la dirección de tu vivienda: Calle 10 #20-30
Ingresa tu correo electrónico: ana@example.com

Ingresa formación académica:

Ingresa el nombre de la universidad: Universidad Nacional
Ingresa el nombre del título: Ingenieria
Ingresa el año de graduación: 2020
¿Quieres añadir más formación profesional? 1.Si/2.No: 2

Ingresa experiencia laboral (opcional):

¿Tienes experiencia laboral? 1.Si/2.No: 1
Empresa donde trabajó: Empresa XYZ
¿Qué cargo ejercías?: Analista
¿Tiempo de duración (cantidad en años)?: 2
¿Quieres ingresar más experiencias laborales? 1.Si/2.No: 2

Ingresa referencias personales:

Ingresa el nombre de tu referencia: Carlos
Ingresa tu relación con esta persona: Amigo
Ingresa el teléfono de tu referencia: 3109876543
¿Quieres añadir más referencias? 1.Si/2.No: 2

Ingresa habilidades adicionales (opcional):

¿Tienes habilidades adicionales? 1.Si/2.No: 1
Digite una habilidad: Python
¿Quieres ingresar otra habilidad? 1.Si/2.No: 2

Resultado:
Se genera hoja_vida_2.txt con la hoja de vida formateada.

Se actualiza datos.json con el nuevo usuario.

Ejemplo 2: Actualizar un usuario
Selecciona la opción 2 y proporciona un ID existente:

Ingresa el ID del usuario a actualizar (ej. 1): 1

Elige una opción de actualización, por ejemplo, añadir experiencia:

Opciones de actualización para el usuario 1
1. Añadir nueva experiencia o formación
2. Editar datos personales o de contacto
3. Agregar habilidades y referencias
4. Volver al menú principal
Selecciona una opción (1-4): 1
¿Deseas añadir experiencia (1) o formación (2)? Ingresa 1 o 2: 1
Ingresa el nombre de la empresa: Nueva Empresa
Ingresa el cargo: Desarrollador
Ingresa la duración (cantidad en años): 1

Resultado:
Se actualiza hoja_vida_1.txt con la nueva experiencia.

Se actualiza datos.json.

Ejemplo 3: Filtrar por habilidades
Selecciona la opción 3:

Opciones de filtrado:
1. Por años de experiencia
2. Por formación específica
3. Por habilidad específica
Selecciona una opción (1-3): 3
Ingresa la habilidad (ej. Python): Python

Resultado:
Se genera habilidades.json con los usuarios que tienen la habilidad "Python".

7. Captura del Tablero de Trabajo
Debido a que este es un documento de texto, no puedo incluir una captura de pantalla directamente. Sin embargo, se recomienda incluir una imagen del tablero de trabajo (por ejemplo, un tablero de Trello, Jira, o un diagrama en papel) que muestre la planificación del proyecto, como tareas asignadas, progreso, o división del trabajo entre los integrantes.
Instrucciones para incluir la captura:
Toma una captura de pantalla del tablero de trabajo (por ejemplo, Trello, Notion, o una foto de un tablero físico).

Guarda la imagen como tablero_trabajo.png o tablero_trabajo.jpg en el repositorio.

Añade la siguiente línea al README.md para mostrar la imagen:
markdown

![Tablero de Trabajo](tablero_trabajo.png)

Asegúrate de que la imagen esté en el mismo directorio que el README.md o proporciona la ruta correcta.

Ejemplo de descripción del tablero (si no puedes incluir la imagen):
El tablero de Trello se dividió en columnas: Pendiente, En Progreso, Revisión, y Completado.

Tareas asignadas:
Thomas: Diseñar la estructura del diccionario usuarios.

Juan Fernando: Implementar las funciones de filtrado (filtrarHojasAños, filtrarFormación, filtrarHabilidades).

Miguel Angel: Crear la función generar_hoja_de_vida y validaciones de entrada.

Jhonatan: Implementar el menú de actualización y persistencia en JSON.

Se usaron etiquetas para priorizar tareas (Alta, Media, Baja) y fechas límite para cada sprint.

.