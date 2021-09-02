from typing import List
from pathlib import Path
import shutil


class Parser:

    def __init__(self) -> None:
        self.extenstions:List[str] = List()

    def valid_extension(self, extenstion):
        return extenstion in self.extenstions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError()

    def read(self, path: Path):
        with path.open() as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):

    extenstions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)
