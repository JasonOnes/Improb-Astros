import omdb
from hidden import om_key

API_KEY = om_key
omdb.set_default('apikey', API_KEY)

print(omdb.get(title="Happy Gilmore", fullplot=True))
