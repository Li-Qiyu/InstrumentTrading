import os
from datetime import datetime
from flask import Flask, request, make_response, render_template, redirect, url_for, app, Blueprint
from werkzeug.utils import secure_filename
from os import path

from models.shop import *
from models.user import *

staff_page = Blueprint("staff_page", __name__)

base_path = path.abspath(path.dirname(""))
upload_path = path.join(base_path, 'static\\uploads\\')

ALLOWED_EXTENSIONS = ['.jpg', '.png', '.gif']


def allowed_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS


def checkAdmin(username):
    adminList = getAdmin()
    if username in adminList:
        return True
    else:
        return False


@staff_page.route('/<string:lan>', methods=['GET'])
def warn(lan):
    return render_template('error.html', lan=lan)


@staff_page.route('/delete-product/<int:id>/<string:lan>')
def delete_product(id, lan):
    delProduct(id)
    return redirect(url_for('staff_page.show_product', lan=lan))


@staff_page.route('/new-product/<string:lan>', methods=['GET', 'POST'])
def new_product(lan):
    if 'username' in session:
        username = findUser(session['username'])
        ifAdmin = checkAdmin(username)
        if ifAdmin:
            if request.method == 'GET':
                return render_template('newProduct.html', lan=lan)
            if request.method == 'POST':
                productName = request.form.get('productName', None)
                productName2 = request.form.get('productName2', None)
                price = request.form.get('price', None)
                description = request.form.get('description', None)
                description2 = request.form.get('description2', None)
                category = request.form.get('category', None)
                category2 = request.form.get('category2', None)
                img_path = None
                image = request.files.get('image')
                if allowed_file(image.filename):
                    img_path = datetime.now().strftime('%Y%m%d%H%M%f') + os.path.splitext(image.filename)[1]
                    image.save(os.path.join(upload_path, img_path))
                images = "/static/uploads/" + str(img_path)
                product = Product(productName=productName, productName2=productName2, price=price, images=images,
                                  description=description, description2=description2, score=None, category=category,
                                  category2=category2)
                product.addShop()
                return redirect(url_for('staff_page.show_product', lan=lan))
        else:
            return redirect(url_for('staff_page.warn', lan=lan))
    return redirect(url_for('member_page.login', lan=lan))


@staff_page.route('/show-product/<string:lan>')
def show_product(lan):
    if 'username' in session:
        username = findUser(session['username'])
        ifAdmin = checkAdmin(username)
        if ifAdmin:
            if request.method == 'GET':
                products = getAllShop()
                return render_template('delProduct.html', products=products, lan=lan)
        else:
            return redirect(url_for('staff_page.warn', lan=lan))
    return redirect(url_for('member_page.login', lan=lan))


@staff_page.route('/edit-product/<int:id>/<string:lan>')
def edit_product(id, lan):
    if 'username' in session:
        username = findUser(session['username'])
        ifAdmin = checkAdmin(username)
        if ifAdmin:
            product = findProduct(id)
            return render_template('editProduct.html', product=product, lan=lan)
        else:
            return redirect(url_for('staff_page.warn', lan=lan))
    return redirect(url_for('member_page.login', lan=lan))


@staff_page.route('/modify-product/<int:id>/<string:lan>', methods=['GET', 'POST'])
def modify_product(id, lan):
    if request.method == 'POST':
        productName = request.form.get('productName', None)
        productName2 = request.form.get('productName2', None)
        price = request.form.get('price', None)
        description = request.form.get('description', None)
        description2 = request.form.get('description2', None)
        category = request.form.get('category', None)
        category2 = request.form.get('category2', None)
        img_path = None
        image = request.files.get('image')
        if allowed_file(image.filename):
            img_path = datetime.now().strftime('%Y%m%d%H%M%f') + os.path.splitext(image.filename)[1]
            image.save(os.path.join(upload_path, img_path))
        images = "/static/uploads/" + str(img_path)
        modifyProduct(id, productName, productName2, price, images, description, description2, None, category,
                      category2)
        return redirect(url_for('staff_page.show_product', lan=lan))


@staff_page.route('/show-order/<string:lan>')
def show_order(lan):
    if 'username' in session:
        username = findUser(session['username'])
        ifAdmin = checkAdmin(username)
        if ifAdmin:
            if request.method == 'GET':
                orders = getOrderList()
                return render_template('delOrder.html', lan=lan, orders=orders)
        else:
            return redirect(url_for('staff_page.warn', lan=lan))
    return redirect(url_for('member_page.login', lan=lan))


@staff_page.route('/delete-order/<int:id>/<string:lan>')
def delete_order(id, lan):
    delOrder(id)
    return redirect(url_for('staff_page.show_order', lan=lan))
