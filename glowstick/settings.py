import dj_database_url
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from getenv import env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = env("TEMPLATE_DEBUG", True)
TEMPLATE_DEBUG = env("TEMPLATE_DEBUG", not DEBUG)
SECRET_KEY = env("SECRET_KEY", "v37qcb%=)d4tj_b5v-gz-3#=w&h7x1)y*h@2j8l5-bitt$stdq" if DEBUG else None)

# List allowed hosts in the format:
#    domain.com;domain2.com
ALLOWED_HOSTS = [host for host in env('ALLOWED_HOSTS', '').split(";") if env("ALLOWED_HOSTS")]

# Define database settings in DATABASE_URL environemnt variable
DATABASES = {'default': dj_database_url.config(default="sqlite:///{0}".format(os.path.join(BASE_DIR, "db.sqlite")))}
CONN_MAX_AGE = env("CONN_MAX_AGE", 0)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Internal Apps
    'devices',

    # External Apps
    'compressor',
    'django_extensions',
    'rest_framework',
    'sekizai',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATIC_ROOT = env("STATIC_ROOT", os.path.join(BASE_DIR, 'staticfiles'))
STATIC_URL = env("STATIC_URL", "/static/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

if not DEBUG:
    # Cache templates if not in DEBUG mode
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = 'glowstick.urls'
WSGI_APPLICATION = 'glowstick.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = env("TIME_ZONE", "UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True

# django-debug-toolbar
try:
    import debug_toolbar
    from debug_toolbar import settings as dt_settings

    INSTALLED_APPS = INSTALLED_APPS + (
        'cache_panel',
        'debug_toolbar',
    )

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
except:
    pass

# django_compressor
COMPRESS_ENABLED = env("COMPRESS_ENABLED", not DEBUG)
COMPRESS_PRECOMPILERS = (
    ('text/less', 'glowstick.filters.LessFilter'),
)

# structlog
import structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.KeyValueRenderer()
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# django-rest-framework
REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

REST_FRAMEWORK = {
}
