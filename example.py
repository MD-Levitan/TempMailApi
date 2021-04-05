from tempmail_api.api import *

email = "patricia_cherry_1999@my6com.com"

s = create_session(proxy={
    "https": "127.0.0.1:8080",
    "http": "127.0.0.1:808"
},
                   verify=False)

r = PremiumAPI.user_login(username="user@email.com",
                          password="some",
                          provider="paddle",
                          session=s)

sid = r.result.sid
email = "evelyn_day_1985asdadasdasdasd@oazv.net"
r = PremiumAPI.new_mailbox(sid=sid, email=email, domain="oazv.net", session=s)
r = PremiumAPI.mailbox_messages(sid=sid, email=email, session=s).result.mails
