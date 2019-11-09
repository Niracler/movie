#python manage.py flush --no-input
python3 manage.py makemigrations
python manage.py migrate
#python manage.py initadmin
python manage.py collectstatic --no-input --clear

exec "$@"