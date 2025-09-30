# Bread Van App

A Flask application for managing bread van schedules and resident stop requests.

## Project Overview
The Bread Van App allows drivers to schedule drives to specific streets and enables residents to view scheduled drives, request stops, and track driver status and location.

## CLI Commands Documentation
Driver Commands
flask driver create "John Driver" - Creates a new driver with the specified name.
flask driver list - Lists all drivers in the system with their current status.
flask driver schedule <driver_id> <street_id> "YYYY-MM-DD HH:MM:SS" - Schedules a drive for a driver to a specific street at the given time.
flask driver status <driver_id> <status> - Updates a driver's status (e.g., "available", "on_route", "offline")
flask driver location <driver_id> <location> - Updates a driver's current location.

Resident Commands
flask resident create "Alice Smith" <street_id> - Creates a new resident with the specified name on the given street.
flask resident list - Lists all residents and the streets they live on.
flask resident inbox <resident_id> - Shows all scheduled drives for the resident's street.
flask resident request <resident_id> <drive_id> - Creates a stop request for a resident on a specific drive.
flask resident driver-status <driver_id> - Shows a driver's current status and location.

Street Commands
flask street create "Main Street" - Creates a new street.
flask street list - Lists all streets in the system.


### Database Initialization
```bash
flask init


Example Usage Workflow

Initialize the database:

flask init
Schedule a drive:

flask driver schedule 1 1 "2024-01-20 14:30:00"
Resident checks their inbox:

flask resident inbox 1
Resident requests a stop:

flask resident request 1 1
Driver updates status:

flask driver status 1 "on_route"
flask driver location 1 "Heading to Main Street"
Resident checks driver status:

flask resident driver-status 1

Models:
Driver - Manages driver information and status
Street - Represents streets where drives are scheduled
Resident - Represents residents living on streets
Drive - Represents scheduled drives by drivers
Request - Represents stop requests from residents
