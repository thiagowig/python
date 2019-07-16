from flask import current_app
from google.cloud import datastore

builtin_list = list


def init_app(app):
    pass


def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])


def from_datastore(entity):    
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.id

    return entity


def list(limit=20, cursor=None):
    ds = get_client()

    query = ds.query(kind='NoteType')
    query_iterator = query.fetch(limit=limit, start_cursor=cursor)
    page = next(query_iterator.pages)

    entities = builtin_list(map(from_datastore, page))

    return entities


def read(id):
    ds = get_client()
    key = ds.key('NoteType', int(id))
    results = ds.get(key)

    return from_datastore(results)


def delete(id):
    ds = get_client()
    key = ds.key('NoteType', int(id))
    ds.delete(key)


def update(data, id=None):
    ds = get_client()

    if id:
        key = ds.key('NoteType', int(id))
    else:
        key = ds.key('NoteType')

    entity = datastore.Entity(key=key)
    entity.update(data)
    ds.put(entity)

    return from_datastore(entity)


create = update
