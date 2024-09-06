# Urban Grocers API Testing
## _Automated API Testing for Urban Grocers_

Urban Grocers API Testing es un proyecto para la creación y prueba de kits de productos, utilizando pytest para realizar pruebas automatizadas de los endpoints de la API, asegurando que las funcionalidades de creación de kits y usuarios funcionen correctamente.

- Escribe pruebas automatizadas para la API
- Verifica las respuestas de la API
- ✨Realiza pruebas reiterativas eficientes en segundos

## Características

- Pruebas para la creación de kits con diferentes longitudes de nombre
- Pruebas para la creación de kits con caracteres especiales, espacios y números
- Pruebas para la creación de kits sin el parámetro `name` y con tipos de datos incorrectos
- Verificación de códigos de respuesta y contenido de las respuestas


## Tecnologías

Urban Grocers API Testing utiliza varios proyectos de código abierto para funcionar correctamente:

- [Python] - Lenguaje de programación principal utilizado para escribir las pruebas
- [pytest] - Framework de pruebas utilizado para ejecutar y gestionar las pruebas
- [requests] - Biblioteca utilizada para realizar solicitudes HTTP a la API
- [apiDoc] - Herramienta utilizada para generar la documentación de la API

![Demostración](https://image.jimcdn.com/app/cms/image/transf/none/path/sd910123ed64e5234/image/ief19b0591f7e0897/version/1725607047/image.jpg)

Y, por supuesto, Urban Grocers API Testing es de código abierto con un [repositorio público][dill] en GitHub.

## Instalación

Urban Grocers API Testing requiere Python v3.6+ para ejecutarse.

Instala las dependencias y ejecuta las pruebas.

```sh
#Clona el repositorio con SSH
git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git

#Instala pytest
pip install pytest

#Ejecuta las pruebas
pytest qa-project-Urban-Grocers-app-es
/create_kit_name_kit_test.py
