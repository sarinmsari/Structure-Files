import os
from pathlib import Path

DIRS = {
    "Docs": [".pdf",".ppt",".xls",".xlsx",".doc",".docx"],
    "Videos": [".mp4",".mov",".mkv"],
    "Images": [".jpg",".jpeg",".png",".gif",".svg"],
    "Music": [".mp3",".wav"],
    "Notes": [".txt",".csv",".json"]
}

def findLocation(ext):
    for category,extensions in DIRS.items():
        for extension in extensions:
            if extension == ext:
                return category
    return "Others"

def organize():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        ext = file_path.suffix.lower()
        if ext == ".py":
            continue
        dir = findLocation(ext)
        dir_path = Path(dir)
        if dir_path.is_dir()!=True:
            dir_path.mkdir()
        file_path.rename(dir_path.joinpath(file_path))

organize()