from google.cloud import firestore  # pylint: disable=import-error


def get_firestore_db_client():
    """
    returns a firestore database client pointed
    at the correct host
    """
    return firestore.Client()