from pathlib import Path
import dj_database_url 
import environ
from datetime import timedelta

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
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External Packages
    "django_ckeditor_5",
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
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

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
    'VERSION': '2.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    "COMPONENT_SPLIT_REQUEST": True,
    # OTHER SETTINGS
}


JAZZMIN_SETTINGS = {
    "site_title": "DocEra",
    "site_header": "DocEra Admin",
    "site_brand": "DocEra",
    "site_icon": "images/favicon.png",  
    "site_logo": None,  
    "welcome_sign": "Welcome to DocEra Admin",
    "copyright": "DocEra Health Care",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    "topmenu_links": [
        {"name": "DocEra Admin Home", "url": "admin:index", "permissions": ["auth.view_user"]},  # Changed to valid admin home (since no 'home' URL)
        {"model": "auth.User"},
    ],
    #############
    # Side Menu #
    #############
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        # Built-in
        "auth": "fas fa-users-cog",  # Admin/user management
        "auth.User": "fas fa-user",  # Users
        "auth.Group": "fas fa-users",  # Groups
        "admin.LogEntry": "fas fa-file",  # Logs
        
        # Custom Apps and Models (professional icons: medical/health-themed)
        "core": "fas fa-user-cog",  # Core user management
        "core.UserProfile": "fas fa-user-circle",  # User profiles (general profile icon)
        
        "appointment": "fas fa-calendar-check",  # Appointments scheduling
        "appointment.Appointment": "fas fa-calendar-alt",  # Specific appointment entries
        
        "contact_us": "fas fa-envelope",  # Contact/communication
        "contact_us.ContactUs": "fas fa-headset",  # Support/inquiries
        
        "doctor": "fas fa-user-md",  # Doctors/medical professionals
        "doctor.AvailableTime": "fas fa-clock",  # Time availability
        "doctor.Designation": "fas fa-id-badge",  # Professional titles
        "doctor.Doctor": "fas fa-user-md",  # Doctor profiles
        "doctor.Review": "fas fa-star",  # Ratings/reviews
        "doctor.Specialization": "fas fa-stethoscope",  # Medical specialties
        
        "patient": "fas fa-user-injured",  # Patients/healthcare recipients
        "patient.Patient": "fas fa-procedures",  # Patient records (bed/treatment icon)
        
        "service": "fas fa-medkit",  # Medical services/supplies
        "service.Service": "fas fa-hospital",  # Hospital services
        
        "token_blacklist": "fas fa-lock",  # Token security
        "token_blacklist.BlacklistedToken": "fas fa-ban",  # Blocked tokens
        "token_blacklist.OutstandingToken": "fas fa-key",  # Active tokens
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    "custom_css": "css/bootstrap-dark.css",  # Updated path based on your location (root/static/bootstrap-dark.css)
    "custom_js": None,
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.User": "collapsible",
        "auth.Group": "vertical_tabs",
    },
}

# JAZZMIN_UI_TWEAKS remains the same (cyborg theme, etc.)—no changes needed unless you want to tweak colors.

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": "cyborg",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', 'fontSize', '|',
            'bold', 'italic', 'underline', '|',
            'bulletedList', 'numberedList', '|',
            'outdent', 'indent', '|',
            'undo', 'redo', 'fullScreen', '|',
            'link', 'insertImage', '|',
            'codeBlock', 'horizontalLine', '|',
            # 'sourceEditing'
        ],
        'height': 300,
        'width': '100%',
    },
}

