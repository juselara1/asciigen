from asciigen.image import Image
from asciigen.colorscales import ColorScale
from asciigen.render import UrwidRender
from asciigen.renderer import TextRenderer
from argparse import ArgumentParser

def main() -> int:
    parser = ArgumentParser(description="Generate ASCII art from images.")
    parser.add_argument("-i", "--input", type=str, help="Input image file.")
    parser.add_argument("-o", "--output", type=str, help="Output file.")
    parser.add_argument("-l", "--height", type=int, help="Height of the output image.", default=100)
    parser.add_argument("-w", "--width", type=int, help="Width of the output image.", default=100)
    parser.add_argument("-c", "--colorscale", type=str, help="Color scale to use.")

    args = parser.parse_args()
    input = args.input
    output = args.output
    height = args.height
    width = args.width
    colorscale = args.colorscale

    if not input:
        print("No input file specified.")
        return 1

    image = (
            Image
            .load_from_file(input)
            .resize(width=width, height=height)
            )
    if colorscale is None:
        colorscale = ColorScale.load([
            character for character in 
            "▒░@#─-. "
            ])
    else:
        colorscale = ColorScale.load_from_file(colorscale)
    render = UrwidRender()
    render = (
            TextRenderer()
            .add_image(image)
            .add_colorscale(colorscale)
            .add_render_type(render)
            .render()
            )
    if output is None:
        render.show()
    else:
        render.save(output)
    return 0

def cli():
    exit(main())
