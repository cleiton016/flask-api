from marshmallow import Schema, fields, EXCLUDE
class BaseSchema(Schema):
    id = fields.UUID(dump_only=True)
    status = fields.Boolean(default=True)
    created_by = fields.UUID(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True
        unknown = EXCLUDE
        datetimeformat = '%Y-%m-%dT%H:%M:%S'
    