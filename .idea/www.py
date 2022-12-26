from application import app

from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension( app )

# from interceptors.Auth import *
# from interceptors.errorHandler import *

from controllers.index import index_page
app.register_blueprint( index_page,url_prefix = "/" )
from controllers.member import member_page
app.register_blueprint( member_page,url_prefix = "/member" )
from controllers.about import about_page
app.register_blueprint( about_page,url_prefix = "/about" )
from controllers.shop import shop_page
app.register_blueprint( shop_page,url_prefix = "shop" )