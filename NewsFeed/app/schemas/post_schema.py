# app/schemas/post_schema.py
from marshmallow import Schema, fields, ValidationError, validates, validate


class PostSchema(Schema):
    user_id = fields.Int(required=True)
    content = fields.Str(required=True, validate=validate.Length(
        3, 300))

    @validates('user_id')
    def validate_user_id(self, value: int):
        if value <= 0:
            raise ValidationError("User ID must be greater than 0")


# Create schema instances
post_create_schema = PostSchema()
post_update_schema = PostSchema(only=("content",))
