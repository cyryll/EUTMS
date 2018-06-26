from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from django.contrib.auth.models import(
    BaseUserManager,AbstractBaseUser
)

STAFFID_REGEX= '^[a-zA-Z0-9.+-]*$'
CONTACT_REGEX= '^\d+$'

class MyUserManager(BaseUserManager):
    def create_user(self,staffId,email,password=None):
        if not email:
            raise ValueError('users must have an email address')
        user = self.model(
            staffId = staffId,
            #contact = contact,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
        #user.password = password //bad-dont do this
    def create_superuser(self,staffId,email,password=None):
        user= self.create_user(
            staffId=staffId,email=email,password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.save(using = self._db)
        return user

class Users(AbstractBaseUser):
    staffId = models.CharField(
        max_length = 300,
        primary_key = True,
        validators = [
            RegexValidator(regex=STAFFID_REGEX,
            message='username must be alphanumeric or contain numbers',
            code ='invalid_username')
        ],
        unique=True
    )
    email = models.EmailField(
        max_length = 255,
        unique = True,
        verbose_name = 'email address'
    )
    contact = models.CharField(
        max_length = 13,
        validators = [
            RegexValidator(regex=CONTACT_REGEX,
            message="invalid mobile number",
            code='invalid_contact')
        ],
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'staffId'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


    def get_short_name(self):
        #user is identified by their email address
        return self.email

    def has_perm(self,perm, odj=None):
        "Does the user have a specific permissions"
        #Simplest possible answer :Yes,always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        #Simplest possible answer :Yes,always
        return True

   

