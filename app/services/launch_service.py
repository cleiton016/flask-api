from app.models.launch_model import LaunchModel
from app.services.base_service import BaseService
class LaunchService(BaseService):
    @staticmethod
    def get(id):
        docs = LaunchModel.get(id)
        if docs:
            return LaunchService.serialize(docs)
        return {"error": "Não encontrado"}, 404

    @staticmethod
    def create(data):
        LaunchModel.create(data)
        return {"success": True, "message": "Criado com sucesso"}

    @staticmethod
    def delete(id):
        LaunchModel.delete(id)
        return {"success": True, "message": "Removido"}
