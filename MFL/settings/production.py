# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#d2=g30-#)u%kwm3ov59l^*jckl#bo)uqy#3mk@6a6xrxl&b60'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['41.72.110.82']

CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'