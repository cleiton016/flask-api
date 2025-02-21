from marshmallow import Schema, fields, ValidationError

class LaunchSchema(Schema):
    nome = fields.String(required=True)
    valor = fields.Float(required=True)
    data = fields.DateTime(required=True)
    parcelado = fields.Boolean(required=False, default=False)
    parcelas = fields.Integer(required=False, default=1)
    tag = fields.String(required=False)
    accountRef = fields.String(required=True)

    
class LaunchQuerySchema(Schema):
    month = fields.Date(format="%d/%m/%Y", required=False)
    tag = fields.String(required=False)
    nome = fields.String(required=False)
    limit = fields.Integer(required=False)
    last_doc_id = fields.String(required=False)
    order_by = fields.String(required=False)
    offset = fields.Integer(required=False)

# Instância do schema
launch_schema = LaunchSchema()
launch_query_schema = LaunchQuerySchema()
