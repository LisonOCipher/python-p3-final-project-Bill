import click
from gallery import session, Rating

@click.command()
def view_all_ratings():
    all_ratings = session.query(Rating).all()

    for rating in all_ratings:
        click.echo(click.style(f" Piece name: {rating.piece_name}, Rating: {rating.score}", fg='green'))