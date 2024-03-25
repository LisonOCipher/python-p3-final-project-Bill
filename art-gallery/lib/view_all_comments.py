import click
from gallery import session, Comment

@click.command()
def view_all_comments():
    all_comments = session.query(Comment).all()

    for comment in all_comments:
        click.echo(click.style(f"Piece name: {comment.piece_name}, Comment: {comment.text}", fg='green'))