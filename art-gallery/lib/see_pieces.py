import click
from gallery import session, Pieces

@click.command()
def see_all_pieces():
    pieces = session.query(pieces).all()

    for pieces in Pieces:
        click.echo(click.style(f"Piece name: {pieces.name}, Price: {pieces.price}, Category: {pieces.category}", fg='green'))