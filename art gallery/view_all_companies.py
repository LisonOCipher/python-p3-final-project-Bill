import click
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('art_gallery.db')
cursor = conn.cursor()

@click.command()
def view_all_companies():
    # Execute a SQL query to fetch all companies from the database
    cursor.execute("SELECT * FROM companies")
    all_companies = cursor.fetchall()

    # Print the details of each company
    for company in all_companies:
        click.echo(click.style(f"Company Name: {company[1]}, Location: {company[2]}, Established Year: {company[3]}", fg='green'))

if __name__ == '__main__':
    view_all_companies()
