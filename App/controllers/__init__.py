# JWT decorators
from flask_jwt_extended import jwt_required, get_jwt_identity

# Module-wide imports
from .user_controller import *
from .auth import *

# Controller modules
from .user_controller import (
    create_user,
    get_user,
    get_user_by_username,
    get_all_users,
    get_all_users_json,
    update_user
)

from .auth import (
    login,
    setup_jwt,
    add_auth_context
)

# ...rest unchanged

from .driver_controller import (
    create_driver,
    update_driver_status,
    update_driver_location,
    get_driver,
    get_driver_location,
    schedule_drive,  # or schedule_driver if renamed
    get_requests_by_driver,
    get_drives_by_driver
)

from .resident_controller import (
    create_resident,
    get_resident
)

from .street_controller import (
    create_street,
    get_drives_by_street
)

from .request_controller import (
    create_request,
    update_request_status
)

# Models and DB
from App.models import User, Driver, Street, Resident, Drive, Request
from App.database import db