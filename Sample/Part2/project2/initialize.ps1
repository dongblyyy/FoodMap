# 가상 환경 활성화
& .\venv\Scripts\Activate.ps1

# 데이터베이스 마이그레이션
py manage.py migrate

$env:DJANGO_SUPERUSER_USERNAME="admin"
$env:DJANGO_SUPERUSER_EMAIL="dongblyyy@gmail.com"
$env:DJANGO_SUPERUSER_PASSWORD="password"

py manage.py createsuperuser --noinput
