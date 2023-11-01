import sys

def is_local_enviroment():
    return sys.argv[0].endswith("__main__.py")
