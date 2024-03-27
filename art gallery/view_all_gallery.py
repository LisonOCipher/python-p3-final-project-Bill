import click
import sqlite3
# from gallery import comment

@click.command()
def view_all_comments():
    # Connect SQLite database
    conn = sqlite3.connect('art_gallery.db')
    cursor = conn.cursor()

    # Retrieve all comments from the database
    cursor.execute("SELECT piece_name, comment_text FROM comments")
    all_comments = cursor.fetchall()

    # Print all comments
    for comment in all_comments:
        click.echo(click.style(f"Piece name: {comment[0]}, Comment: {comment[1]}", fg='green'))

    # Close the connection
    conn.close()

if __name__ == '__main__':
    view_all_comments()
