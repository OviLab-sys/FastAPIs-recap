from models import Creature
from fastapi import FastAPI, Depends, params

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()

#a dependency function
def user_dep(name: str=params, password: str=params):
    return{"name":name, "valid": True}

#the path function/endpoint function that depends on the dependency function
@app.get("/user")
def get_user(user: dict= Depends(user_dep)) -> dict:
    return user

#if the dependency function doesn't return any value but just chcks on the validity 
#of a values lets say, then it can be defined within the decorator of the path function/
#web endpoint function as follows.

#the dpendency function
def check_dep(name: str=params, passord: str = params):
    if not name: 
        raise

#the path function
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True


if __name__=="__main__":
    import uvicorn
    uvicorn.run('routes:app', reload=True) 