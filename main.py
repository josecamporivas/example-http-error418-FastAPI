from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return "Go to http://localhost:8000/error418 to use HTTP error 418 called 'I'm a teapot'"

@app.get("/error418")
async def root():
    raise HTTPException(status_code=418, detail="Error 418 has been achieved successfully!!!")