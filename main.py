from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

class Note(BaseModel):
    id : int
    title : str
    content : str

app = FastAPI()
notes = []
@app.post("/notes")
def create_note(note : Note):
    notes.append(note)
    return {"message": "note created", "note": note}

@app.get("/notes")
def get_note():
    return {"note": notes}

@app.get("/notes/{note_id}")
def getbyid(note_id : int):
    for i , note in enumerate(notes):
        if note_id == note.id:
            return { "note" : note}
    raise HTTPException(status_code= 404 , detail= " note not found")

@app.put("/notes/{note_id}")
def update( note_id : int , updated_note : Note):
    for i, note in enumerate(notes) :
        if note.id ==note_id :
            notes[i] = updated_note
            return {"note": updated_note}
    raise HTTPException(status_code=404 , detail = "note not found")

@app.delete("/notes/{note_id}")
def delete(note_id : int):
    for i , note in enumerate(notes):
        if note_id == note.id:
            notes.pop(i)
            return {"message": "deleted sucessfully"}
    raise HTTPException(status_code = 404 , detail = "note not found")
