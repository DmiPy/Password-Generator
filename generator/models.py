from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    login = models.CharField("Login", max_length = 100)
    password = models.CharField("Password",max_length = 16)
    website = models.URLField("URL")
    date = models.DateField("Date")
    isSaved = models.BooleanField(default = False)

    def __str__(self):
        if len(self.login) > 0:
            return f"{self.login}"
        else:
            return f"{self.password}"