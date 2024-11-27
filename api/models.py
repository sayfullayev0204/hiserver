from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=50, blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.first_name


class Payment(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    chek = models.ImageField(upload_to="check/")
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} Payment"


class Message(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="message/", blank=True)
    video = models.FileField(upload_to="message/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    message_id = models.BigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.text[:10] + "..."

class Referral(models.Model):
    user = models.OneToOneField(TelegramUser, on_delete=models.CASCADE, related_name="referral")
    invited_users = models.ManyToManyField(TelegramUser, related_name="invited_by", blank=True)
    referral_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username or self.user.telegram_id} - {self.referral_count} referrals"

class Channel(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.name
