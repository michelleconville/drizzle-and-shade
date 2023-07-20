release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drizzle_and_shade.wsgi