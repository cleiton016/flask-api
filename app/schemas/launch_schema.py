from marshmallow import Schema, fields, ValidationError

class LaunchSchema(Schema):
    example = fields.String(required=True)
    
# Instância do schema
launch_schema = LaunchSchema()
