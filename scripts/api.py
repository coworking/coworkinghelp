######################################################################
# Drop the following keys in local_settings.py
#
# API_KEY="Your Airtable API Key"
# BASE_KEY="Base Key for Coworking Help Airtable"
# TABLE_NAME="Table Name for Airtable"
# VIEW_NAME="View Name for Airtable"
######################################################################

from airtable import Airtable

import local_settings as settings


airtable = Airtable(settings.BASE_KEY, settings.TABLE_NAME, api_key=settings.API_KEY)
# print(airtable.get_all(view=settings.VIEW_NAME, maxRecords=20))
