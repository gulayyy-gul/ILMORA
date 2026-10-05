def apply_filters(
    documents,
    **filters
):

    result = documents

    for key, value in filters.items():

        if value:

            result = [
                document
                for document in result
                if document.get(key) == value
            ]

    return result
