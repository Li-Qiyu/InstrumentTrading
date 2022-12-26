from flask import Blueprint, render_template, session, request, redirect, url_for
import math
from controllers.shop import Prices
from models.shop import getAllCarts, isExisted
from models.blog import *
from models.user import getNickname

blog_page = Blueprint("blog_page", __name__)


@blog_page.route("/blog_grid/<string:lan>/<int:page>", methods=['POST', 'GET'])
def blog_grid(lan, page):
    if request.method == 'GET':
        allBlog = getAllBlogByTime()
        allNum = len(allBlog)
        pageNum = math.ceil(allNum / 6)
        if 'username' in session:
            carts = getAllCarts(session['username'])
            return render_template("blog-grid.html", carts=carts, blog=allBlog, allNum=allNum, pageNum=pageNum,
                                   page=page, lan=lan)
        return render_template("blog-grid.html", blog=allBlog, allNum=allNum, lan=lan,
                               pageNum=pageNum, page=page)

    if request.method == 'POST':
        allBlog = getAllBlogByTime()
        allNum = len(allBlog)
        pageNum = math.ceil(allNum / 6)
        if 'username' in session:
            carts = getAllCarts(session['username'])
            return render_template("blog-grid.html", carts=carts, blog=allBlog,
                                   allNum=allNum, pageNum=pageNum, page=page, lan=lan)
        return render_template("blog-grid.html", blog=allBlog, allNum=allNum, lan=lan,
                               pageNum=pageNum, page=page)


@blog_page.route("/single_blog/<int:id>/<string:lan>", methods=['GET', 'POST'])
def single_blog(id, lan):
    ID = findBlogID(id)
    blogs = getAllBlogByTime()
    ID1 = findBlogID(1)
    ID_0 = findBlogID(id - 1)
    ID_1 = findBlogID(id + 1)
    blogNum = len(blogs)
    ID_E = findBlogID(blogNum)
    reviews = getAllBlogReviews(id)
    if request.method == "GET":
        if 'username' in session:
            username = session['username']
            carts = getAllCarts(username)
            isTrue = isExisted(username, ID.title)
            return render_template('single-blog.html', carts=carts, ID=ID, id=id - 1, totalPrices=Prices(carts),
                                   blogs=blogs[0:6], isTrue=isTrue, reviews=reviews, reviewNum=len(reviews), lan=lan,
                                   ID1=ID1, blogNum=blogNum, ID_0=ID_0, ID_1=ID_1, ID_E=ID_E)
        return render_template('single-blog.html', ID=ID, blogs=blogs[0:4], reviews=reviews, reviewNum=len(reviews),
                               lan=lan, ID1=ID1, blogNum=blogNum, ID_0=ID_0, ID_1=ID_1, ID_E=ID_E)

    if request.method == 'POST':
        if 'username' in session:
            blogReviews = request.form.get('blogReviews')
            reviews = BlogReviews(id, session['username'], blogReviews)
            reviews.addReviews()
            return redirect(url_for('shop_page.single_blog', id=id))
        return render_template('single-blog.html', ID=ID, blogs=blogs[0:4], reviews=reviews, reviewNum=len(reviews),
                               lan=lan, ID1=ID1, blogNum=blogNum, ID_0=ID_0, ID_1=ID_1, ID_E=ID_E)


@blog_page.route("/review/<int:id>/<string:lan>",methods=['GET','POST'])
def review(id,lan):
    ID = findBlogID(id)
    blogs = getAllBlogByTime()
    reviews = getAllBlogReviews(id)
    if request.method == 'POST':
        if 'username' in session:
            blogReviews = request.form.get('review', None)
            reviews = BlogReviews(id, session['username'], blogReviews)
            reviews.addBlogReviews()
            return redirect(url_for('blog_page.single_blog', id=id, lan=lan))
        return render_template('single-blog.html', ID=ID, blogs=blogs[0:4], reviews=reviews,
                               reviewNum=len(reviews), lan=lan)
    if request.method == "GET":
        if 'username' in session:
            username = session['username']
            carts = getAllCarts(username)
            return render_template('newBlogReview.html', ID=ID, lan=lan)
        return render_template('single-blog.html', ID=ID, id=id - 1, blogs=blogs[0:4], reviews=reviews,
                               reviewNum=len(reviews), lan=lan)