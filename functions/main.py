from example_library.utils import basic_foo
from firebase_functions import https_fn  # pylint: disable=import-error
from firebase_admin import initialize_app  # pylint: disable=import-error


# Initialize Firebase Admin
initialize_app()


# First endpoint
@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    """
    This is a basic example of something that works
    :param req: a https_fun request
    :return: Response
    """
    if req:
        pass
    return https_fn.Response(basic_foo())