call venv\Scripts\activate.bat
py manage.py migrate

set DJANGO_SUPERUSER_USERNAME=admin
set DJANGO_SUPERUSER_EMAIL=dongblyyy@gmail.com
set DJANGO_SUPERUSER_PASSWORD=password

py manage.py createsuperuser --noinput
