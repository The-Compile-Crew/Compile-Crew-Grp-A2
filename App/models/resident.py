from App.database import db
from App.models.user import User

class Resident(User):
    __tablename__ = 'resident'
    residentId = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    streetId = db.Column(db.Integer, db.ForeignKey('street.streetId'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    requests = db.relationship('Request', backref='resident', lazy=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'resident',
    }

    def __init__(self, username, password, name, streetId):
        super().__init__(username, password)
        self.name = name
        self.streetId = streetId
    
    def get_json(self):
        return {
            'residentId': self.residentId,
            'streetId': self.streetId,
            'name': self.name
        }