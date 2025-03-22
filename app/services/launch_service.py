import datetime
import uuid
from app.models.launch_model import LaunchModel
from app.schemas.launch_schema import LaunchSchema
from app.services.base_service import BaseService
class LaunchService(BaseService):
    @staticmethod
    def get(id, params: dict):
        docs = LaunchModel.get(id, params)
        def month_filter(document):
            date = document.get("data")
            date_obj = datetime.datetime.date(date)
            date_filter = params.get("month")
            return date_obj.month == date_filter.month and date_obj.year == date_filter.year
        
        def filter_by_param(document, param):
            # dever fazer uma busca aproximada
            return document.get(param).lower().find(params.get(param).lower()) != -1
        if params.get("month"):
            docs = [doc for doc in docs if month_filter(doc)]
        if params.get("tag"):
            docs = [doc for doc in docs if filter_by_param(doc, "tag")]
        if params.get("nome"):
            docs = [doc for doc in docs if filter_by_param(doc, "nome")]
        
        
        if docs:
            return LaunchService.serialize_paginated(docs)
        return {"error": "Não encontrado"}, 404

    @staticmethod
    def create(data: dict):
        data["valorParcela"] = LaunchService.format_amount(data.get("valor") / data.get("parcelas"))
        data["valor"] = LaunchService.format_amount(data.get("valor"))
        idTransacao = str(uuid.uuid4())
        if data.get("parcelado"):
            for i in range(data.get("parcelas")):
                data["numeroParcela"] = i + 1
                data["transacaoRef"] = idTransacao # id da transação para identificar as parcelas
                LaunchModel.create(data)
        else:
            data["numeroParcela"] = 1
            data["transacaoRef"] = idTransacao
            LaunchModel.create(data)
        return {"success": True, "message": "Criado com sucesso"}
    
    @staticmethod
    def update(id, data):
        LaunchModel.update(id, data)
        return {"success": True, "message": "Atualizado com sucesso"}

    @staticmethod
    def delete(id):
        return LaunchModel.delete(id)