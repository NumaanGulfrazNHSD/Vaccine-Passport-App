from mimetypes import init
from app import __init__

def test_init():
    assert init() == 'config'
