import couchdb


class CouchDBAccess:

    # externalize config
    url = 'my-poker-couch:5984'
    user = 'admin'
    password = 'admin'

    def __init__(self):
        self.couch_db_server = couchdb.Server("http://%s:%s@%s/" % (self.user, self.password, self.url))

    def get_db(self, hero):
        # non-performant?
        if hero in self.couch_db_server:
            return self.couch_db_server[hero]
        else:
            return self.couch_db_server.create(hero)

    def save_poker_hand(self, hero, hand_history_doc):
        db = self.get_db(hero)
        db.save(hand_history_doc)
