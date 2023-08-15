import harperdb

from secret import HARPERDB_URL, HARPERDB_PASSWORD, HARPERDB_USERNAME



db = harperdb.HarperDB(
    url=HARPERDB_URL,
    username=HARPERDB_USERNAME,
    password=HARPERDB_PASSWORD
)