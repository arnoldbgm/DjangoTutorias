### 1. **Crear un Entorno Virtual**

Un entorno virtual te permite aislar las dependencias de tu proyecto. Para crear un entorno virtual:

1. Abre una terminal o línea de comandos.
2. Navega al directorio donde deseas crear tu proyecto.

3. Crea el entorno virtual con el siguiente comando:
   ```bash
   python -m venv nombre_del_entorno
   ```

   Por ejemplo, si quieres que tu entorno virtual se llame `venv`, usa:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:

   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - En **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### 2. **Instalar Django**

Con el entorno virtual activado, instala Django utilizando `pip`:

```bash
pip install django
```

### 3. **Crear un Proyecto Django**

Una vez que Django está instalado, puedes crear un nuevo proyecto:

1. Crea un nuevo proyecto con el siguiente comando:
   ```bash
   django-admin startproject nombre_del_proyecto
   ```

   Por ejemplo, si deseas que tu proyecto se llame `mi_libreria`, ejecuta:
   ```bash
   django-admin startproject core .
   ```


### 4. **Instalar Django REST Framework (DRF)**

Django REST Framework es un potente kit de herramientas para construir APIs web.

1. Instala Django REST Framework con `pip`:
   ```bash
   pip install djangorestframework
   ```

2. Agrega `rest_framework` a la lista de aplicaciones instaladas en el archivo `settings.py` de tu proyecto:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
   ]
   ```

### 5. **Instalar Jazzmin**

Jazzmin es un paquete que mejora la interfaz de administración de Django con un diseño moderno.

1. Instala Jazzmin con `pip`:
   ```bash
   pip install django-jazzmin
   ```

2. Agrega `jazzmin` a la lista de aplicaciones instaladas en el archivo `settings.py` de tu proyecto, justo antes de `django.contrib.admin`:
   ```python
   INSTALLED_APPS = [
       'jazzmin',  # debe ir antes de 'django.contrib.admin'
       'django.contrib.admin',
       ...
   ]
   ```

3. Ejecuta las migraciones para aplicar cualquier cambio de modelo:
   ```bash
   python manage.py migrate
   ```

### 6. **Correr el Servidor de Desarrollo**

Para asegurarte de que todo está configurado correctamente, inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre tu navegador y ve a `http://127.0.0.1:8000/admin/`. Deberías ver la interfaz de administración mejorada por Jazzmin.

### 7. **Crear una Aplicación Django (Opcional)**

Si deseas crear una aplicación dentro de tu proyecto Django:

1. Crea una nueva aplicación con el siguiente comando:
   ```bash
   python manage.py startapp nombre_de_la_aplicacion
   ```

2. Agrega la aplicación a `INSTALLED_APPS` en `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'nombre_de_la_aplicacion',
   ]
   ```

### 8. **Requisitos Adicionales (Opcional)**

Si necesitas instalar paquetes adicionales o crear un archivo `requirements.txt`:

1. Guarda las dependencias actuales en un archivo `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

2. Para instalar las dependencias desde `requirements.txt` en otro entorno:
   ```bash
   pip install -r requirements.txt
   ```

### 9. **Desactivar el Entorno Virtual**

Cuando hayas terminado de trabajar, puedes desactivar el entorno virtual con el comando:

```bash
deactivate
```

### Resumen

Siguiendo estos pasos, habrás configurado un proyecto Django con un entorno virtual, instalado Django, Django REST Framework, y Jazzmin. ¡Ya estarás listo para comenzar a desarrollar tu aplicación web!