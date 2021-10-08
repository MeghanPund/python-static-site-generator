from pathlib import Path

class Site:
    
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = 'c:/Users/Brazuka/python-static-site-generator/'
