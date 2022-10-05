from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator

min_length_validator = MinLengthValidator(3)

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(blank=True, null=True, editable=False)