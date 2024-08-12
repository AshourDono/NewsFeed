# app/schemas/post_schema.py
from marshmallow import Schema, fields, ValidationError, validates


# DRY
class ContentValidationMixin:
    @validates('content')
    def validate_content_length(self, value: str):
        if not (3 <= len(value) <= 300):
            raise ValidationError(
                "Content must be between 3 and 200 characters long."
            )


class PostCreateSchema(Schema, ContentValidationMixin):
    user_id = fields.Int(required=True)
    content = fields.Str(required=True)

    @validates('user_id')
    def validate_user_id(self, value: int):
        if value <= 0:
            raise ValidationError("User ID must be greater than 0")


class PostUpdateSchema(Schema, ContentValidationMixin):
    content = fields.Str(required=True)


# Create schema instances
post_create_schema = PostCreateSchema()
post_update_schema = PostUpdateSchema()
