# join-us2.py
# join-us2.html 필요
# result.html 필요

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import csv

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def show_form(request: Request) :
    return templates.TemplateResponse(
        "join-us2.html", {"request": request}
    )

@app.post("/join")
def submit_form(
    request: Request,
    name: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    age: str = Form(...),
    gender: str = Form(...) 
) :
    per_info = {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "age": age,
        "gender": gender
    }
    print(">>>> [POST - /join]", name, address, phone, email, age, gender)
    
    #CSV 파일로 저장
    CSV_FILE = "./person.csv"
    with open(CSV_FILE, "a+", newline="", encoding="utf-8") as f:
        f.seek(0)
        first_line = f.readline().strip()
        
        writer = csv.writer(f)
        if not first_line:
            writer.writerow(["submitted_at", "name", "address", "phone", "email", "age", "gender"])
        writer.writerow(["submitted_at", name, address, phone, email, age, gender])
    
    # 아래는 리턴값에 대한 3가지 방법
    # return per_info
    # => 위 방법은 제이슨 형태로 바로 보이게 하는 방법 / 이쁘지 않다.
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "age": age,
        "gender": gender
        
    })
    
    # 아래 방법은 HTML을 바로 표현하는 방법
    # 간단히 표현은 가능하나, 프론트엔드 / 백엔드 구분하는 방식에는 맞지 않다.
    #return HTMLResponse(f"""
    #    <!DOCTYPE html>
    #    <html>
    #        <body>
    #            <h1>결과페이지</h1>
    #            <ul>
    #                <li>성명: {name}</li>
    #                <li>주소: {address}</li>
    #                <li>전화번호: {phone}</li>
    #                <li>email: {email}</li>
    #                <li>나이: {age}</li>
    #                <li>성별: {gender}</li>
    #        </body>
    #    </html>
    #""")