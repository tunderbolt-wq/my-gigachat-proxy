import os
from gpt2giga import GigaChatProxy

# Читаем ключ
api_key = os.getenv("GIGACHAT_API_KEY")

if not api_key:
    raise ValueError("Установи переменную окружения GIGACHAT_API_KEY")

# Создаем приложение
app = GigaChatProxy(api_key=api_key)

# --- ВОТ ЭТО НОВОЕ: Блок запуска ---
# Vercel увидит это и запустит сервер командой 'python main.py'
if __name__ == "__main__":
    import uvicorn
    # Порт берем из переменной Vercel, если её нет — ставим 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app.app, host="0.0.0.0", port=port)
