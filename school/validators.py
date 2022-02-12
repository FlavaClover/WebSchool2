from django.core.exceptions import ValidationError


def validate_age(value):
    if value <= 0:
        raise ValidationError("Age must be a positive number")

