from django.contrib.auth.models import AbstractUser, BaseUserManager


class ExtUserManager(BaseUserManager):
    use_in_migrations = True


class ExtUser(AbstractUser):
    objects = ExtUserManager()
