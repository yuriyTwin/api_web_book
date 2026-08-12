from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class SqlLoader:

    def __init__(self, root):

        root = Path(root).resolve()

        print("SQL ROOT =", root)

        self.env = Environment(
            loader=FileSystemLoader(str(root)),
            trim_blocks=True,
            lstrip_blocks=True
        )

        print("SEARCH PATH =", self.env.loader.searchpath)

    def render(self, file, **kwargs):

        print("OPEN =", file)

        template = self.env.get_template(file)

        query = template.render(**kwargs)

        #print(query)
    
        return query
