"""Define MyGHub Enviroment variables"""

import os
import dotenv


def use_env():
    """Load ENV from .env file"""

    dotenv.load_dotenv()


use_env()

GH_TOKEN = os.getenv('GH_TOKEN', None)
