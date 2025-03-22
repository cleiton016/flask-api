from flask import Blueprint

public_bp = Blueprint("public", __name__)

public_bp.route("/public", methods=["GET"])(lambda : "Hello from public route")
