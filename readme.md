converter.py <входной_файл.doc> <выходной_файл.docx>

Конвертация через **Aspose.Words**. Чтобы убрать оговорку в документе — положи файл лицензии `Aspose.Words.Python.NET.lic` или `license.lic` в папку со скриптом или задай `ASPOSE_LICENSE_PATH`. Бесплатная временная лицензия: https://purchase.aspose.com/temporary-license/

**Сборка**

- **Windows** (на Windows): pyinstaller --onefile --name converter converter.py` → `dist/converter_win.exe
- **Linux** (на Linux): pyinstaller --onefile --name converter converter.py` → `dist/converter_linux



Кросс-сборки нет: бинарник получается для той ОС, на которой запущен PyInstaller. Чтобы иметь оба файла — собери на Windows, затем на Linux (например, в Docker).

convert dev:
```text
python converter.py C:\Users\Air\Desktop\doc-to-docx\source\source.doc C:\Users\Air\Desktop\doc-to-docx\result\result.docx
```
convert prod:
```text
converter.exe C:\Users\Air\Desktop\doc-to-docx\source\source.doc C:\Users\Air\Desktop\doc-to-docx\result\result.docx
```
