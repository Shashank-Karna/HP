from hp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    tests = db.relationship("Test", backref="user", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    cp = db.Column(db.Integer)
    trest_bps = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.Integer)
    rest_ecg = db.Column(db.Integer)
    thalach = db.Column(db.Integer)
    exang = db.Column(db.Integer)
    old_peak = db.Column(db.Integer)
    slope = db.Column(db.Integer)
    ca = db.Column(db.Integer)
    thal = db.Column(db.Integer)
    target = db.Column(db.Integer)

    def __repr__(self):
        return f"Test('{self.target}')"
