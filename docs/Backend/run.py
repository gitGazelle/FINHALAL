import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(abspath(__file__)))
from app import create_app

app = create_app()
