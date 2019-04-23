from pprint import pprint

from api import airtable

pages = airtable.get_iter()
for page in pages:
    for record in page:
        pprint(record)
