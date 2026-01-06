#main.py
from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
# URL 기본값일시 아래 내용 출력
# ex) http://127.0.0.1:8000
# => {"message":"안녕하세요!!!"} 출력
def read_root():
    return {"message": "안녕하세요!!!"}


@app.get("/hello")
# URL이 hello로 입력될시 아래 함수 출력
# ex) http://127.0.0.1:8000/hello
# => {"name":"hong"} 출력
# ex) http://127.0.0.1:8000/hello?name=kim
# => {"name":"kim"} 출력
def hello(name = "hong") :
    print("[GET] name is", name)
    return {
        "[GET] name":name
    }
    
@app.post("/hello")
def hello2(name:str=Form(...), password:str=Form(...)) :
    print("[POST] name is", name)
    print("[POST] pasword is" , password)
    return {
        "[POST] name": name
    }