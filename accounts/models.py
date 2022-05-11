from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser
from datetime import datetime

#Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):       
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password
            )
        
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save( using =self._db)
        return user


def  get_profile_image_path(self,filename=None):
    return f"profile_image/{self.id}_{self.username}/{filename}"

def  get_default_profile_image():
    return f'profile_image/profile.png'


class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email' , unique=True,)
    username        = models.CharField(max_length=100,unique=True)
    password        = models.CharField(max_length=100)

    first_name      = models.CharField(max_length=100, blank=True)
    last_name       = models.CharField(max_length=100, blank=True)
    profile_image   = models.ImageField(upload_to=get_profile_image_path , default =get_default_profile_image ,blank=True)

    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    
    
    USERNAME_FIELD = 'email'        # for login # default userneme
    REQUIRED_FIELDS=['username']

    objects= MyAccountManager()

    def __str__(self):
        return self.username

    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]


    # required fun coustom users
    def has_perm(self,perm,obj=None):
        return self.is_active
    
    def has_module_perms(self,app_label):
        return True

