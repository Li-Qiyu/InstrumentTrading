from application import app, db
from flask import Blueprint, request, make_response, redirect
from libs.Helper import ops_renderJSON, ops_renderErrJSON, ops_render
from libs.DataHelper import getCurrentTime
from libs.UrlManager import UrlManager
from models.user import User
from libs.UserService import UserService
from flask import Blueprint, render_template, request, url_for, redirect, session, escape, flash
from models.user import *
from models.shop import *

member_page = Blueprint("member_page", __name__)


@member_page.route('/reg/<string:lan>', methods=['GET', 'POST'])
def reg(lan):
    if request.method == 'POST':
        nickname = request.form.get('nickname', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        email = request.form.get('email', None)
        user = User(nickname, username, password, email, None)
        if user.isExisted():
            return ops_renderErrJSON("Failed")
        else:
            user.addUser()
            session['username'] = username
            session.permanent = True
            if lan == "e":
                return render_template("index.html", lan=lan)
            elif lan == "c":
                return render_template("index.html", lan=lan)
    return render_template("reg.html", lan=lan)


@member_page.route('/login/<string:lan>', methods=['GET', 'POST'])
def login(lan):
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        user = User(None, username, password, None, None)
        if user.isExisted():
            session['username'] = username
            session.permanent = True
            if lan == "e":
                return redirect(url_for('index_page.index'))
            elif lan == "c":
                return redirect(url_for('index_page.index2'))
        else:
            return ops_renderErrJSON("Failed")
    return render_template('login.html', lan=lan)


@member_page.route('/logout/<string:lan>')
def logout(lan):
    session.pop('username', None)
    return redirect(url_for('member_page.login', lan=lan))


@member_page.route('/my_account/<string:lan>')
def my_account(lan):
    if 'username' in session:
        user = findUser(session['username'])
        address = getAddress(session['username'])
        carts = getAllCarts(session['username'])
        orders = getAllOrder(session['username'])
        return render_template('my-account.html', user=user, carts=carts, totalPrices=Prices(carts), orders=orders,
                               address=address, lan=lan)
    flash("Please login")
    return redirect(url_for('member_page.login', lan=lan))


def Prices(carts):
    a = []
    for p in carts:
        a.append(p.price)
    Product = len(a)
    totalPrices = sum([float(i) for i in a])
    return totalPrices, Product


@member_page.route('/edit_account/<string:lan>')
def edit_account(lan):
    if 'username' in session:
        user = findUser(session['username'])
        return render_template('editAccount.html', user=user, lan=lan)
    return redirect(url_for('member_page.login',lan=lan))


@member_page.route('/modify_account/<id>', methods=['GET', 'POST'])
def modify_account(id):
    if request.method == 'POST':
        if 'username' in session:
            password = request.form.get('password', None)
            email = request.form.get('email', None)
            modifyUser(session['username'], password, email)
            return redirect(url_for('member_page.my_account'))


@member_page.route('/edit_address/<string:lan>')
def edit_address(lan):
    if 'username' in session:
        address = findAddress(session['username'])
        return render_template('editAddress.html', address=address, lan=lan)
    return redirect(url_for('member_page.login',lan=lan))


@member_page.route('/modify_address/<string:username>/<string:lan>', methods=['GET', 'POST'])
def modify_address(username,lan):
    if request.method == 'POST':
        if 'username' in session:
            addressName = request.form.get('addressName', None)
            phone = request.form.get('phone', None)
            country = request.form.get('country', None)
            town = request.form.get('town', None)
            detail = request.form.get('detail', None)
            postCode = request.form.get('postCode', None)
            modifyAddress(session['username'], addressName, phone, country, town, detail, postCode)
            return redirect(url_for('member_page.my_account',lan=lan))
