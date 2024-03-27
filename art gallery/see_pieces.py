import click
import sqlite3
from gallery import Pieces

@click.command()
def see_all_pieces():
    # Connect SQLite database
    conn = sqlite3.connect('art_gallery.db')
    cursor = conn.cursor()

    # Execute SQL query to retrieve all pieces
    cursor.execute("SELECT * FROM pieces")
    pieces = cursor.fetchall()

    # Display retrieved pieces
    for piece in pieces:
        click.echo(click.style(f"Piece name: {piece[1]}, Price: {piece[4]}, Category: {piece[3]}", fg='green'))

    # Close connection
    conn.close()

if __name__ == '__main__':
    see_all_pieces()
