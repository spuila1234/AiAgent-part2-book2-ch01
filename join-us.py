# 실습
# 1. join-us.html 파일을 만든다.
# 2. 신상 정보 입력 받을 수 있도록 form 구현
# 3. 성명, 주소, 전화번호, email, 나이, 성별 등
# 4. join-us.py에서 데이터를 전송 받아서 터미널에 출력 or 파일 저장

# join-us.html 필요

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hold() :
    print("사이트 접속")
    return {
        "message" : "반갑습니다."
    }

@app.get("/per_info")
def get(name, password, number, email, age, gender) :
    per_info = {
        "이름" : name, 
        "비밀번호" : password, 
        "전화번호" : number, 
        "이메일" : email, 
        "나이" : age, 
        "성별" : gender
    }
    print(per_info)
    with open("per_info.txt", "a", encoding="utf-8") as f :
        line = f"이름={name}, 비밀번호={password}, 전화번호={number}, 이메일={email}, 나이={age}, 성별={gender}\n"
        f.write(line)
    return {
        "message" : "개인 정보 입력 완료."
    }