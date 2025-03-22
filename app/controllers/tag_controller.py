from flask import request, jsonify
from app.schemas.tag_schema import tag_schema
from app.services.tag_service import TagService

class TagController:
    @staticmethod
    def get(id):
        return jsonify(TagService.get(id))

    @staticmethod
    def create():
        try:
            data = tag_schema.load(request.json)
            return jsonify(TagService.create(data))
        except Exception as e:
            return {"error": str(e)}, 400

    @staticmethod
    def update(id):
        try:
            data = tag_schema.load(request.json)
            return jsonify(TagService.update(id, data))
        except Exception as e:
            return {"error": str(e)}, 400
        
    @staticmethod
    def delete(id):
        return jsonify(TagService.delete(id))
