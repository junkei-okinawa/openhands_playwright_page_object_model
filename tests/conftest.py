import sys
import os
import pytest

def pytest_sessionstart(session):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))