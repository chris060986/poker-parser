import os


def env_variable(key, default=None):
    val = os.environ.get(key, default)

    if val == 'True':
        val = True

    elif val == 'False':
        val = False

    return val


# Class to have a default config that can be overwritten by env variables
class PokerParserConfig:

    DEBUG = env_variable("DEBUG", default=False)
    DATABASE_URL = env_variable('DATABASE_URL', default="my-poker-couch")
    DATABASE_PORT = env_variable('DATABASE_PORT', default=5984)