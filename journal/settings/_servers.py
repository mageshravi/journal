import socket

LIVE_HOST = 'e2e-11-38.e2enetworks.net.in'


def get_server_type():
    hostname = socket.gethostname()

    if hostname == LIVE_HOST:
        return "prod"
    else:
        return "dev"
    # end if
