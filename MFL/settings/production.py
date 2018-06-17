import os

# SECRET_KEY = os.environ['SECRET_KEY']

#Read secret key from a file with 
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()        

DEBUG = False

ALLOWED_HOSTS = ['41.72.110.82', 'mfl.moh.gov.zm']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': os.path.join(BASE_DIR, 'db.spatiallite'),
        'NAME': 'MFL',
        'USER': 'django',
        'PASSWORD' : 'django_12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
