from App.database import db

class Driver(db.Model):
    driverId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="available")
    location = db.Column(db.String(100))
    
    drives = db.relationship('Drive', backref='driver', lazy=True)
    
    def __init__(self, name, status="available", location=None):
        self.name = name
        self.status = status
        self.location = location

    
    def toJSON(self):
        return {
            'driverId': self.driverId,
            'name': self.name,
            'status': self.status,
            'location': self.location
        }