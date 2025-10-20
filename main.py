from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Разрешаем CORS для взаимодействия с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextData(BaseModel):
    text: str

@app.post("/save-text")
async def save_text(data: TextData):
    try:
        with open("data.txt", "a", encoding="utf-8") as file:
            file.write(data.text + "\n")
        return {"status": "success", "message": "Text saved successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/get-text")
async def get_text():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            content = file.read()
        return {"status": "success", "content": content}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3002)