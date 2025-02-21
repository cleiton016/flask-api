from babel.numbers import format_currency

class BaseService:
    @staticmethod
    def serialize(data) -> list:
        list = []
        for item in data:
            obj = item.to_dict()
            obj["id"] = item.id
            list.append(obj)
        return list
    
    @staticmethod
    def serialize_paginated(data) -> dict:
        data = BaseService.serialize(data)
        return {
            "data": data,
            "last_doc_id": data[-1]["id"] if data else None
        }
    @staticmethod
    def serialize_one(data) -> dict:
        return data.to_dict()
    
    @classmethod
    def format_amount(cls, amount: float) -> str:
        """Converte float (ex: 199.99) para string formatada (ex: 'R$ 199,99')"""
        return format_currency(amount, "BRL", locale="pt_BR")

    @classmethod
    def unformat_amount(cls, amount: str) -> float:
        """Converte string formatada (ex: 'R$ 199,99') para float (ex: 199.99)"""
        return float(amount.replace("R$", "").replace(".", "").replace(",", ".").strip())