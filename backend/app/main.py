from fastapi import FastAPI


app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

