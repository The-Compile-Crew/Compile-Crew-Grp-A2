from App.database import db

class Resident(db.Model):
    residentId = db.Column(db.Integer, primary_key=True)
    streetId = db.Column(db.Integer, db.ForeignKey('street.streetId'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    requests = db.relationship('Request', backref='resident', lazy=True)
    
    def __init__(self, name, streetId):
        self.name = name
        self.streetId = streetId
    
    def toJSON(self):
        return {
            'residentId': self.residentId,
            'streetId': self.streetId,
            'name': self.name
        }