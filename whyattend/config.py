"""
    Application Configuration
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    This file should be used as a template and overview
    of all available options. Put your local deployment
    settings into local_config.py, which overrides these
    defaults. (see bottom of file)
"""

import datetime

# Database URI (see http://docs.sqlalchemy.org/en/latest/core/engines.html#supported-databases)
DATABASE_URI = 'sqlite:///../tmp/test.db'

# Path to temporary folder for OpenID authentication files
OID_STORE_PATH = 'tmp/oid'

# generate one via e.g. "import os; os.urandom(24)". The key is used to sign the session cookies.
SECRET_KEY = ''

CLAN_NAMES = ('CLAN', 'STRONK')
CLAN_IDS = {
    'CLAN': '23456789',
    'STRONK': '34567890'
}

# Temporary folder for uploaded replays
UPLOAD_FOLDER = 'tmp/uploads'

# Wargaming.net API token and base URL
API_URL = 'http://api.worldoftanks.eu/'
API_TOKEN = 'd0a293dc77667c9328783d489c8cef73'

# WoT Server region code
WOT_SERVER_REGION_CODE = 'eu'

# Key for attendance tracker API functions
API_KEY = 'testkey'

# Map WoT API clan roles to displayed name
ROLE_LABELS = {
    'leader': 'Commander',
    'vice_leader': 'Deputy Commander',
    'commander': 'Field Commander',
    'recruiter': 'Recruiter',
    'private': 'Soldier',
    'recruit': 'Recruit',
    'treasurer': 'Treasurer'
}

# List of player names that can do everything
ADMINS = ('fantastico', )

CREATE_BATTLE_ROLES = ('leader', 'vice_leader', 'treasurer')
DELETE_BATTLE_ROLES = ('leader', 'vice_leader', 'treasurer')
PAYOUT_ROLES = ('leader', 'vice_leader', 'treasurer')
ADMIN_ROLES = ('leader', 'vice_leader', 'commander', 'treasurer')
PLAYER_PERFORMANCE_ROLES = ('leader', 'vice_leader')

# How long after the battle date should reserves be able to sign in themselves
RESERVE_SIGNUP_DURATION = datetime.timedelta(days=7)
# Allow/disallow signup by players. If disallowed, only members with a position in CREATE_BATTLE_ROLES can do it
RESERVE_SIGNUP_ALLOWED = False

# Should replays be stored in the database?
STORE_REPLAYS_IN_DB = True

# Logfile
ERROR_LOG_FILE = '/tmp/error.log'
LOG_FILE = '/tmp/whyattend.log'

# Celery task queue settings
# See http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

# Override settings with local config, if present.
try:
    from local_config import *
except ImportError:
    pass
