from flask import Blueprint
from app.controllers.tag_controller import TagController

tag_bp = Blueprint("tag", __name__)

tag_bp.route("/tags/<id>", methods=["GET"])(TagController.get)
tag_bp.route("/tags", methods=["POST"])(TagController.create)
tag_bp.route("/tags/<id>", methods=["PUT"])(TagController.update)
tag_bp.route("/tags/<id>", methods=["DELETE"])(TagController.delete)
