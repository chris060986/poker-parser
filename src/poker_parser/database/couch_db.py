import couchdb


class CouchDBAccess:
    # externalize config
    user = 'admin'
    password = 'admin'

    def __init__(self, config):
        self.config = config
        self.couch_db_server = couchdb.Server("http://%s:%s@%s:%s/" % (self.user, self.password, self.config["DATABASE_URL"], self.config["DATABASE_PORT"]))

    def get_db(self, hero):
        # non-performant?
        if hero in self.couch_db_server:
            return self.couch_db_server[hero]
        else:
            return self.couch_db_server.create(hero)

    def save_poker_hand(self, hero, hand_history_doc):
        """Creates and updates the poker hand. If the hand is not available in the database it will be created.
           If available it will be overwritten. NO MERGE!


            Parameters
            ----------
            hero : str
                The name of the pokerhero used as db name
            hand_history_doc : doc
                The json document of the poker hand

            Returns
            -------
            (id, rev)
                tuple of id and rev of the saved document
            """
        _id = str(hand_history_doc['id'])
        db = self.get_db(hero)
        hand_history_doc['_id'] = _id
        row = db.get(_id)
        print(_id)
        if row is not None:
            print(row['_rev'])
            hand_history_doc['_rev'] = row['_rev']
        return db.save(hand_history_doc)
