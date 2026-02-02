FROM python:3.12-slim

WORKDIR /app

# PyInstaller на Linux требует objdump (пакет binutils)
RUN apt-get update && apt-get install -y --no-install-recommends binutils \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем код проекта
COPY converter.py converter.spec ./

# По умолчанию — показ справки (без аргументов). Свою команду передавайте через docker compose run app ...
CMD ["python", "converter.py"]
