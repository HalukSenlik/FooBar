from google.cloud import firestore  # pylint: disable=import-error
import os

def get_firestore_db_client():
    """
    returns a firestore database client pointed
    at the correct host
    """
    print(os.getenv("FIRESTORE_EMULATOR_HOST"))
    return firestore.Client()