from flask import Blueprint
import os
def register_blueprints(app):
    """Percorre a pasta routes e registra todos os blueprints"""
    for file in os.listdir("app/routes"):
        if file.endswith("_router.py"):
            module_name = file[:-3]  # Remove o ".py" da extensão
            bp_name = module_name.split("_")[0] + "_bp"
            module = __import__("app.routes." + module_name, fromlist=[module_name])
            blueprint = getattr(module, bp_name)
            app.register_blueprint(blueprint)
