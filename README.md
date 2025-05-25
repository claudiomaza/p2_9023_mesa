# p2_9023_mesa

Repositorio de ejemplo para una aplicación de gestión de librería desarrollada en Python con Flask y SQLAlchemy. Este proyecto implementa un sistema de gestión de ventas, títulos/editoriales y consultas a través de una API REST conectada a una base de datos MySQL.

## Estructura del proyecto

- `app.py`: Aplicación principal en Flask. Define el modelo de la base de datos y los endpoints para interactuar con ventas, títulos y editoriales. Incluye ejemplos de rutas para:
  - Consultar ventas por ID y por año/fecha.
  - Consultar títulos por tipo.
  - Registrar y consultar editoriales, incluyendo filtrado por país.
- `modelos.txt`: Documento de referencia con la estructura de tablas y campos considerados en el desarrollo (ventas, títulos, editoriales, autores, empleados, locales, trabajos).
- `requeriments.txt`: Lista de dependencias necesarias para ejecutar la aplicación.
- `.gitignore`: Archivo de configuración para ignorar archivos no necesarios en el control de versiones.

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/claudiomaza/p2_9023_mesa.git
   ```
2. Instala los requerimientos en un entorno virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requeriments.txt
   ```

3. Configura tu base de datos MySQL y ajusta la cadena de conexión en `app.py` si es necesario.

## Uso

1. Ejecuta la aplicación:
   ```sh
   python app.py
   ```
2. Accede a los endpoints según la definición en `app.py` (por ejemplo: `/ventas/<stor_id>`, `/editoriales`, etc.).

## Endpoints principales

- `GET /ventas/<int:stor_id>`: Consulta ventas por ID.
- `GET /ventas/años/<string:fecha>`: Consulta ventas por año/fecha.
- `GET /titulos/tipo/<string:tipo>`: Consulta títulos por tipo.
- `POST /editoriales`: Alta de nueva editorial.
- `GET /editoriales/pais/<string:pais>`: Consulta editoriales por país.

## Modelos de datos

Consulta el archivo `modelos.txt` para ver la estructura de tablas y campos utilizada.

## Dependencias principales

- Flask
- Flask-SQLAlchemy
- PyMySQL
- SQLAlchemy

(Ver `requeriments.txt` para la lista completa.)

## Autor

Repositorio creado por [claudiomaza](https://github.com/claudiomaza).

---

> Proyecto de ejemplo educativo para la materia de Bases de Datos y Desarrollo de Aplicaciones.
