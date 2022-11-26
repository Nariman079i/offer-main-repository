from django.db.models import *
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Обязательное поле")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,email,password=None):
        if not email:
            raise ValueError("Обязательное поле")

        user = self.model(
            email = self.normalize_email(email)
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user

class CustomUser(AbstractBaseUser):
    email = CharField(max_length=60,unique=True)

    date_joined = DateField(auto_now_add=True)
    last_login = DateField(auto_now=True)

    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
