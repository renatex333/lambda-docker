import sys

def hello_from_docker(event, context):
    """
    Handler function for docker test
    """
    return {
        "created_by": "Renatex",
        "message": "Hello World!",
        "version": sys.version
    }
