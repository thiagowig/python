from flask import make_response, abort
from config import db
from models import Person, PersonSchema, Note


def read_all():
    people = Person.query.order_by(Person.lname).all()

    person_schema = PersonSchema(many=True)
    data = person_schema.dump(people).data
    return data


def read_one(person_id):
    person = (
        Person.query.filter(Person.person_id == person_id)
        .outerjoin(Note)
        .one_or_none()
    )

    if person is not None:
        person_schema = PersonSchema()
        data = person_schema.dump(person).data
        return data

    else:
        abort(404, "Person not found")


def create(person):
    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (
        Person.query.filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
    )

    if existing_person is None:
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session).data

        db.session.add(new_person)
        db.session.commit()

        data = schema.dump(new_person).data

        return data, 201

    else:
        abort(409, "Person exists already")


def update(person_id, person):
    update_person = Person.query.filter(
        Person.person_id == person_id
    ).one_or_none()

    if update_person is not None:

        schema = PersonSchema()
        update = schema.load(person, session=db.session).data

        update.person_id = update_person.person_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_person).data

        return data, 200

    else:
        abort(404, "Person not found")


def delete(person_id):
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response("Person deleted", 200)

    else:
        abort(404, "Person not found")