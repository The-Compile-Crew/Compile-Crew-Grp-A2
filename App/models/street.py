from App.database import db

class Street(db.Model):
    streetId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    drives = db.relationship('Drive', backref='street', lazy=True)
    residents = db.relationship('Resident', backref='street', lazy=True)
    
    def __init__(self, name):
        self.name = name
    
    def toJSON(self):
        return {
            'streetId': self.streetId,
            'name': self.name
        }