import os

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / "envs/.env.dev"
load_dotenv(dotenv_path=env_path)
