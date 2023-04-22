# -*- coding: cp949 -*- 
from fastapi import FastAPI
from todo import todo_router
import uvicorn

app = FastAPI()



# 127.3.24.23:8000/ddd ddd���� �ؿ� get���� �����Ѵ�.

# �ؿ� ��� �Ⱥپ� ������ ��Ʈ�ּ�.
# �񵿱� ��� / �Լ� �ϳ� ���� / ���� / ���Ϲ�� ��ųʸ� ����
@app.get("/")
async def welcome() -> dict:
    return{ # �� �ּҷ� ������, ���̽� ���� �������� ����
        "msg" : "hello world??????"
    }

app.include_router(todo_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
