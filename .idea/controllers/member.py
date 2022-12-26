from application import app,db
from flask import Blueprint,request,make_response,redirect
from libs.Helper import ops_renderJSON,ops_renderErrJSON,ops_render
from libs.DataHelper import getCurrentTime
from libs.UrlManager import UrlManager
from models.user import User
from libs.UserService import UserService


member_page = Blueprint( "member_page",__name__ )


@member_page.route("/reg",methods = [ "GET","POST" ])
def reg():
    if request.method == "GET":
        return ops_render("member/reg.html")

    req = request.values
    nickname = req['nickname'] if "nickname" in req else ""
    login_name = req['login_name'] if "login_name" in req else ""
    login_pwd = req['login_pwd'] if "login_pwd" in req else ""
    login_pwd2 = req['login_pwd2'] if "login_pwd2" in req else ""
    email = req['email'] if "email" in req else ""

    if login_name is None or len( login_name ) < 1:
        return ops_renderErrJSON(msg = "Please input correct username")

    if login_pwd is None or len( login_pwd ) < 6:
        return ops_renderErrJSON(msg = "Please input correct password (at least 6 characters)")

    if login_pwd != login_pwd2:
        return ops_renderErrJSON(msg = "The check password is not correct")

    user_info = User.query.filter_by( login_name = login_name ).first()
    if user_info:
        return ops_renderErrJSON(msg = "The username has been registered")

    if email is None:
        return ops_renderErrJSON(msg = "Please input youw email address")

    user_info = User.query.filter_by( email = email ).first()
    if user_info:
        return ops_renderErrJSON(msg = "The email has been registered")

    model_user = User()
    model_user.login_name = login_name
    model_user.nickname = nickname if nickname is not None else login_name
    model_user.login_salt = UserService.geneSalt( 8 )
    model_user.login_pwd = UserService.genePwd( login_pwd,model_user.login_salt )
    model_user.email = email
    model_user.created_time = model_user.updated_time = getCurrentTime()
    db.session.add( model_user )
    db.session.commit()
    return ops_renderJSON(msg = "Successfully register")


@member_page.route("/login",methods = [ "GET","POST" ])
def login():
    if request.method == "GET":
        return ops_render("member/login.html")

    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    if login_name is None or len( login_name ) < 1:
        return ops_renderErrJSON("Please input correct username")

    if login_pwd is None or len( login_pwd ) < 6:
        return ops_renderErrJSON("Please input correct password")
    user_info = User.query.filter_by( login_name = login_name ).first()
    if not user_info:
        return ops_renderErrJSON("Please input correct username and password -1")

    if user_info.login_pwd != UserService.genePwd( login_pwd,user_info.login_salt ):
        return ops_renderErrJSON("Please input correct username and password -2")


    response = make_response( ops_renderJSON( msg="Successfully login" ) )
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s#%s"%( UserService.geneAuthCode( user_info ),user_info.id ),60 * 60 *24 *120 )
    return response