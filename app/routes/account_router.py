from flask import Blueprint
from app.controllers.account_controller import AccountController

account_bp = Blueprint("account", __name__)

account_bp.route("/accounts/<id>", methods=["GET"])(AccountController.get)
account_bp.route("/accounts", methods=["POST"])(AccountController.create)
account_bp.route("/accounts/<id>", methods=["PUT"])(AccountController.update)
account_bp.route("/accounts/<id>", methods=["DELETE"])(AccountController.delete)
