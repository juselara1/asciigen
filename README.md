# asciigen

This is package allows to convert images into ascii art using `numpy` and `opencv`.

![comparison](https://raw.githubusercontent.com/juselara1/Resources/master/asciigen/sample.png)

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

## Usage

Suppose you have the an image saved as `sample.jpg`, you can render this image as follows:

```sh
asciigen -i sample.jpg
```

You can change the shape of the image:

```sh
asciigen -i sample.jpg -l 256 -w 256
```

You can specify an output file to save the text:

```sh
asciigen -i sample.jpg -o output.txt
```

Finally, you can change the colorscale or the ascii characters that are used to build the image:

```sh
printf "@. " > scale.txt && asciigen -i sample.jpg -c scale.txt
```
