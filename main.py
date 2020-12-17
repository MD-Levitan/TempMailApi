from api.api import *

email = "tony_smith_@nyobase.com"

API.SESSION = create_seesion(proxy={
    "https": "127.0.0.1:8081", "http": "127.0.0.1:8081"
},
                             verify=False)
r = API.get_messages(email)
r = API.get_domains()
print(r)
