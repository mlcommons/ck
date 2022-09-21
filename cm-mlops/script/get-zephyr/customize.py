from cmind import utils
import os

def preprocess(i):

    return {'return':0}


def postprocess(i):

    env = i['env']
    env['ZEPHYR_TOOLCHAIN_VARIANT'] = "zephyr"
    env['ZEPHYR_SDK_INSTALL_DIR'] = os.path.join(os.getcwd(), "zephyr")

    return {'return':0}
