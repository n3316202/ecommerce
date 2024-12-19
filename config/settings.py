"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%6#4db0jb4=+i&lph&i&y^zwpiyto!qv_pph8c3ur#f26_!k9-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'home',
    'boards',
    'accounts',
    'store',
    'cart',
    'payment',#dev_41 앱추가
     #dev_46 소셜로그인 추가
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    #provider 추가 (추가로 다른 사이트도 하고 싶을 경우 뒤에 이름만 변경하면 됨)
    #'allauth.socialaccount.providers.google', #구글로그인 구현시 추가
    'allauth.socialaccount.providers.kakao', # 카카오로그인 구현시 추가
    #'allauth.socialaccount.providers.naver', # 네이버 로그인 구현시 추가
    'api',#dev_48
    'rest_framework',#dev_48
    'django_filters',#dev_48
]
#dev_46
#AUTH_USER_MODEL = 'user.User' #추가!! 없으면 오류 발생 "앱이름.모델명" user모델생성 후 allauth말고 내가 생성한 모델을 우선으로 적용
#dev_46
SITE_ID = 1 #추가

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'allauth.account.middleware.AccountMiddleware', # #dev_46 추가
]

ROOT_URLCONF = "config.urls"

#dev_46 
AUTHENTICATION_BACKENDS = [
    #추가 장고에서 사용자의 이름을 기준으로 로그인하도록 설정
    'django.contrib.auth.backends.ModelBackend',
    # 추가 'allauth'의 인증방식 추가
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                 'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko"

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

#Timezone의 사용여부를 정한다.
#False면 모든 datetime들을 표시하고 True면 template과 form에만 적용된다.
#즉 DB에 저장되는 정보도 한국 시간대로 사용하려면 이 부분을 False로 지정해주어야 한다.
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 로그인 성공후 이동하는 URL
LOGIN_REDIRECT_URL = '/'

# 미디어 파일 경로 설정
import os
#http://127.0.0.1:8000/media/파일경로
MEDIA_URL = 'media/'		# ex) /media/photo1.png
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#dev_46 소셜로그인 설정
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True

#dev_46 소셜로그인 설정
SOCIALACCOUNT_PROVIDERS ={
#추가 카카오 설정
"kakao": {
"APP": {
"client_id": "114f15d304d60d315b190c730e98f711",
"secret": "d5eNqRjUNoC90v4JehEVuHDk0eB0Y2oL",
"key": ""
},
# scope의 경우 내가 어떤 데이터를 가져올건지를 선택하는 것인데 사이트마다
# 제공하는 값이 다르기 때문에 가져올 데이터를 설정한 이후 추가/삭제 해보면 됩니다.
# SCOPE값에 제공하지 않는 값을 넣거나 하는 이유로 오류가 나올 수 있음
"SCOPE": [

],
#추가
"AUTH_PARAMS": {
"access_type": "online", #추가
'prompt': 'select_account', #추가 간편로그인을 지원해줌
}}}