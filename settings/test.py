"""
Test-specific Django settings.
"""

# Inherit from base settings
from __future__ import absolute_import
from .base import *     # pylint:disable=W0614,W0401

TEST_APPS = (
    'ubcpi',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_ubcpi',
        'TEST_NAME': 'test_ubcpi',
    },
    'read_replica': {
        'ENGINE': 'django.db.backends.sqlite3',
        'TEST_MIRROR': 'default',
    },
}


# Store uploaded files in a test-specific directory
MEDIA_ROOT = os.path.join(BASE_DIR, 'storage/test')


# Silence cache key warnings
# https://docs.djangoproject.com/en/1.4/topics/cache/#cache-key-warnings
import warnings
from django.core.cache import CacheKeyWarning
warnings.simplefilter("ignore", CacheKeyWarning)
