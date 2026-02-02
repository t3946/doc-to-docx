# Конвертирует .doc в .docx: аргументы — путь к .doc и путь к .docx. Лицензия (опционально): ASPOSE_LICENSE_PATH или license.lic в папке скрипта.
import aspose.words as aw
import sys
import os

if len(sys.argv) < 3:
    sys.exit("Использование: converter.py <входной.doc> <выходной.docx>")

inp, out = sys.argv[1], sys.argv[2]
lic_path = os.environ.get("ASPOSE_LICENSE_PATH") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "license.lic")
if lic_path and os.path.isfile(lic_path):
    aw.License().set_license(lic_path)

doc = aw.Document(inp)
doc.save(out)
