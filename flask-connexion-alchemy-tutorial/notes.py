
from flask import make_response, abort
from config import db
from models import Person, Note, NoteSchema


def read_all():
    notes = Note.query.order_by(db.desc(Note.timestamp)).all()

    note_schema = NoteSchema(many=True, exclude=["person.notes"])
    data = note_schema.dump(notes).data
    return data


def read_one(person_id, note_id):
    note = (
        Note.query.join(Person, Person.person_id == Note.person_id)
        .filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    if note is not None:
        note_schema = NoteSchema()
        data = note_schema.dump(note).data
        return data

    else:
        abort(404, "Note not found")


def create(person_id, note):
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is None:
        abort(404, "Person not found")

    schema = NoteSchema()
    new_note = schema.load(note, session=db.session).data

    person.notes.append(new_note)
    db.session.commit()

    data = schema.dump(new_note).data

    return data, 201


def update(person_id, note_id, note):
    update_note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    if update_note is not None:

        schema = NoteSchema()
        update = schema.load(note, session=db.session).data

        update.person_id = update_note.person_id
        update.note_id = update_note.note_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_note).data

        return data, 200

    else:
        abort(404, "Note not found")


def delete(person_id, note_id):
    note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    if note is not None:
        db.session.delete(note)
        db.session.commit()
        return make_response(
            "Note {note_id} deleted".format(note_id=note_id), 200
        )

    else:
        abort(404, "Note not found")