from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
