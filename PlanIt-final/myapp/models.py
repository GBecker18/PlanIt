from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings  # Add this import 
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)
def generate_account_id():
    return get_random_string(8, allowed_chars='0123456789')

class Employee(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    userID = models.CharField(unique=True, max_length=8, default=generate_account_id, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
   

    def save(self, *args, **kwargs):
        if not self.userID:
            self.userID = generate_account_id()
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.username} ({self.userID})'

"""
class Manager(AbstractBaseUser):
    objects = CustomUserManager()

    userID = models.CharField(unique=True, max_length=8, default=generate_account_id(), blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        # Handle custom permissions logic here
        return True

    def has_module_perms(self, app_label):
        # Handle custom module permissions logic here
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        if not self.userID:
            self.userID = generate_account_id()  
        super(Manager, self).save(*args, **kwargs)

"""


class Shift(models.Model):
    # Assuming you have a ForeignKey to Employee
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='userID')
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()