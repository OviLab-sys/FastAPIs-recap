from fastapi import FastAPI
from web import explore, creature


app = FastAPI()

app.include_router(explore.router)
app.include_router(creature.router)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)