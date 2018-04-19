"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY", default="q8lVkJGsIiHcTSQKaWIBsMVPOGnCnF6f7NDGup8KdDNmviSaZVhP0Nq3q3MolmFU")
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache", "LOCATION": ""
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa F405
TEMPLATES[0]["OPTIONS"]["loaders"] = [  # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# Taken from https://github.com/firebase/firebase-admin-python/blob/master/tests/data/service_account.json
FIREBASE_AUTH_CREDENTIALS = {
	"type": "service_account",
	"project_id": "mock-project-id",
	"private_key_id": "mock-key-id-1",
    "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAwJENcRev+eXZKvhhWLiV3Lz2MvO+naQRHo59g3vaNQnbgyduN/L4krlr\nJ5c6FiikXdtJNb/QrsAHSyJWCu8j3T9CruiwbidGAk2W0RuViTVspjHUTsIHExx9euWM0Uom\nGvYkoqXahdhPL/zViVSJt+Rt8bHLsMvpb8RquTIb9iKY3SMV2tCofNmyCSgVbghq/y7lKORt\nV/IRguWs6R22fbkb0r2MCYoNAbZ9dqnbRIFNZBC7itYtUoTEresRWcyFMh0zfAIJycWOJlVL\nDLqkY2SmIx8u7fuysCg1wcoSZoStuDq02nZEMw1dx8HGzE0hynpHlloRLByuIuOAfMCCYwID\nAQABAoIBADFtihu7TspAO0wSUTpqttzgC/nsIsNn95T2UjVLtyjiDNxPZLUrwq42tdCFur0x\nVW9Z+CK5x6DzXWvltlw8IeKKeF1ZEOBVaFzy+YFXKTz835SROcO1fgdjyrme7lRSShGlmKW/\nGKY+baUNquoDLw5qreXaE0SgMp0jt5ktyYuVxvhLDeV4omw2u6waoGkifsGm8lYivg5l3VR7\nw2IVOvYZTt4BuSYVwOM+qjwaS1vtL7gv0SUjrj85Ja6zERRdFiITDhZw6nsvacr9/+/aut9E\naL/koSSb62g5fntQMEwoT4hRnjPnAedmorM9Rhddh2TB3ZKTBbMN1tUk3fJxOuECgYEA+z6l\neSaAcZ3qvwpntcXSpwwJ0SSmzLTH2RJNf+Ld3eBHiSvLTG53dWB7lJtF4R1KcIwf+KGcOFJv\nsnepzcZBylRvT8RrAAkV0s9OiVm1lXZyaepbLg4GGFJBPi8A6VIAj7zYknToRApdW0s1x/XX\nChewfJDckqsevTMovdbg8YkCgYEAxDYX+3mfvv/opo6HNNY3SfVunM+4vVJL+n8gWZ2w9kz3\nQ9Ub9YbRmI7iQaiVkO5xNuoG1n9bM+3Mnm84aQ1YeNT01YqeyQsipP5Wi+um0PzYTaBw9RO+\n8Gh6992OwlJiRtFk5WjalNWOxY4MU0ImnJwIfKQlUODvLmcixm68NYsCgYEAuAqI3jkk55Vd\nKvotREsX5wP7gPePM+7NYiZ1HNQL4Ab1f/bTojZdTV8Sx6YCR0fUiqMqnE+OBvfkGGBtw22S\nLesx6sWf99Ov58+x4Q0U5dpxL0Lb7d2Z+2Dtp+Z4jXFjNeeI4ae/qG/LOR/b0pE0J5F415ap\n7Mpq5v89vepUtrkCgYAjMXytu4v+q1Ikhc4UmRPDrUUQ1WVSd+9u19yKlnFGTFnRjej86hiw\nH3jPxBhHra0a53EgiilmsBGSnWpl1WH4EmJz5vBCKUAmjgQiBrueIqv9iHiaTNdjsanUyaWw\njyxXfXl2eI80QPXh02+8g1H/pzESgjK7Rg1AqnkfVH9nrwKBgQDJVxKBPTw9pigYMVt9iHrR\niCl9zQVjRMbWiPOc0J56+/5FZYm/AOGl9rfhQ9vGxXZYZiOP5FsNkwt05Y1UoAAH4B4VQwbL\nqod71qOcI0ywgZiIR87CYw40gzRfjWnN+YEEW1qfyoNLilEwJB8iB/T+ZePHGmJ4MmQ/cTn9\nxpdLXA==\n-----END RSA PRIVATE KEY-----",
	"client_email": "mock-email@mock-project.iam.gserviceaccount.com",
	"client_id": "1234567890",
	"auth_uri": "https://accounts.google.com/o/oauth2/auth",
	"token_uri": "https://accounts.google.com/o/oauth2/token",
	"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mock-project-id.iam.gserviceaccount.com"
}
