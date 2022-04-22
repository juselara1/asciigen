from abc import ABC, abstractmethod
from asciigen.image import Image
from asciigen.colorscales import ColorScale
from asciigen.render import AbstactRender, UrwidRender

class AbstractRenderer(ABC):

    @abstractmethod
    def add_image(self, image: Image) -> "AbstractRenderer":
        ...

    @abstractmethod
    def add_colorscale(self, colorscale: ColorScale) -> "AbstractRenderer":
        ...

    @abstractmethod
    def add_render_type(self, render: AbstactRender) -> "AbstractRenderer":
        ...

    @abstractmethod
    def render(self) -> AbstactRender:
        pass

class TextRenderer(AbstractRenderer):
    image: Image
    colorscale: ColorScale
    render_type: UrwidRender

    def add_image(self, image: Image) -> "TextRenderer":
        self.image = image
        return self

    def add_colorscale(self, colorscale: ColorScale) -> "TextRenderer":
        self.colorscale = colorscale
        return self

    def add_render_type(self, render: UrwidRender) -> "TextRenderer":
        self.render_type = render
        return self

    def render(self) -> UrwidRender:
        image = self.image.set_levels(self.colorscale.size)
        ascii_image = self.colorscale[image]
        render = self.render_type.add_lines(list(map(lambda line: "".join(line), ascii_image)))
        return render
