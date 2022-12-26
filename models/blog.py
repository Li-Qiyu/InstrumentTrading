from application import db


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    username = db.Column(db.String(20))
    titleImage = db.Column(db.String(100))
    content = db.Column(db.String(4000))
    date = db.Column(db.DateTime, server_default=db.FetchedValue())
    tag1 = db.Column(db.String(100))
    tag2 = db.Column(db.String(100))
    tag3 = db.Column(db.String(100))

    def __init__(self, title, username, titleImage, content, date, tag1, tag2, tag3):
        self.title = title
        self.username = username
        self.titleImage = titleImage
        self.content = content
        self.date = date
        self.tag1 = tag1
        self.tag2 = tag2
        self.tag3 = tag3

    def __repr__(self):
        return "%s" % self.username

    def addBlog(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


class BlogReviews(db.Model):
    __tablename__ = 'blog_reviews'
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer)
    username = db.Column(db.String(100))
    review = db.Column(db.String(1000))
    date = db.Column(db.DateTime, server_default=db.FetchedValue())

    def __init__(self, bid, username, review):
        self.bid = bid
        self.username = username
        self.review = review

    def __repr__(self):
        return "%s" % self.username

    def addBlogReviews(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


def getAllBlog():
    Bloglist = Blog.query.all()
    return Bloglist


def getAllBlogByTime():
    BlogList = Blog.query.order_by(Blog.date).all()
    return BlogList


def findBlogID(id):
    ID = Blog.query.filter_by(id=id).first()
    return ID


def getAllCategories():
    ID = Blog.query.filter(Blog.category != None).all()
    categories = {}
    for i in ID:
        if i.category not in categories:
            categories[i.category] = 1
        if i.category in categories:
            categories[i.category] += 1
    return categories


def selectByCategory(category):
    if category == "all":
        selected = getAllBlog()
    else:
        selected = Blog.query.filter(Blog.category == category).all()
    return selected


def getAllBlogReviews(id):
    Reviewslist = BlogReviews.query.filter_by(bid=id).all()
    return Reviewslist


def findBlog(id):
    blog = Blog.query.filter_by(id=id).first()
    return blog


def modifyBlog(id, title, username, titleImage, content, category, date):
    blog = Blog.query.filter_by(id=id).first()
    blog.title = title
    blog.username = username
    blog.titleImage = titleImage
    blog.content = content
    blog.category = category
    blog.date = date
    db.session.commit()
    return 1


def searchBlog(search_value):
    s = Blog.query.filter(Blog.title.like("%" + search_value + "%") if search_value is not None else "").all()
    return s
