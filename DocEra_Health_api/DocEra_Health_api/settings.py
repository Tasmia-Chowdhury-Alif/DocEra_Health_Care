
from pathlib import Path
import dj_database_url 
import environ
from datetime import timedelta
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''
env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env("SECRET_KEY") 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=["http://127.0.0.1","http://localhost:3000"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["http://127.0.0.1", "http://localhost:3000"])


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.import_export",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External Packages
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "djoser",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    # Internal Apps
    'core',
    'appointment',
    'contact_us',
    'doctor',
    'patient',
    'service',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'DocEra_Health_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DocEra_Health_api.wsgi.app'


# Database configuration
DATABASE_ENGINE = env.str("DATABASE_ENGINE", default="sqlite").lower()

if DATABASE_ENGINE == "postgresql":
    DATABASES = {
        "default": dj_database_url.parse(
            env("DATABASE_URL", default="postgres://docera:docera@localhost:5432/docera")
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")


# Stripe congiguration
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY") 
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY") 
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET") 


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions. IsAuthenticated', 
    # ]
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=(60*24)),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=4),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}


DJOSER = {
    "LOGIN_FIELD": "username",
    "USER_CREATE_PASSWORD_RETYPE": False,
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "auth/users/activation/{uid}/{token}",
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'user': 'core.serializers.UserSerializer',
        'current_user': 'core.serializers.UserSerializer',
    },
    "EMAIL": {
        "activation": "djoser.email.ActivationEmail",
        "confirmation": "djoser.email.ConfirmationEmail",
        "password_reset": "djoser.email.PasswordResetEmail",
        "password_changed_confirmation": "djoser.email.PasswordChangedConfirmationEmail",
    },
    "TEMPLATES": {
        "activation": "email/activation.html",
        "confirmation": "email/confirmation.html",
        "password_reset": "email/password_reset.html",
        "password_changed_confirmation": "email/password_changed_confirmation.html",
    },
    "SITE_NAME": "DocEra Health Care",
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'DocEra Health API',
    'DESCRIPTION': 'A clean and reliable backend for a Hospital Management System built with Django REST Framework. It handles patient info, doctor schedules, appointments (online & offline), and secure login with JWT and email verification. Online appointments trigger meet link emails automatically.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    "COMPONENT_SPLIT_REQUEST": True,
    # OTHER SETTINGS
}


# Django Unfold Configuration
UNFOLD = {
    "SITE_TITLE": "DocEra Admin",
    "SITE_HEADER": "DocEra Health Care",
    "SITE_LOGO": lambda request: static("images/docera_logo.png"),
    "SITE_FAVICON": lambda request: static("images/docera_favicon.ico"),
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": False,
    "COLORS": {
        "primary": {
            "50": "#e6f0fa",
            "100": "#b3d4f5",
            "200": "#80b8f0",
            "300": "#4d9beb",
            "400": "#1a7fe6",
            "500": "#0066cc",
            "600": "#0052a3",
            "700": "#003d7a",
            "800": "#002952",
            "900": "#001429",
        },
        "secondary": {
            "50": "#e6f5e9",
            "100": "#b3e6bf",
            "200": "#80d895",
            "300": "#4dc96b",
            "400": "#1aba41",
            "500": "#00a127",
            "600": "#008120",
            "700": "#006118",
            "800": "#004110",
            "900": "#002008",
        },
    },
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Doctor Dashboard"),
                "icon": "dashboard",
                "link": "/admin/",
                "items": [],  # Empty items to satisfy Unfold's structure
            },
            {
                "title": _("Appointments"),
                "icon": "event",
                "items": [
                    {
                        "title": _("Appointments"),
                        "link": lambda request: str(reverse_lazy("admin:appointment_appointment_changelist")),
                    },
                ],
            },
            {
                "title": _("Patients"),
                "icon": "person",
                "items": [
                    {
                        "title": _("Patients"),
                        "link": lambda request: str(reverse_lazy("admin:patient_patient_changelist")),
                    },
                ],
            },
            {
                "title": _("Doctors"),
                "icon": "medical_services",
                "items": [
                    {
                        "title": _("Doctors"),
                        "link": lambda request: str(reverse_lazy("admin:doctor_doctor_changelist")),
                    },
                    {
                        "title": _("Designations"),
                        "link": lambda request: str(reverse_lazy("admin:doctor_designation_changelist")),
                    },
                    {
                        "title": _("Specializations"),
                        "link": lambda request: str(reverse_lazy("admin:doctor_specialization_changelist")),
                    },
                    {
                        "title": _("Available Times"),
                        "link": lambda request: str(reverse_lazy("admin:doctor_availabletime_changelist")),
                    },
                    {
                        "title": _("Reviews"),
                        "link": lambda request: str(reverse_lazy("admin:doctor_review_changelist")),
                    },
                ],
                "visible": lambda request: request.user.is_superuser,
            },
            {
                "title": _("Services"),
                "icon": "health_and_safety",
                "items": [
                    {
                        "title": _("Services"),
                        "link": lambda request: str(reverse_lazy("admin:service_service_changelist")),
                    },
                ],
                "visible": lambda request: request.user.is_superuser,
            },
        ],
    },
    "DASHBOARD": {
        "widgets": [
            {
                "type": "stats",
                "title": _("Today's Appointments"),
                "queryset": "appointment.Appointment.objects.filter(time__date=timezone.now().date())",
                "icon": "event",
            },
            {
                "type": "stats",
                "title": _("Pending Payments"),
                "queryset": "appointment.Appointment.objects.filter(payment_status='unpaid')",
                "icon": "payment",
            },
        ],
    },
    "TABS": [
        {
            "models": ["appointment.Appointment"],
            "items": [
                {
                    "title": _("All Appointments"),
                    "link": lambda request: str(reverse_lazy("admin:appointment_appointment_changelist")),
                },
                {
                    "title": _("Online Appointments"),
                    "link": lambda request: str(reverse_lazy("admin:appointment_appointment_changelist")) + "?appointment_type__exact=Online",
                },
                {
                    "title": _("Offline Appointments"),
                    "link": lambda request: str(reverse_lazy("admin:appointment_appointment_changelist")) + "?appointment_type__exact=Offline",
                },
            ],
        },
    ],
    "FILTERS": {
        "AUTOCOMPLETE": ["appointment.Appointment.patient", "appointment.Appointment.doctor"],
    },
    # "EXTENSIONS": {
    #     "modeltranslation": {
    #         "languages": ["en"],
    #     },
    # },
}