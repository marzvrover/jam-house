from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(os.path.dirname(os.path.abspath(__file__)) + '/..') / '.env'

env_path = str(env_path.resolve())

load_dotenv(dotenv_path=env_path)
