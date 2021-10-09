from os import close, path, read, write
from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension is_in(self.extension):
            return True

    def parse(path: Path, source: Path, dest: Path):
        raise(NotImplementedError)

    def read(path):
        with open(path, "r") as f:
            return read(f)

    def write(path, dest, content, ext = ".html"):
        full_path = self.dest / path(ext).with_suffix.name
        with open(full_path, "w") as f:
            f.write(content)