from rest_framework import serializers
from .models import TelegramUser, Payment, Message


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ["telegram_id", "first_name", "phone", "username"]

    def validate(self, data):
        if not data.get("first_name"):
            raise serializers.ValidationError({"first_name": "This field is required."})
        return data

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["user", "chek", "is_confirmed"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["user", "text", "image", "video", "date"]

from rest_framework import serializers
from .models import TelegramUser, Referral

class TelegramUserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = "__all__"

class ReferralSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer()

    class Meta:
        model = Referral
        fields = "__all__"
