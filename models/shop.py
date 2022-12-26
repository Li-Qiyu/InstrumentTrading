from application import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100))
    productName2 = db.Column(db.String(100))
    price = db.Column(db.String(50))
    images = db.Column(db.String(50), default='xxx.png')
    description = db.Column(db.String(2000))
    description2 = db.Column(db.String(2000))
    score = db.Column(db.String(2000))
    category = db.Column(db.String(100))
    category2 = db.Column(db.String(100))
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())

    def __init__(self, productName, productName2, price, images, description, description2, score, category, category2):
        self.productName = productName
        self.productName2 = productName2
        self.price = price
        self.images = images
        self.description = description
        self.description2 = description2
        self.score = score
        self.category = category
        self.category2 = category2

    def __repr__(self):
        return "%s" % self.productName

    def addShop(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String(1500))
    username = db.Column(db.String(100))
    productName = db.Column(db.String(100))
    productName2 = db.Column(db.String(100))
    price = db.Column(db.String(50))
    images = db.Column(db.String(50), default='xxx.png')
    productDescription = db.Column(db.String(2000))
    productNum = db.Column(db.String(50), default='1')

    def __init__(self, pid, username, productName, productName2, price, images, productDescription, productNum):
        self.pid = pid
        self.username = username
        self.productName = productName
        self.productName2 = productName2
        self.price = price
        self.images = images
        self.productDescription = productDescription
        self.productNum = productNum

    def __repr__(self):
        return "%s" % self.id

    def addCart(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    addressName = db.Column(db.String(100))
    userPhone = db.Column(db.String(100))
    country = db.Column(db.String(50))
    town = db.Column(db.String(50))
    detailedAddress = db.Column(db.String(200))
    postCode = db.Column(db.String(50))
    note = db.Column(db.String(200))

    def __init__(self, username, addressName, userPhone, country, town, detailedAddress, postCode, note):
        self.username = username
        self.addressName = addressName
        self.userPhone = userPhone
        self.country = country
        self.town = town
        self.detailedAddress = detailedAddress
        self.postCode = postCode
        self.note = note

    def __repr__(self):
        return "%s" % self.id

    def addAddress(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


class order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String(1500))
    username = db.Column(db.String(100))
    productName = db.Column(db.String(50))
    productName2 = db.Column(db.String(50))
    price = db.Column(db.String(50))
    dispatched = db.Column(db.Integer)
    received = db.Column(db.Integer)
    createTime = db.Column(db.DateTime, server_default=db.FetchedValue())

    def __init__(self, pid, username, productName, productName2, price, dispatched, received):
        self.pid = pid
        self.username = username
        self.productName = productName
        self.productName2 = productName2
        self.price = price
        self.dispatched = dispatched
        self.received = received

    def __repr__(self):
        return "%s" % self.id

    def addOrder(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


class ProductReviews(db.Model):
    __tablename__ = 'product_reviews'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String(1500))
    username = db.Column(db.String(100))
    review = db.Column(db.String(1000))
    score = db.Column(db.Integer)

    def __init__(self, pid, username, review, score):
        self.pid = pid
        self.username = username
        self.review = review
        self.score = score

    def __repr__(self):
        return "%s" % self.id

    def addProductReviews(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 1


def getAllShop():
    Shoplist = Product.query.all()
    return Shoplist


def getAllShopByTime():
    ShopList = Product.query.order_by(Product.createTime.desc()).all()
    return ShopList


def getAllShopByAZ():
    ShopList = Product.query.order_by(Product.productName.asc()).all()
    return ShopList


def getAllShopByAZ2():
    ShopList = Product.query.order_by(Product.productName2.asc()).all()
    return ShopList


def getAllShopByZA():
    ShopList = Product.query.order_by(Product.productName.desc()).all()
    return ShopList


def getAllShopByZA2():
    ShopList = Product.query.order_by(Product.productName2.desc()).all()
    return ShopList


def getAllShopByPriceUp():
    ShopList = Product.query.order_by(Product.price.asc()).all()
    return ShopList


def getAllShopByPriceDown():
    ShopList = Product.query.order_by(Product.price.desc()).all()
    return ShopList


def findProductID(id):
    ID = Product.query.filter_by(id=id).first()
    return ID


def getAllCarts(username):
    Cartlist = db.session.query(Cart).filter_by(username=username).all()
    return Cartlist


def getAllOrder(username):
    orderlist = order.query.filter_by(username=username).all()
    return orderlist


def getAddress(username):
    address = Address.query.filter_by(username=username).first()
    return address


def getOrderList():
    orderList = order.query.all()
    return orderList


def delProduct(id):
    result = Product.query.filter(Product.id == id).first()
    db.session.delete(result)
    db.session.commit()
    return True


def delOrder(id):
    result = order.query.filter(order.id == id).first()
    db.session.delete(result)
    db.session.commit()
    return True


def delCart(id):
    result = Cart.query.filter(Cart.id == id).first()
    db.session.delete(result)
    db.session.commit()
    return True


def isExisted(username, productName):
    isTrue = Cart.query.filter_by(username=username, productName=productName).first()
    if isTrue is None:
        print("0")
        return 0
    else:
        print("1")
        return 1


def submitOrder(username):
    for product in getAllCarts(username):
        print(product.productName)
        o = order(product.pid, username, product.productName, product.productName2, product.price, 0, 0)
        o.addOrder()


# def submitReview(id,username,review,score):
#     review = ProductReviews(id,username,review,score)
#     review.addProductReviews()
#     return True


def isExistedOrder(username, productName):
    isTrue = order.query.filter_by(username=username, productName=productName).first()
    if isTrue is None:
        return 0
    else:
        return isTrue


def getAllProductReviews(id):
    Reviewslist = ProductReviews.query.filter_by(pid=id).all()
    return Reviewslist


def getAllCategories():
    ID = Product.query.filter(Product.category!=None).all()
    categories = {}
    for i in ID:
        if i.category not in categories:
            categories[i.category] = 1
        if i.category in categories:
            categories[i.category] += 1
    return categories


def getAllCategories2():
    ID = Product.query.filter(Product.category2!=None).all()
    categories = {}
    for i in ID:
        if i.category2 not in categories:
            categories[i.category2] = 1
        if i.category2 in categories:
            categories[i.category2] += 1
    return categories



def selectByCategory(category):
    if category == "all":
        selected = getAllShop()
    else:
        selected = Product.query.filter(Product.category==category).all()
    return selected


def findProduct(id):
    product = Product.query.filter_by(id=id).first()
    return product


def findAddress(username):
    address = Address.query.filter_by(username=username).first()
    return address


def modifyProduct(id, productName, productName2, price, images, description, description2, score, category, category2):
    product = Product.query.filter_by(id=id).first()
    product.productName = productName
    product.productName2 = productName2
    product.price = price
    product.images = images
    product.description = description
    product.description2 = description2
    product.score = score
    product.category = category
    product.category2 = category2
    db.session.commit()
    return 1


def modifyAddress(username, addressName, phone, country, town, detailedAddress, postCode):
    address = Address.query.filter_by(username=username).first()
    address.username = username
    address.addressName = addressName
    address.phone = phone
    address.country = country
    address.town = town
    address.detailedAddress = detailedAddress
    address.postCode = postCode
    db.session.commit()
    return 1


def searchProduct(search_value):
    s = Product.query.filter(Product.productName.like("%" + search_value + "%") if search_value is not None else "").all()
    return s


def searchProduct2(search_value):
    s = Product.query.filter(Product.productName2.like("%" + search_value + "%") if search_value is not None else "").all()
    return s
