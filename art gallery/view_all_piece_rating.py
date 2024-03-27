import click
import sqlite3

@click.command()
def view_all_ratings():
    # Connect to the SQLite database
    conn = sqlite3.connect('art_gallery.db')
    cursor = conn.cursor()

    # Retrieve all ratings from the database
    cursor.execute("SELECT * FROM ratings")
    all_ratings = cursor.fetchall()

    # Print all ratings
    for rating in all_ratings:
        click.echo(click.style(f" Piece name: {rating[1]}, Rating: {rating[2]}", fg='green'))

    # Close the connection
    conn.close()

if __name__ == '__main__':
    view_all_ratings()
