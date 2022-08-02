from flask import Blueprint

articles = Blueprint ('articles',__name__, template_folder= 'templates' )

from . import articles_routes