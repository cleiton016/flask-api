from marshmallow import Schema, fields, ValidationError
import re
from app.schemas.base_schema import BaseSchema

def validate_slug(value):
    if not value:
        raise ValidationError("O campo slug é obrigatório")
    if len(value) < 3:
        raise ValidationError("O campo slug deve ter no mínimo 3 caracteres")
    if not re.match(r"^[a-z0-9_]*$", value):
        raise ValidationError("O campo slug deve conter apenas letras minúsculas, números e underline")


class TagSchema(BaseSchema):
    nome = fields.String(required=True)
    slug = fields.String(required=True, validate=validate_slug)
    descricao = fields.String(required=True)
    cor = fields.String(required=True)
    dedutivel = fields.Boolean(required=True, default=False)
    codigoIrpf = fields.String(required=False)

    
# Instância do schema
tag_schema = TagSchema()
