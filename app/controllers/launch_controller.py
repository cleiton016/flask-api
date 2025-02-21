from flask import request, jsonify
from app.schemas.launch_schema import launch_schema, launch_query_schema
from app.services.launch_service import LaunchService

class LaunchController:
    @staticmethod
    def get(id):
        ## ober os query params
        params = launch_query_schema.load(request.args)
        return jsonify(LaunchService.get(id, params))

    @staticmethod
    def create():
        try:
            data = launch_schema.load(request.json)
            return jsonify(LaunchService.create(data))
        except Exception as e:
            return {"error": str(e)}, 400

    @staticmethod
    def delete(id):
        return jsonify(LaunchService.delete(id))
