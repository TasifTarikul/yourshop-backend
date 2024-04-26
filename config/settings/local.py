from .base import *
import sentry_sdk
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
    'storages',
]

# API

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
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

# sentry_sdk.init(
#     dsn="https://7958a554076320285c7718f71e4fd90c@o4506760653897728.ingest.sentry.io/4506760655536128",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )

STORAGE_DESTINATION = env('STORAGE_DESTINATION')
if STORAGE_DESTINATION == 's3':
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')
    AWS_S3_CUSTOM_DOMAIN='%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME)

    # static files settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'project_root.coreapp.storage_backends.PublicMediaStorage'
else:
    STATIC_URL = "static/"
    STATIC_ROOT = "static/"

    MEDIA_ROOT = "media/"
    MEDIA_URL = "media/"