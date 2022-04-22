from abc import ABC, abstractmethod
from typing import List
import urwid

class AbstactRender(ABC):
    @abstractmethod
    def show(self):
        ...

    @abstractmethod
    def save(self, filename: str):
        ...

class UrwidRender(AbstactRender):
    lines: List[str]
    text: urwid.Text
    filler: urwid.Filler

    def add_lines(self, lines: List[str]) -> "UrwidRender":
        self.lines = lines
        self.text = urwid.Text("\n".join(self.lines))
        self.filler = urwid.Filler(self.text, "top")
        return self

    @staticmethod
    def handle_input(key):
        if key.lower() == "q":
            raise urwid.ExitMainLoop()

    def show(self):
        loop = urwid.MainLoop(self.filler, unhandled_input=self.handle_input)
        loop.run()
    
    def save(self, filename: str):
        with open(filename, "w") as f:
            f.write("\n".join(self.lines))
