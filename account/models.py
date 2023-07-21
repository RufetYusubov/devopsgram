from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib import auth

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    
    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()



class AccountModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    Gender_Choices = (
        ('Female' , 'Female'),
        ('Male','Male')
    )
    gender = models.CharField(max_length=20,blank=True,null=True,choices=Gender_Choices)
    friends = models.ManyToManyField("self",blank=True,null=True,related_name="user_friends")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = "Account"
        ordering = ["-id"]

    objects = UserManager()

    
class ProfileAboutModel(models.Model):
    user = models.OneToOneField(AccountModel,on_delete=models.CASCADE,related_name="user_profile")
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=10)
    martail_status = models.CharField(max_length=10,blank=True,null=True)
    location = models.CharField(max_length=40)
    job = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Profile about"


    def __str__(self) -> str:
        return self.name + " " + self.surname
    


    

