from flask import request, jsonify
from app.schemas.#{name}_schema import #{name}_schema
from app.services.#{name}_service import #{nameUp}Service

class #{nameUp}Controller:
    @staticmethod
    def get(id):
        return jsonify(#{nameUp}Service.get(id))

    @staticmethod
    def create():
        try:
            data = #{name}_schema.load(request.json)
            return jsonify(#{nameUp}Service.create(data))
        except Exception as e:
            return {"error": str(e)}, 400

    @staticmethod
    def delete(id):
        return jsonify(#{nameUp}Service.delete(id))
