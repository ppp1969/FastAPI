# -*- coding: cp949 -*- 
from fastapi import FastAPI
from todo import todo_router
import uvicorn

app = FastAPI()



# 127.3.24.23:8000/ddd ddd값은 밑에 get에서 관할한다.

# 밑에 얘는 안붙어 있으니 루트주소.
# 비동기 방식 / 함수 하나 정의 / 웰컴 / 리턴방식 딕셔너리 형식
@app.get("/")
async def welcome() -> dict:
    return{ # 요 주소로 들어오면, 제이슨 파일 형식으로 리턴
        "msg" : "hello world??????"
    }

app.include_router(todo_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
