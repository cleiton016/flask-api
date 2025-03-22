from marshmallow import Schema, fields, ValidationError

from app.schemas.account_schema import AccountSchema
from app.schemas.base_schema import BaseSchema
from app.schemas.tag_schema import TagSchema

class LaunchSchema(BaseSchema):
    nome = fields.String(required=True)
    valor = fields.Float(required=True)
    data = fields.DateTime(required=True)
    parcelado = fields.Boolean(required=False, default=False)
    parcelas = fields.Integer(required=False, default=1)
    tipoTransacaoRef = fields.String(required=False)
    transacaoRef = fields.String(dump_only=True)
    accountRef = fields.String(required=True)
    tagRef = fields.String(required=True)
    ## Campos para imposto de renda
    cpf_cnpj = fields.String(required=False, validate=lambda value: len(value) in [11, 14])
    valorReembolso = fields.Float(required=False, default=0.00)
    
class LaunchQuerySchema(Schema):
    month = fields.Date(format="%d/%m/%Y", required=False)
    tag = fields.String(required=False)
    nome = fields.String(required=False)
    limit = fields.Integer(required=False)
    parcelado = fields.Boolean(required=False)
    last_doc_id = fields.String(required=False)
    order_by = fields.String(required=False)
    offset = fields.Integer(required=False)

# Instância do schema
launch_schema = LaunchSchema()
launch_query_schema = LaunchQuerySchema()
