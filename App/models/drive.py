from App.database import db
from datetime import datetime

class Drive(db.Model):
    driveId = db.Column(db.Integer, primary_key=True)
    driverId = db.Column(db.Integer, db.ForeignKey('driver.driverId'), nullable=False)
    streetId = db.Column(db.Integer, db.ForeignKey('street.streetId'), nullable=False)
    scheduledTime = db.Column(db.DateTime, nullable=False)
    
    requests = db.relationship('Request', backref='drive', lazy=True)
    
    def __init__(self, driverId, streetId, scheduledTime):
        self.driverId = driverId
        self.streetId = streetId
        self.scheduledTime = scheduledTime
    
    def get_json(self):
        return {
            'driveId': self.driveId,
            'driverId': self.driverId,
            'streetId': self.streetId,
            'scheduledTime': self.scheduledTime.isoformat()
        }

    # Backwards-compatible alias expected by some tests
    def toJSON(self):
        return self.get_json()