from flask import Blueprint, render_template, session, request, url_for, redirect

from models.shop import *
from models.user import getNickname

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    login = False
    if 'username' in session:
        login = True
        carts = getAllCarts(session['username'])
        return render_template("index.html", producti=getAllShop(), login=login, carts=carts, lan="e")
    return render_template("index.html", producti=getAllShop(), login=login, lan="e")


@index_page.route("/c")
def index2():
    login = False
    if 'username' in session:
        login = True
        carts = getAllCarts(session['username'])
        return render_template("index.html", producti=getAllShop(), login=login, carts=carts, lan="c")
    return render_template("index.html", producti=getAllShop(), login=login, lan="c")


@index_page.route('/search/<string:lan>', methods=['post', 'get'])
def search(lan):
    productName = request.form.get('search')
    if productName is None:
        productName = " "
    result = " "
    if lan == "e":
        result = searchProduct(productName)
    elif lan == "c":
        result = searchProduct2(productName)
    return render_template('search.html', result=result, lan=lan)


@index_page.route("/contact/<string:lan>")
def contact(lan):
    login = False
    if 'username' in session:
        login = True
        carts = getAllCarts(session['username'])
        return render_template("contact.html", lan=lan, producti=getAllShop(), login=login, carts=carts)
    return render_template("contact.html", lan=lan, producti=getAllShop(), login=login)
