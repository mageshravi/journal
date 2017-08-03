from .dev import *

DEBUG = False

ALLOWED_HOSTS = ['webinative.com', 'www.webinative.com']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'com_webinative',
#         'USER': 'webinative',
#         'PASSWORD': 'thebeginningofgreatness',
#         'HOST': 'localhost',
#         'PORT': 3306
#     }
# }

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'public')

# E-mail settings

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'support@webinative.com'
EMAIL_HOST_PASSWORD = 'isaid2016!config'
DEFAULT_FROM_EMAIL = 'support@webinative.com'
SERVER_EMAIL = 'support@webinative.com'
