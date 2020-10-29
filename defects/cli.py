import click
from defects.remove_linkers import introduce_defects

@click.command()
@click.argument('num', type=int)
def introduce_defects_cli(num):
    return introduce_defects(num)
