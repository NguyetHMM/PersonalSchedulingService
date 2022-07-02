import json
import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.config import config_dict, FLASK_ENV
from src.core.genetic_algorithm.src.exception.exception import GeneticException
from src.core.tabu_algorithm.src.exception.exception import TabuException
from src.routes import initialize_routes


def create_app(flask_env=FLASK_ENV):
    """_summary_

    Args:
        flask_env (_type_, optional): _description_. Defaults to FLASK_ENV.

    Returns:
        _type_: _description_
    """
    app = Flask(__name__)
    # CORS(app, resources={r"*":{"origins":"*"}}) 

    # Config app
    app.config.from_object(config_dict[flask_env])
    app.app_context().push()

    api = Api(app)

    initialize_routes(api)

    return app


app = create_app()


@app.errorhandler(GeneticException)
def handle_exception(e):
    return {
               'message': e.message,
           }, 422


@app.errorhandler(TabuException)
def handle_exception(e):
    return {
               'message': e.message,
           }, 422
