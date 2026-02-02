# doc-to-docx — конвертер .doc → .docx, в результате — exe

# 1. Создай venv (Python 3.13 или 3.14 — подойдёт любой из py --list)
#    py -3.13 -m venv temp_env
#    temp_env\Scripts\activate

# 2. Установи зависимости
#    pip install -r requirements.txt

# 3. Собери exe


#    pyinstaller --onefile converter.py
# Готовый exe будет в папке dist/converter.exe

# Использование exe: converter.exe <входной.doc> <выходной.docx>
# Оба пути — абсолютные или относительные.
