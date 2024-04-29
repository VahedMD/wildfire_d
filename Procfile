web: gunicorn <project_name>.wsgi --log-file - 
web: python manage.py migrate && gunicorn backend.wsgi