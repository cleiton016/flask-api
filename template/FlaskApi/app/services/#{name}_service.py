from app.models.#{name}_model import #{nameUp}Model
from app.services.base_service import BaseService
class #{nameUp}Service(BaseService):
    @staticmethod
    def get(id):
        docs = #{nameUp}Model.get(id)
        if docs:
            return #{nameUp}Service.serialize(docs)
        return {"error": "Não encontrado"}, 404

    @staticmethod
    def create(data):
        #{nameUp}Model.create(data)
        return {"success": True, "message": "Criado com sucesso"}

    @staticmethod
    def delete(id):
        #{nameUp}Model.delete(id)
        return {"success": True, "message": "Removido"}
