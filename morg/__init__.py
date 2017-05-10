import os
import time

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.normpath(os.path.join(SRC_DIR, ".."))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
LOG_FILE_PATH = os.path.join(
    ROOT_DIR, 'logs', 'morg_{}.log'.format(time.strftime("%Y_%m_%d")),
)


def run():

    from morg.main import MyOrganiser
    MyOrganiser().run()
