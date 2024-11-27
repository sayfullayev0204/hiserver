from django.contrib import admin
from .models import TelegramUser, Payment, Message,Referral

admin.site.register(TelegramUser)
admin.site.register(Payment)
admin.site.register(Message)
admin.site.register(Referral)
