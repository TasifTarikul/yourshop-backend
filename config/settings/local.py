from .base import *
from rest_framework.settings import api_settings

# Take environment variables from .env_local file
environ.Env.read_env(os.path.join(BASE_DIR, 'env/.env_local'))

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS + [
    # Third Party Apps
    'channels',     
]

# API

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

REST_KNOX = {
  'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
  'TOKEN_TTL': timedelta(hours=1),
  'USER_SERIALIZER': 'knox.serializers.UserSerializer',
  'TOKEN_LIMIT_PER_USER': None,
  'AUTO_REFRESH': False,
  'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
  'AUTH_HEADER_PREFIX': 'Bearer'
}

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
