from flask import Blueprint
from app.controllers.tag_controller import TagController

tag_bp = Blueprint("public", __name__)

tag_bp.route("/public", methods=["GET"])(lambda : "Hello from public route")
