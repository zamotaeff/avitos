from rest_framework import serializers


def not_published(value):
    if value:
        raise serializers.ValidationError(f"Поле is_published не может быть True")
