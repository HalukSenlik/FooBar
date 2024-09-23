from example_library.firestore_client import get_firestore_db_client


def basic_foo():
    """
    Basic example of something that works
    :return:
    """
    firestore_db = get_firestore_db_client()
    res = firestore_db.collection("fooBar/num_requests/count").document("count_file").get().to_dict()
    new_count = 1

    if res not in [None, {}]:
        new_count = res['new_count'] + 1

    firestore_db.collection("fooBar/num_requests/count").document("count_file").set({
        'new_count': new_count
    })

    return "Bar"
