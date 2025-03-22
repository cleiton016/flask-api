from flask import Blueprint
from app.controllers.launch_controller import LaunchController

launch_bp = Blueprint("launch", __name__)

launch_bp.route("/launch/<id>", methods=["GET"])(LaunchController.get)
launch_bp.route("/launch", methods=["POST"])(LaunchController.create)
launch_bp.route("/launch/<id>", methods=["PUT"])(LaunchController.update)
launch_bp.route("/launch/<id>", methods=["DELETE"])(LaunchController.delete)
