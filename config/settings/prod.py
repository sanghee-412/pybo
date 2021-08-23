from .base import *

ALLOWED_HOSTS = ['3.38.66.8', 'pybo412.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '=`z<*ffM?~M9q^NH&>2Y2nDqb^241dk%|',
        'HOST': 'ls-4e2a340f0b45f7a149659c882333019cbaf6f259.c73y3p1tyvfn.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}