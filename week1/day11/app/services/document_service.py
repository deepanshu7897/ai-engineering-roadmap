documents = []


def get_documents():
    return documents


def create_document(document):
    documents.append(document)
    return document


def update_document(doc_id, document):
    if doc_id > len(documents) or doc_id <= 0:
        return None

    documents[doc_id - 1] = document
    return document


def delete_document(doc_id):
    if doc_id > len(documents) or doc_id <= 0:
        return False

    documents.pop(doc_id - 1)
    return True