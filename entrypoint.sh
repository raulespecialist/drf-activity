#!/bin/bash
python core/manage.py migrate
python core/manage.py collectstatic --no-input --clear
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'meloadik@gmail.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('user1', 'user1@example.com', 'TestPass3')" | python core/manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_user('user2', 'user2@example.com', 'TestPass3')" | python core/manage.py shell

export DJANGO_SETTINGS_MODULE=core.settings
exec gunicorn -c config/gunicorn/conf.py --bind :8000 --chdir core core.wsgi:application

exec "$@"