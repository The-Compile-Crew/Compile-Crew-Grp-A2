from App.database import db

class Request(db.Model):
    requestId = db.Column(db.Integer, primary_key=True)
    residentId = db.Column(db.Integer, db.ForeignKey('resident.residentId'), nullable=False)
    driveId = db.Column(db.Integer, db.ForeignKey('drive.driveId'), nullable=False)
    status = db.Column(db.String(50), default="pending")
    description = db.Column(db.String(255))  # Optional field for request details

    def __init__(self, residentId, driveId, status="pending", description=None):
        self.residentId = residentId
        self.driveId = driveId
        self.status = status
        self.description = description

    def toJSON(self):
        return {
            'requestId': self.requestId,
            'residentId': self.residentId,
            'driveId': self.driveId,
            'status': self.status,
            'description': self.description
        }