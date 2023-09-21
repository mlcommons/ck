import os

def postprocess(i):

    env = i['env']

    env['CM_SQLITE_PATH'] = os.getcwd()

    return {'return':0}
