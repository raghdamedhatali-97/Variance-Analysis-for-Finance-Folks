"""Wrap bridge-builder.html (artifact body) into a standalone index.html."""
from pathlib import Path
src = Path(__file__).with_name("bridge-builder.html").read_text(encoding="utf-8")
Path(__file__).with_name("index.html").write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
    + src + "\n</body>\n</html>\n", encoding="utf-8")
