from App.database import db
from App.models.user import User

class Driver(User):
    __tablename__ = 'driver'
    driverId = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    driverName = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="available")
    location = db.Column(db.String(100), nullable=False)
    
    drives = db.relationship('Drive', backref='driver', lazy=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'driver',
    }

    def __init__(self, username, driverName, password, location, status="available"):
        super().__init__(username, password)
        self.driverName = driverName
        self.location = location
        self.status = status
    
    def get_json(self):
        return {
            'driverId': self.driverId,
            'driverName': self.driverName,
            'status': self.status,
            'location': self.location
        }

    # Backwards-compatible alias some code/tests expect
    def toJSON(self):
        return self.get_json()