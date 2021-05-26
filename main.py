from fastapi import FastAPI, Depends, HTTPException
from database import Session, Thingy, engine, BaseModel
app = FastAPI()
# initialize the database
BaseModel.metadata.create_all(bind=engine)
# fastapi dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/viewall")
def page1(db=Depends(get_db)):
    return db.query(Thingy).all()

@app.get("/new:{thingy_id}")
def page2(thingy_id, db=Depends(get_db)):
    # check if that id is already taken
    preexisting_thingy = db.query(Thingy).filter(Thingy.id == thingy_id).first()
    if preexisting_thingy:
        raise HTTPException(status_code=400, detail="Thingy already exists")
    
    # add new thingy to db
    thingy = Thingy(id=thingy_id)
    db.add(thingy)
    db.commit()
    db.refresh(thingy)
    return thingy
