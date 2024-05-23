from flask import Blueprint

forms = Blueprint ('forms',__name__, template_folder= 'templates' )

from . import forms_routes