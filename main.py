from database import db
from fastapi import FastAPI,Body
from fastapi.middleware.cors import CORSMiddleware



app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.get('/')
def getRoute():
    return ['/notes','/notes/<pk>']



@app.get('/notes')
def getNotes():
    notes = db.sql('SELECT * FROM notesapp.notes ORDER BY __updatedtime__ DESC')
    return notes

@app.get('/notes/{pk}')
def getNote(pk:str):
    notes = db.search_by_hash('notesapp','notes',[pk],get_attributes=["*"])
    return notes[0]



@app.post('/notes')
def addNotes(data= Body()):
    db.insert('notesapp','notes',[{"body":data['body']}])
    notes = db.search_by_value('notesapp','notes','id',"*",get_attributes=['*'])
    return notes


@app.put('/notes/{pk}')
def updateNotes(pk:str,data=Body()):
    db.update('notesapp','notes',[{"id":pk,"body":data['body']}])
    notes = db.search_by_value('notesapp','notes','id',"*",get_attributes=['*'])
    return notes


@app.delete('/notes/{pk}')
def deleteNotes(pk:str):
    db.delete('notesapp','notes',[pk])
    notes = db.search_by_value('notesapp','notes','id',"*",get_attributes=['*'])
    return notes