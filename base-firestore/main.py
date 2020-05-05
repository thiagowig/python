from src.base_firestore import BaseFirestore
from src.base_firestore import FirestoreFilter
from src.base_firestore import FilterOperation

base = BaseFirestore("users")

#
#id = base.save({
#    "name": "Thiago Fonseca"
#})
#
#print("ID: " + id)

filter = FirestoreFilter("name", FilterOperation.EQUALS, "Thiago Fonseca")

data = base.get_by_filters([filter])

print(data)