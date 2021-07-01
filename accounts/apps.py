from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'
