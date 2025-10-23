from App.models import Street
from App.database import db

def create_street(name):
  street = Street(name)
  db.session.add(street)
  db.session.commit()
  return street

def get_all_streets():
  return Street.query.all()
