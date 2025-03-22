from app.models.tag_model import TagModel
from app.services.base_service import BaseService
class TagService(BaseService):
    @staticmethod
    def get(id):
        docs = TagModel.get(id)
        if docs:
            return TagService.serialize(docs)
        return {"error": "Não encontrado"}, 404

    @staticmethod
    def create(data):
        TagModel.create(data)
        return {"success": True, "message": "Criado com sucesso"}
    
    @staticmethod
    def update(id, data):
        TagModel.update(id, data)
        return {"success": True, "message": "Atualizado com sucesso"}

    @staticmethod
    def delete(id):
        return TagModel.delete(id)
