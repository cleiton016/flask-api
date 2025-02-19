from flask import Blueprint
from app.controllers.#{name}_controller import #{nameUp}Controller

#{name}_bp = Blueprint("#{name}", __name__)

#{name}_bp.route("/#{name}s/<id>", methods=["GET"])(#{nameUp}Controller.get)
#{name}_bp.route("/#{name}s", methods=["POST"])(#{nameUp}Controller.create)
#{name}_bp.route("/#{name}s/<id>", methods=["DELETE"])(#{nameUp}Controller.delete)
