
# Create your models here.
from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or self.telegram_id
