from django.apps import apps
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator
from django.db.models import CharField, Model, ForeignKey, CASCADE, ImageField, PositiveIntegerField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserCustomManager(BaseUserManager):
    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given phone_number, email, and password.
        """
        if not phone_number:
            raise ValueError("The phone number must be set.")
        email = self.normalize_email(email) if email else None
        user = self.model(phone=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)
class User(AbstractUser):
    objects = UserCustomManager()

    # Remove username field and use phone for authentication
    username = None
    email = None
    phone = CharField(max_length=12, unique=True, verbose_name=_("phone number"))
    address = CharField(max_length=255, blank=True, null=True, verbose_name=_("address"))
    telegram_id = CharField(max_length=30, blank=True, null=True, unique=True, validators=[
        RegexValidator(regex=r'^\d+$', message="Telegram ID must contain only numbers.")],
                            verbose_name=_("telegram id"))
    district = ForeignKey('District', on_delete=CASCADE, blank=True, null=True)
    image = ImageField(upload_to='user/%Y/%m/%d/', default='default.jpg', blank=True, verbose_name=_("image"))
    balance = PositiveIntegerField(default=0, verbose_name=_('user balance'))

    # Use phone as the primary identifier
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]  # You can keep email as a required field

    def __str__(self):
        return self.phone

class Region(Model):
    name = CharField(max_length=255, verbose_name=_("region name"))

    def __str__(self):
        return self.name


class District(Model):
    name = CharField(max_length=255, verbose_name=_("district name"))
    region = ForeignKey('user.Region', CASCADE, related_name='districts')

    def __str__(self):
        return self.name



