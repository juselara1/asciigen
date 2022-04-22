# asciigen

This is package allows to convert images into ascii art using `numpy` and `opencv`.

## Installation

* You can install this package via `pip`:

    ```sh
    pip install asciigen
    ```

* Installation with `poetry`:

    ```sh
    poetry add asciigen
    ```

## Usage

You can use `asciigen` as a cli:

```sh
> asciigen --help

usage: asciigen [-h] [-i INPUT] [-o OUTPUT] [-l HEIGHT] [-w WIDTH] [-c COLORSCALE]

Generate ASCII art from images.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input image file.
  -o OUTPUT, --output OUTPUT
                        Output file.
  -l HEIGHT, --height HEIGHT
                        Height of the output image.
  -w WIDTH, --width WIDTH
                        Width of the output image.
  -c COLORSCALE, --colorscale COLORSCALE
                        Color scale to use.
```
