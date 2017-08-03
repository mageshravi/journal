"""Settings for multiple environments
"""
from ._servers import get_server_type

server_type = get_server_type()

try:
    exec("from .%s import *" % server_type)
except ImportError as error:
    print("%s settings not found" % server_type)
    raise error
# end except
