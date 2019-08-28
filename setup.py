import os
from flask import Flask
from src.routes.analysis import analysis

def setup_app():
    blueprints = [
        dict(bp=analysis, prefix='/api/analysis')
    ]

    app = Flask(__name__)

    for bp in blueprints:
        app.register_blueprint(
            bp.get('bp'),
            url_prefix=bp.get('prefix')
        )

    return app

PORT = os.getenv('PORT', 8000)

app = setup_app()
