import os

from mybooktype.settings import *

# DATABASE STUFF
DATABASES = {'default': {'ENGINE': os.environ['BOOKTYPE_DATABASE_ENGINE'],
                         'NAME': 'booktype',
                         'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
                         'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
                         'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
                         'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
                        }
            }

DATA_ROOT = os.environ['OPENSHIFT_DATA_DIR']
MEDIA_ROOT = DATA_ROOT

REDIS_UNIX_SOCKET = '/tmp/redis.sock'
