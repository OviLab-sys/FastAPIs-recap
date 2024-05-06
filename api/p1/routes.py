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


"""single path dependency"""
#if the dependency function doesn't return any value but just checks on the validity 
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

"""multiple path dependency"""
# the FastAPI router app is not built for dealing with multiple endpoints at a time.
# so we use APIRouter, as in, app = APIRouter()
# when you define a top level FastAPI application object, you can add dependencies to it 
#that will apply to all path functions as follows.

from fastapi import APIRouter

router = APIRouter(..., dependencies=[Depends(check_dep)])
#that will make check_dep() dependency function to be called for all path functions under router.

# you can as well have more than one dependency function attatched to a fastapi() app instance as follows

def depfunc1():
    pass

def depfunc2():
    pass

app = FastAPI(...,dependencies=[Depends(depfunc1), Depends(depfunc2)])

@app.get("/main")
def get_main():
    pass

if __name__=="__main__":
    import uvicorn
    uvicorn.run('routes:app', reload=True) 