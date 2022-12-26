from models import *
from datetime import datetime
from models.user import session, escape
from user.model import findUser
from flask import Blueprint,render_template,redirect,url_for, request,send_from_directory,flash
shop_page = Blueprint( "shop_page",__name__ )

@shop_page.route("/shop_full")
def shop_full():
    product = getAllShop()
    if 'username' in session:
        carts = getAllCarts(escape(session['username']))
        return render_template("shop-left-sidebar.html",carts=carts,product=product,totalPrices=Prices(carts),adminUser=findUser(escape(session['username'])))
    return render_template("shop-left-sidebar.html",product=product)