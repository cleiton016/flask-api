from marshmallow import Schema, fields, ValidationError

class AccountSchema(Schema):
    contaSalario = fields.Boolean(required=True, default=False, error_messages={"required": "O campo contaSalario é obrigatório"})
    creditoUsado = fields.String(required=False)
    limite = fields.String(required=True, error_messages={"required": "O campo limite é obrigatório"})
    nome = fields.String(required=True, error_messages={"required": "O campo nome é obrigatório"})
    receitaMensal = fields.String(required=False)
    saldo = fields.String(required=False)
    userRef = fields.String(required=True, )

# Instância do schema
account_schema = AccountSchema()
