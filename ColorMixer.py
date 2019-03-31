import click
from colorutils import ArithmeticModel, Color, hex_to_rgb


@click.group()
def main():
    """
    Simple CLI to blend colors together.

    Usage:

    blend - blends two colors together when given the colors in rgb or hex
    python3 ColorMixer.py blend <r> <g> <b> <r> <g> <b>
    """
    pass


@click.command()
@click.option('--rgb', 'type', flag_value='rgb')
@click.option('--hex', 'type', flag_value='hex')
@click.argument('blend', nargs=-1)
def blend(blend, type):
    if type == 'rgb':
        c1rgb = int(blend[0]), int(blend[1]), int(blend[2])
        c2rgb = int(blend[3]), int(blend[4]), int(blend[5])
        blended = Color(rgb=(c1rgb), arithmetic=ArithmeticModel.BLEND) + \
            Color(rgb=(c2rgb))
        print(blended)
    if type == 'hex':
        c1 = Color(hex=blend[0])
        c2 = Color(hex=blend[1])
        blended = Color(rgb=(c1), arithmetic=ArithmeticModel.BLEND) + \
            Color(rgb=(c2))
        print(blended)


if __name__ == "__main__":
    blend()
