import os

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['41.72.110.82']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': os.path.join(BASE_DIR, 'db.spatiallite'),
        'NAME': 'mfl',
        'USER': 'django',
        'PASSSWORD': 'django_12345',
    }
}


CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
