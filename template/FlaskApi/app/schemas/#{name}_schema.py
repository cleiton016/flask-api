from marshmallow import Schema, fields, ValidationError

class #{nameUp}Schema(Schema):
    example = fields.String(required=True)
    
# Instância do schema
#{name}_schema = #{nameUp}Schema()
