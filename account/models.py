from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import(
    BaseUserManager,AbstractBaseUser
)

STAFFID_REGEX= '^[a-zA-Z0-9.+-]*$'
CONTACT_REGEX= '^\d+$'

class MyUserManager(BaseUserManager):
    def create_user(self,StaffId,Email,password=None):
        if not Email:
            raise ValueError('users must have an email address')
        user = self.model(
            StaffId = StaffId,
            Email = self.normalize_email(Email)
        )
        user.set_password(password)
        user.Role = 4
        user.save(using = self._db)
        return user
        #user.password = password //bad-dont do this
    def create_superuser(self,StaffId,Email,password=None):
        user= self.create_user(
            StaffId,Email,password=password
        )
        user.Role = 1
        user.is_staff=True
        user.save(using = self._db)
        return user

class Users(AbstractBaseUser):
    ADMIN =1,
    TransportManager = 2
    FleetAssistant = 3
    DepartmentHead = 4
    MechanicManager = 5
    ROLE_CHOICES = (
        ('ADMIN','Admin'),
        ('TransportManager','Transport Manager'),
        ('FleetAssistant', 'Fleet Assistant'),
        ('DepartmentHead','Department Head'),
        ('MechanicManager','Mechanic Manager')
    )
    StaffId = models.IntegerField(
        primary_key= True,
        unique=True)
    Email = models.EmailField(
        max_length = 255,
        unique = True,
        verbose_name = 'email address'
    )
    Role = models.PositiveIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'StaffId'
    REQUIRED_FIELDS = ['Email']

    def __str__(self):
        return self.Email


    def get_short_name(self):
        #user is identified by their email address
        return self.StaffId

    def has_perm(self,perm, odj=None):
        "Does the user have a specific permissions"
        #Simplest possible answer :Yes,always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        #Simplest possible answer :Yes,always
        return True

class UserProfile(models.Model):
    StaffId = models.OneToOneField(
        Users,
        on_delete= models.CASCADE,
        primary_key = True,
    )
    Email = models.EmailField(
        max_length = 255,
        unique = True,
        verbose_name = 'email address'
    )
    Contact = models.CharField(
        max_length = 13,
        validators = [
            RegexValidator(regex=CONTACT_REGEX,
            message="invalid mobile number",
            code='invalid_contact')
        ],
    )
    Name = models.CharField(max_length= 200)
    Department = models.CharField(max_length= 100)

#def create_profile(sender, **kwargs):
   # if kwargs['created']:
   #     user_profile = Staff.objects.create(user = kwargs['instance'])
#
#post_save.connect(create_profile, sender=Users)

#@receiver(post_save, sender=Users)
#def create_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Staff.objects.create(user=instance)
  #  instance.profile.save()

    

   

