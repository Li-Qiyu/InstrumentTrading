import math
from os import path
from werkzeug.utils import secure_filename
from libs import UserService
from libs.DataHelper import getCurrentTime
from libs.Helper import ops_render, ops_renderErrJSON, ops_renderJSON
from models import *
from datetime import datetime
from models.user import *
from models.shop import *
from flask import Blueprint, render_template, redirect, url_for, request, send_from_directory, flash

shop_page = Blueprint("shop_page", __name__)


def sortAndSelect(order, category):
    if order == 1:
        product = getAllShopByTime()
    elif order == 2:
        product = getAllShopByAZ()
    elif order == 3:
        product = getAllShopByZA()
    elif order == 4:
        product = getAllShopByPriceUp()
    elif order == 5:
        product = getAllShopByPriceDown()
    else:
        product = getAllShopByTime()
    selected = []
    if category == "all":
        for i in product:
            selected.append(i)
    else:
        for i in product:
            if i.category == category:
                selected.append(i)
    return selected


@shop_page.route("/shop_full/<string:lan>/<string:category>/<int:order>/<int:page>", methods=['POST', 'GET'])
def shop_full(lan, category, order, page):
    if request.method == 'GET':
        fullPath = request.full_path
        pathList = fullPath.split(sep="/")
        category = pathList[4]
        order = pathList[5]
        product = sortAndSelect(order, category)
        categories = getAllCategories()
        categories2 = getAllCategories2()
        allProduct = getAllShop()
        allNum = len(allProduct)
        selectedNum = len(product)
        pageNum = math.ceil(selectedNum / 8)
        if 'username' in session:
            carts = getAllCarts(session['username'])
            return render_template("shop-list.html", carts=carts, product=product, categories=categories,
                                   categories2=categories2, allNum=allNum,
                                   pageNum=pageNum, page=page, order=order, category=category, selectedNum=selectedNum,
                                   lan=lan)
        return render_template("shop-list.html", product=product, categories=categories, categories2=categories2,
                               allNum=allNum, pageNum=pageNum,
                               page=page, order=order, category=category, selectedNum=selectedNum, lan=lan)
    if request.method == 'POST':
        fullPath = request.full_path
        pathList = fullPath.split(sep="/")
        category = pathList[4]
        order = pathList[5]
        product = sortAndSelect(order, category)
        categories = getAllCategories()
        categories2 = getAllCategories2()
        allProduct = getAllShop()
        allNum = len(allProduct)
        selectedNum = len(product)
        pageNum = math.ceil(selectedNum / 8)
        if 'username' in session:
            carts = getAllCarts(session['username'])
            return render_template("shop-list.html", carts=carts, product=product, categories=categories,
                                   categories2=categories2, allNum=allNum,
                                   pageNum=pageNum, page=page, order=order, category=category, selectedNum=selectedNum,
                                   lan=lan)
        return render_template("shop-list.html", product=product, categories=categories, allNum=allNum, pageNum=pageNum,
                               page=page, order=order, category=category, categories2=categories2,
                               selectedNum=selectedNum, lan=lan)


@shop_page.route("/single_product/<int:id>/<string:lan>", methods=['GET', 'POST'])
def single_product(id, lan):
    ID = findProductID(id)
    products = getAllShopByTime()
    reviews = getAllProductReviews(id)
    if request.method == "GET":
        if 'username' in session:
            username = session['username']
            carts = getAllCarts(username)
            isTrue = isExisted(username, ID.productName)
            order = isExistedOrder(username, ID.productName)
            return render_template('single-product.html', carts=carts, ID=ID, id=id - 1, products=products[0:6],
                                   isTrue=isTrue, order=order, reviews=reviews, reviewNum=len(reviews), lan=lan)
        return render_template('single-product.html', ID=ID, id=id - 1, products=products[0:4], reviews=reviews,
                               reviewNum=len(reviews), lan=lan)



@shop_page.route("/review/<int:id>/<string:lan>",methods=['GET','POST'])
def review(id,lan):
    ID = findProductID(id)
    products = getAllShopByTime()
    reviews = getAllProductReviews(id)
    if request.method == 'POST':
        if 'username' in session:
            productReviews = request.form.get('review', None)
            score = request.form.get('score',None)
            print(productReviews)
            reviews = ProductReviews(id, session['username'], productReviews, score)
            reviews.addProductReviews()
            return redirect(url_for('shop_page.single_product', id=id, lan=lan))
        return render_template('single-product.html', ID=ID, products=products[0:4], reviews=reviews,
                               reviewNum=len(reviews), lan=lan)
    if request.method == "GET":
        if 'username' in session:
            username = session['username']
            carts = getAllCarts(username)
            isTrue = isExisted(username, ID.productName)
            order = isExistedOrder(username, ID.productName)
            return render_template('newReview.html', carts=carts, ID=ID, id=id - 1, products=products[0:6],
                                   isTrue=isTrue, order=order, reviews=reviews, reviewNum=len(reviews), lan=lan)
        return render_template('single-product.html', ID=ID, id=id - 1, products=products[0:4], reviews=reviews,
                               reviewNum=len(reviews), lan=lan)



@shop_page.route('/cart/<string:lan>')
def carts(lan):
    if 'username' in session:
        carts = getAllCarts(session['username'])
        return render_template("cart.html", carts=carts, totalPrices=Prices(carts), lan=lan)
    flash("Please login")
    return redirect(url_for('member_page.login'))


def Prices(carts):
    a = []
    for p in carts:
        a.append(p.price)
    totalPrices = sum([float(i) for i in a])
    return totalPrices


@shop_page.route('/checkout/<string:lan>')
def checkout(lan):
    # if request.method == 'POST':
    #     addressusername = request.form.get('username')
    #     userPhone = request.form.get('userPhone')
    #     town = request.form.get('town')
    #     detailedAddress = request.form.get('detailedAddress')
    #     print(detailedAddress)
    #     postCode = request.form.get('postCode')
    #     email = request.form.get('email')
    #     note = request.form.get('note')
    #     user_address = Address(1, addressusername, userPhone, town, detailedAddress, postCode, email, note)
    #     user_address.addAddress()
    #     return redirect(url_for('shop_page.checkout', lan=lan))

    # if request.method == 'GET':
    if 'username' in session:
        user = findUser(session['username'])
        address = findAddress(session['username'])
        carts = getAllCarts(session['username'])
        return render_template('checkout.html', lan=lan, carts=carts, totalPrices=Prices(carts),
                               username=session['username'], address=address, user=user, price=Prices(carts))
    flash("Please login")
    return redirect(url_for('member_page.login'))


@shop_page.route('/order/<string:lan>')
def orders(lan):
    if 'username' in session:
        carts = getAllCarts(session['username'])
        submitOrder(session['username'])
        for cart in carts:
            delCart(cart.id)
        if lan == "e":
            return redirect(url_for('index_page.index'))
        elif lan == "c":
            return redirect(url_for('index_page.index2'))


@shop_page.route('/pay/<string:lan>')
def pay(lan):
    return render_template('pay.html',lan=lan)


@shop_page.route('/addcs/<int:idsss>/<string:lan>', methods=['GET', 'POST'])
def addcartssss(idsss,lan):
    if 'username' in session:
        name = session['username']
        ID = findProductID(idsss)
        usercart = Cart(idsss, name, ID.productName, ID.productName2, ID.price, ID.images, ID.description, 1)
        usercart.addCart()
        return redirect(url_for('shop_page.single_product',lan=lan, id=ID.id))
    flash("Please login")
    return redirect(url_for('member_page.login'))


@shop_page.route('delcart/<int:id>')
def delcart(id):
    if 'username' in session:
        delCart(id)
        return redirect(url_for('shop_page.carts'))
    return redirect(url_for('shop_page.carts'))