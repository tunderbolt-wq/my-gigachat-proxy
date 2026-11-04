import os
from gpt2giga import GigaChatProxy

# Читаем ключ из переменных окружения (которые мы зададим в Vercel)
api_key = os.getenv("GIGACHAT_API_KEY")

if not api_key:
    raise ValueError("Установи переменную окружения GIGACHAT_API_KEY")

# Создаем приложение
app = GigaChatProxy(api_key=api_key)

# (GigaChatProxy сам внутри себя создает FastAPI инстанс)
# Нам нужно его извлечь, чтобы Vercel его увидел
fastapi_app = app.app

# Если Vercel не найдет переменную 'app', можно просто:
# from fastapi import FastAPI
# app = FastAPI()
# Но GigaChatProxy удобнее
