from pathlib import Path
from dotenv import load_dotenv

env_path = Path('..') / '.env'

env_path = str(env_path.resolve())

load_dotenv(dotenv_path=env_path)
