import os


def get_env(option):

    def log_level():
        return (os.getenv('LOG_LEVEL', 'INFO')).upper()

    options = {
        'LOG_LEVEL': log_level,
    }

    return options[option]()
