# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from .auth import auth_views
from .user import user_views
from .index import index_views
from .driver import driver_views
from .request import request_views
from .resident import resident_views
from .street import street_views

def init_views(app):
    app.register_blueprint(auth_views)
    app.register_blueprint(user_views)
    app.register_blueprint(index_views)
    app.register_blueprint(driver_views)
    app.register_blueprint(request_views)
    app.register_blueprint(resident_views)
    app.register_blueprint(street_views)


views = [auth_views, user_views, index_views, driver_views, request_views, resident_views, street_views]
# blueprints must be added to this list