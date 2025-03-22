from flask import request, jsonify
from app.schemas.account_schema import account_schema
from app.services.account_service import AccountService

class AccountController:
    @staticmethod
    def get(id):
        return jsonify(AccountService.get(id))

    @staticmethod
    def create():
        try:
            data = account_schema.load(request.json)
            return jsonify(AccountService.create(data))
        except Exception as e:
            return {"error": str(e)}, 400

    @staticmethod
    def update(id):
        try:
            data = account_schema.load(request.json)
            return jsonify(AccountService.update(id, data))
        except Exception as e:
            return {"error": str(e)}, 400
    @staticmethod
    def delete(id):
        return jsonify(AccountService.delete(id))
