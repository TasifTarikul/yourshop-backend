from .base import *

# Take environment variables from .env_local file
environ.Env.read_env(os.path.join(BASE_DIR, 'env/.env_local'))

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'), 
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}