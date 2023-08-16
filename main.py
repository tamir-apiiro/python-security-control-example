from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

# Sample methods for demonstration
def method_one(data):
    return {"result": f"Method One called with data: {data}"}

def method_two():
    return {"result": "Method Two called"}

def method_three(param1, param2):
    return {"result": f"Method Three called with params: {param1}, {param2}"}

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username == correct_username and credentials.password == correct_password:
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.post("/call_method_one")
async def call_method_one(data: dict):
    result = method_one(data)
    return result

@app.get("/call_method_two")
async def call_method_two():
    result = method_two()
    return result

@app.get("/call_method_three")
async def call_method_three(param1: str, param2: int):
    result = method_three(param1, param2)
    return result

@app.get("/call_method_four")
async def call_method_four(credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_user(credentials)
    return {"result": "Authenticated Method Four called"}
