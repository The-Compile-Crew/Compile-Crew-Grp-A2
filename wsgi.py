import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))


    

app.cli.add_command(test)

# Driver commands
driver_cli = AppGroup('driver', help='Driver operations')

@driver_cli.command("create", help="Create a driver")
@click.argument("name")
def create_driver_command(name):
    create_driver(name)
    print(f'Driver {name} created!')

@driver_cli.command("list", help="List all drivers")
def list_drivers_command():
    drivers = get_all_drivers()
    for driver in drivers:
        print(f"{driver.driverId}: {driver.name} - Status: {driver.status}")

@driver_cli.command("schedule", help="Schedule a drive")
@click.argument("driver_id", type=int)
@click.argument("street_id", type=int) 
@click.argument("scheduled_time")
def schedule_drive_command(driver_id, street_id, scheduled_time):
    from datetime import datetime
    scheduled_time = datetime.fromisoformat(scheduled_time)
    drive = schedule_drive(driver_id, street_id, scheduled_time)
    print(f'Drive scheduled: {drive}')

@driver_cli.command("status", help="Update driver status")
@click.argument("driver_id", type=int)
@click.argument("status")
def update_driver_status_command(driver_id, status):
    driver = update_driver_status(driver_id, status)
    print(f'Driver {driver.name} status updated to: {status}')

@driver_cli.command("location", help="Update driver location")
@click.argument("driver_id", type=int)
@click.argument("location")
def update_driver_location_command(driver_id, location):
    driver = update_driver_location(driver_id, location)
    print(f'Driver {driver.name} location updated to: {location}')

@driver_cli.command("requests", help="View requests for driver's drives")
@click.argument("driver_id", type=int)
def view_driver_requests_command(driver_id):
    requests = get_requests_by_driver(driver_id)
    print(f"Requests for driver {driver_id}:")
    for req in requests:
        print(f"Request {req.requestId}: Resident {req.resident.name} - Status: {req.status}")

app.cli.add_command(driver_cli)

# Resident commands
resident_cli = AppGroup('resident', help='Resident operations')

@resident_cli.command("create", help="Create a resident")
@click.argument("name")
@click.argument("street_id", type=int)
def create_resident_command(name, street_id):
    create_resident(name, street_id)
    print(f'Resident {name} created!')

@resident_cli.command("list", help="List all residents")
def list_residents_command():
    residents = get_all_residents()
    for resident in residents:
        print(f"{resident.residentId}: {resident.name} - Street: {resident.street.name}")

@resident_cli.command("inbox", help="View scheduled drives for resident's street")
@click.argument("resident_id", type=int)
def view_inbox_command(resident_id):
    resident = get_resident(resident_id)
    if resident:
        drives = get_drives_by_street(resident.streetId)
        print(f"Scheduled drives for {resident.name}'s street:")
        for drive in drives:
            print(f"  Drive {drive.driveId}: {drive.driver.name} at {drive.scheduledTime}")
    else:
        print("Resident not found")

@resident_cli.command("request", help="Request a stop")
@click.argument("resident_id", type=int)
@click.argument("drive_id", type=int)
def request_stop_command(resident_id, drive_id):
    request = create_request(resident_id, drive_id)
    print(f'Stop request created: {request}')

@resident_cli.command("driver-status", help="View driver status")
@click.argument("driver_id", type=int)
def view_driver_status_command(driver_id):
    driver = get_driver(driver_id)
    if driver:
        print(f"Driver {driver.name}: Status={driver.status}, Location={driver.location}")
    else:
        print("Driver not found")

app.cli.add_command(resident_cli)

# Street commands
street_cli = AppGroup('street', help='Street operations')

@street_cli.command("create", help="Create a street")
@click.argument("name")
def create_street_command(name):
    create_street(name)
    print(f'Street {name} created!')

@street_cli.command("list", help="List all streets")
def list_streets_command():
    streets = get_all_streets()
    for street in streets:
        print(f"{street.streetId}: {street.name}")

app.cli.add_command(street_cli)
