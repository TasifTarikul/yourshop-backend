from .base import *

# Take environment variables from .env_local file
environ.Env.read_env(os.path.join(BASE_DIR, 'env/.env_local'))

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS + [
    # Third Party Apps
    'channels'       
]

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
if os.environ.get('DOCKER_CONTAINER'):
    DATABASES['default']['HOST']=env('DB_HOST_DOCKER')

ASGI_APPLICATION = "config.asgi.application" #routing.py will handle the ASGI

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
        }
    }
