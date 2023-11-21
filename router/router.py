from fastapi import APIRouter

user = APIRouter()

@user.get('/user')

def root():
  return {"message": "Hi, I'm root for fastAPI "}