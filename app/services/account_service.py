from app.models.account_model import AccountModel
from app.services.base_service import BaseService
class AccountService(BaseService):
    @staticmethod
    def get(id):
        docs = AccountModel.get(id)
        if docs:
            return AccountService.serialize(docs)
        return {"error": "Não encontrado"}, 404

    @staticmethod
    def create( data):
        AccountModel.create(data)
        return {"success": True, "message": "Criado com sucesso"}
    
    @staticmethod
    def update(id, data):
        AccountModel.update(id, data)
        return {"success": True, "message": "Atualizado com sucesso"}

    @staticmethod
    def delete(id):
        AccountModel.delete(id)
        return {"success": True, "message": "Removido"}
