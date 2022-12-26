from application import db

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(100))
    price = db.Column(db.String(50))
    images = db.Column(db.String(50),default='xxx.png')
    description = db.Column(db.String(2000))
    score = db.Column(db.String(2000))

    def __init__(self,name,price,images,description,score):
        self.productName = productName
        self.price = price
        self.images = images
        self.description = description
        self.score = score

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


class Cart(db.model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer,primary_key=True)
    pid = db.Column(db.String(1500))
    username = db.Column(db.String(100))
    productName = db.Column(db.String(100))
    price = db.Column(db.String(50))
    images = db.Column(db.String(50),default='xxx.png')
    productDescription = db.Column(db.String(2000))
    productNum = db.Column(db.String(50),default='1')

    def __init__(self,pid,username,productName,price,images,productDescription,productNum):
        self.pid=pid
        self.username=username
        self.productName=productName
        self.price=price
        self.images=images
        self.productDescription=productDescription
        self.productNum=productNum

    def __repr__(self):
        return "%s" % self.productName
    
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


class address(db.Model):
    __tablename__ = 'useraddress'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    addressName = db.Column(db.String(100))
    userPhone = db.Column(db.String(100))
    town = db.Column(db.String(50))
    detailedAddress = db.Column(db.String(200))
    postCode = db.Column(db.String(50))
    note = db.Column(db.String(200))\

    def __init__(self,username,addressName,userPhone,town,detailedAddress,postCode,note):
        self.username=username
        self.addressName=addressName
        self.userPhone=userPhone
        self.town=town
        self.detailedAddress=detailedAddress
        self.postCode=postCode
        self.note=note

    def __repr__(self):
        return "%s" % self.productName

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
    id = db.Column(db.Integer,primary_key=True)
    pid = db.Column(db.String(1500))
    userName = db.Column(db.String(100))
    productName = db.Column(db.String(50))
    price = db.Column(db.String(50))
    status = db.Column(db.String(20),default='not dispatched')

    def __init__(self,pid,username,productName,price,status):
        self.pid=pid
        self.username=username
        self.productName=productName
        self.price=price
        self.status=status

    def __repr__(self):
        return "%s" % self.productName

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


class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key=True)
    pid = db.Column(db.String(1500))
    username = db.Column(db.String(100))
    review = db.Column(db.String(1000))

    def __init__(self, pid, username, review):
        self.pid = pid
        self.username = username
        self.review = review

    def __repr__(self):
        return "%s" % self.productName

    def addReviews(self):
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
    Shoplist = storeManagement.query.all()
    return Shoplist


def findID(id):
    ID = storeManagement.query.filter_by(id=id).first()
    return ID


def getAllCarts(username):
    Cartlist = Cart.query.filter_by(username=username).all()
    return Cartlist


def getAllOrder(username):
    orderlist = order.query.filter_by(username=username).all()
    return orderlist


def delCart(id):
    result = Cart.query.filter(Cart.id==id).first()
    db.session.delete(result)
    db.session.commit()
    return True


def submitOrder(orderNum,username):
    for Product in getAllCarts(username):
        print(product.productName)
        o = order(product.pid, username, product.productName, product.price, None)
        o.addOrder()


def isExistedOrder(username,productName):
    isTrue = order.query.filter_by(username=username,productName=productName).first()
    if isTrue is None:
        return 0
    else:
        return isTrue


def getAllReviews(id):
    Reviewslist = Reviews.query.filter_by(pid=id).all()
    return Reviewslist


def delReview(id):
    review = Reviews.query.filter(Reviews.id==id).first()
    if review is None:
        pass
    db.session.delete(reivew)
    db.session.commit()
    print("ok")
    return 1


def findProduct(id):
    Product = storeManagement.query.filter_by(id=id),first()
    return Product


def modifyProduct(id,productName,price,images,description,score):
    Product = storeManagement.query.filter_by(id=id).first()
    Product.productName = productName
    Product.price = price
    Product.description = description
    Product.score = score
    db.session.commit()
    return 1


def search(search_value):
    s = storeManagement.query.filter(storeManagement.productName.endswith(search_value)).all()
    return s


db.create_all()

