# app/schemas/user_schema.py

from marshmallow import Schema, fields, ValidationError, validates, pre_load
from marshmallow.validate import Length


class ValidationMixin():
    @pre_load
    def trim_whitespace(self, data, **kwargs):
        # Trim whitespace from all string fields before validation
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data

    @validates('password')
    def validate_password_strength(self, value: str):
        # Example password strength validation
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isupper() for char in value):
            raise ValidationError(
                "Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise ValidationError(
                "Password must contain at least one lowercase letter.")
        if not any(char in '!@#$%^&*()_+' for char in value):
            raise ValidationError(
                "Password must contain at least one special character.")
# Custom field for validating string length


class ValidatedStr(fields.Str, ValidationMixin):
    def __init__(self, *args, min_length=3, max_length=50, **kwargs):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(validate=Length(min=min_length, max=max_length), *args, **kwargs)

    def _validate(self, value):
        super()._validate(value)
        if len(value) < self.min_length or len(value) > self.max_length:
            raise ValidationError(
                f"Field must be between {self.min_length} and {
                    self.max_length} characters long."
            )

# Schema for creating a new user


class UserCreateSchema(Schema, ValidationMixin):
    user_name = ValidatedStr(required=True, min_length=3, max_length=30)
    email = fields.Email(required=True)
    password = ValidatedStr(required=True, min_length=8, max_length=50)


# Schema for updating user details


class UserUpdateSchema(Schema):
    user_name = ValidatedStr(required=False, min_length=3, max_length=30)
    email = fields.Email(required=False)
    password = ValidatedStr(required=False, min_length=8, max_length=50)


# Create schema instances
user_create_schema = UserCreateSchema()
user_update_schema = UserUpdateSchema()
