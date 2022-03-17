from flask import Blueprint

registerp = Blueprint ('registerp',__name__, template_folder= 'templates' )

from . import registerp_routes