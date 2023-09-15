from models.note_model import Note, NoteSchema
from models.person_model import Person, PersonSchema

# GET /notes
# [
#     {
#         "note_id": 1,
#         "content": "aaa", timestamp:".....",
#         "person": {lname:"...",fname:"...", "person_id":"..."}
#     }
# ]

def read_all():
    notes = Note.query.outerjoin(Person).all()

    note_schema = NoteSchema(many=True)
    results = note_schema.dump(notes)

    return results


# POST /people/{person_id}/notes
# GET /people/{person_id}/notes/{note_id}
# PUT /people/{person_id}/notes/{note_id}
# DELETE /people/{person_id}/notes/{note_id}

