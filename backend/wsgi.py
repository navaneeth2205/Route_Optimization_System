"""WSGI entry point for deployments that set `backend` as the root directory."""

import os
import sys


ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.app import create_app


app = create_app()