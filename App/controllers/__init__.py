from flask_jwt_extended import jwt_required, get_jwt_identity
from .user import *
from .driver_controller import *
from .resident_controller import *
from .street_controller import *
from .request_controller import *

from App.models import User, Driver, Street, Resident, Drive, Request
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    
    # Create sample data
    main_st = Street("Main Street")
    oak_st = Street("Oak Avenue")
    db.session.add(main_st)
    db.session.add(oak_st)
    
    # Add drivers
    driver1 = Driver("John Driver")
    driver2 = Driver("Sarah Driver") 
    db.session.add(driver1)
    db.session.add(driver2)
    
    # Add residents
    resident1 = Resident("Alice Smith", 1)
    resident2 = Resident("Bob Johnson", 1)
    resident3 = Resident("Carol Williams", 2)
    db.session.add(resident1)
    db.session.add(resident2)
    db.session.add(resident3)
    
    db.session.commit()
    print("Database initialized with sample data!")
