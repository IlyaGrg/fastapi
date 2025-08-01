from fastapi import FastAPI

app = FastAPI()

@app.get("/" , summary = "Главная ручка" , tags = ["Основные ручки"])

def main():
    return "Hello World"