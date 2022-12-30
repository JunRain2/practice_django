from django.apps import AppConfig

# 앱 생성시 자동으로 생성, 특별한일 없으면 바꾸지 않음.
class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'



