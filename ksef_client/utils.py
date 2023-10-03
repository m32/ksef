from .consts import ACCEPT, JSON


def get_header(content_type = JSON, token=None):
    
    header = {
        'Accept': ACCEPT,
        'content-type': content_type,
    }
    
    if token:
        header['SessionToken'] = token
    
    return header