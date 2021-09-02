import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):

    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = Content.__regex.split(string=string, maxsplit=2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content) -> None:
        super().__init__()
        self.data:dict = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    @type.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self.data.__iter__()

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        data = {}
        for key, value in self.data.items():
            if key == "content":
                data[key] = value
        return str(data)