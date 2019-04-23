######################################################################
# Drop the following keys in local_settings.py
#
# API_KEY="Your Airtable API Key"
# BASE_KEY="Base Key for Coworking Help Airtable"
# TABLE_NAME="Table Name for Airtable"
# VIEW_NAME="View Name for Airtable"
######################################################################

import yaml
from airtable import Airtable
import local_settings as settings


DATA_FILE = "../consultants.yml"

airtable = Airtable(settings.BASE_KEY, settings.TABLE_NAME, api_key=settings.API_KEY)


def dump_all_data():
    data = airtable.get_all(view=settings.VIEW_NAME)
    with open(DATA_FILE, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)
