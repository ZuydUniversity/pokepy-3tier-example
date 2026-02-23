import configparser
import os

from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment

def read_config():
    config = configparser.ConfigParser()

    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, '..', 'config.ini')
    config.read(config_path)

    try:
        debug_mode = config.getboolean('General', 'debug')
        print(debug_mode)
        log_level = config.get('General', 'log_level')
        
        # Read database configuration from environment variables
        db_name = os.getenv('DB_NAME')
        db_host = os.getenv('DB_HOST')
        db_port = int(os.getenv('DB_PORT'))
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')

        config_values = {
            'debug_mode': debug_mode,
            'log_level': log_level,
            'db_name': db_name,
            'db_host': db_host,
            'db_port': db_port,
            'db_user': db_user,
            'db_password': db_password
        }
        return config_values

    except configparser.NoSectionError as e:
        print(f"Configuration error: {e}")
    except configparser.NoOptionError as e:
        print(f"Configuration error: {e}")

    return {}
