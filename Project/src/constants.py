import os

dir = os.path.dirname(__file__)

PRIV_DIR = dir + os.sep + '..' + os.sep + 'priv' + os.sep

try:
    os.makedirs(PRIV_DIR, exist_ok=True)
except:
    pass

PAGES_DIRECTORY = 'pages'