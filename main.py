from fastapi import FastAPI , HTTPException , Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine , SessionLocal
models.Base.metadata.create_all(bind = engine)
app = FastAPI()
class Notecreate(BaseModel):
    title : str
    content : str
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/notes")
def create_model(note : Notecreate , db: Session = Depends(get_db)):
    db_note = models.Note(title = note.title , content = note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return{"message" : "note created succesfully" , "note": db_note}
@app.get("/notes")
def getall(db : Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return {"notes": notes}
@app.get("/notes/{note_id}")
def getbyid(note_id : int , db : Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404 , detail="note not found")
    return {"note" : note}

@app.put("/notes/{note_id}")
def update_note(note_id : int , updated : Notecreate , db : Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404 , detail="note not found")
    note.title = updated.title
    note.content = updated.content
    db.commit()
    db.refresh(note)
    return{"message" : "note updated sussfully" , "note" : note}

@app.delete("/notes/{note_id}")
def deletenote(note_id: int , db : Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404 , detail="note not found")
    db.delete(note)
    db.commit()
    return{"message" : "note deleted successfully"}

    
    



