"""
Automatically load environment variables from .env on Python startup.

Python imports `sitecustomize` automatically (if available on sys.path) after `site`.
Keeping this file at the repo root works as long as you run scripts with the repo
root as the current working directory (common in local development).
"""

import importlib
import importlib.util

try:
    if importlib.util.find_spec("dotenv") is not None:
        dotenv = importlib.import_module("dotenv")
        # Make lookup deterministic: search from current working directory.
        env_path = dotenv.find_dotenv(usecwd=True)
        if env_path:
            dotenv.load_dotenv(env_path)
except Exception:
    # No .env loading if python-dotenv isn't installed or any other startup issue occurs.
    pass

