# app/schemas/user_schema.py

from marshmallow import Schema, fields, ValidationError, validates


# DRY
class UserDataValidationMixin:
    @validates('user_name')
    def validate_user_name_length(self, value: str):
        if value and not (3 <= len(value) <= 30):
            raise ValidationError(
                "Username must be between 3 and 30 characters long."
            )

    @validates('password')
    def validate_password_length(self, value: str):
        if value and not (3 <= len(value) <= 50):
            raise ValidationError(
                "Password must be between 3 and 50 characters long."
            )


class UserCreateSchema(Schema, UserDataValidationMixin):
    user_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class UserUpdateSchema(Schema, UserDataValidationMixin):
    user_name = fields.Str(required=False)
    email = fields.Email(required=False)
    password = fields.Str(required=False)

    def validate(self, data, *args, **kwargs):
        errors = {}

        # Check if at least one field is provided
        if not any(field in data for field in ['user_name', 'email', 'password']):
            errors['__all__'] = "At least one of user_name, email, or password must be provided."

        if errors:
            raise ValidationError(errors)
        return data


# Create schema instances
user_create_schema = UserCreateSchema()
user_update_schema = UserUpdateSchema()
