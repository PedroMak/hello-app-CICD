from fastapi import FastAPI 

app = FastAPI() 

@app.get("/") 
async def root(): 
    return {"message": "Glitches in the code or gaps in a strange dream..."} 