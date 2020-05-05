"""Base class to work with Firestore."""
from enum import Enum
from google.cloud import firestore


class BaseFirestore:
    """Base class to work with Firestore."""

    collection: str
    client: firestore.Client

    def __init__(self, collection: str):
        """Constructor."""
        self.collection = collection
        self.client = firestore.Client()


    def get_by_id(self, id: str):
        """Get document by id."""
        document_reference = self.get_document_ref(id)
        document = document_reference.get()

        return document.to_dict()


    def get_by_filters(self, filters: str):
        """Get document by filter."""
        collection = self.get_collection_ref()

        for filter in filters:
            collection = collection.where(filter.field, filter.op.value, filter.value)

        documents = collection.stream()

        return self.generate_array_response(documents)


    def save(self, data: dict):
        """Save new document."""
        collection = self.get_collection_ref()
        document = collection.document()

        document.set(data)

        return document.id


    def generate_array_response(self, docs):
        array = []

        for doc in docs:
            fields = doc.to_dict()
            array.append(fields)

        return array


    def get_document_ref(self, id):
        collection = self.client.collection(self.collection)
        document = collection.document(id)

        return document

    def get_collection_ref(self):
        return self.client.collection(self.collection)


class FirestoreFilter:
    field: str
    op: str
    value: str

    def __init__(self, field, op, value):
        """Constructor."""
        self.field = field
        self.op = op
        self.value = value


class FilterOperation(Enum):
    EQUALS = "=="
    GREATER_THAN = ">"
    GREATER_EQUAL = ">="
    LESS_THAN = "<"
    LESS_EQUAL = "<="
    IN = "in"
    ARRAY_CONTAINS = "array_contains"
