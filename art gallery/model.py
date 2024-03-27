import click
import random
import sqlite3
# from gallery import customer, Company, Piece, Rating, Comment

# Establish SQLite connection
conn = sqlite3.connect('art_gallery.db')
cursor = conn.cursor()

# Define command line functions

@click.command()
def customer_input():
    name = click.prompt(click.style("Name", fg='blue'), type=str)
    age = click.prompt(click.style("Age", fg='blue'), type=int)
    email = click.prompt(click.style("Email", fg='blue'), type=str)
    address = click.prompt(click.style("Address", fg='blue'), type=str)
    points_per_purchase = random.randint(1, 3)
    discount_percentage = min(5 + (points_per_purchase // 100) * 5, 20)
    discount_message = click.style(f"You will get a {discount_percentage}% discount on your next purchase!", fg='green')

    if age >= 8:
        click.echo(click.style(f"Hello {name}, thank you for choosing art-gallery. Your satisfaction is our priority.", fg='green'))
        click.echo(discount_message)

        # Inserting customer details into the database
        cursor.execute("INSERT INTO customers (name, age, email, address) VALUES (?, ?, ?, ?)", (name, age, email, address))
        conn.commit()
        click.echo("Customer details added to the database.")
    else:
        click.echo(click.style("Sorry, we cannot process your order.", fg='red'))

        

@click.command()
def piece_input():
    piece_name = click.prompt(click.style("Piece", fg='blue'), type=str)
    company_id = click.prompt(click.style("Company ID", fg='blue'), type=int)
    category_of_piece = click.prompt(click.style("Category", fg='blue'), type=str)
    price = click.prompt(click.style("Price", fg='blue'), type=float)
    
    # Inserting piece details into the database
    cursor.execute("INSERT INTO pieces (piece_name, company_id, category_of_piece, price) VALUES (?, ?, ?, ?)", (piece_name, company_id, category_of_piece, price))
    conn.commit()

    click.echo(click.style(f"Piece '{piece_name}' has been added to the database.", fg='green'))

@click.command()
def delete_piece():
    piece_name = click.prompt(click.style("Piece Name to Delete", fg='red'), type=str)
    
    cursor.execute("SELECT * FROM pieces WHERE piece_name=?", (piece_name,))
    existing_piece = cursor.fetchone()
    
    if existing_piece:
        
        cursor.execute("DELETE FROM pieces WHERE piece_name=?", (piece_name,))
        conn.commit()
        click.echo(click.style(f"Piece '{piece_name}' has been deleted from the database.", fg='green'))
    else:
        click.echo(click.style(f"Piece '{piece_name}' not found in the database.", fg='yellow'))

@click.command()
def company_input():
    company_name = click.prompt(click.style("Company Name", fg='blue'), type=str)
    location = click.prompt(click.style("Location", fg='blue'), type=str)
    established_year = click.prompt(click.style("Established Year", fg='blue'), type=int)
    
    # Inserting company details into the database
    cursor.execute("INSERT INTO companies (company_name, location, established_year) VALUES (?, ?, ?)", (company_name, location, established_year))
    conn.commit()

    click.echo(click.style(f"Company '{company_name}' has been added to the database.", fg='green'))

@click.command()
def add_comment():
    piece_name = click.prompt(click.style("Piece Name", fg='blue'), type=str)
    comment_text = click.prompt(click.style("Comment", fg='blue'), type=str)
    
    # Inserting comment details into the database
    cursor.execute("INSERT INTO comments (comment_text, piece_name) VALUES (?, ?)", (comment_text, piece_name))
    conn.commit()
    
    click.echo(click.style(f"Your comment has been added.", fg='green'))

@click.command()
def add_piece_rating():
    piece_name = click.prompt(click.style("Piece Name", fg='blue'), type=str)
    rating_score = click.prompt(click.style("Rating (1-5)", fg='blue'), type=int)
    
    # Inserting rating details into the database
    cursor.execute("INSERT INTO ratings (piece_name, rating_score) VALUES (?, ?)", (piece_name, rating_score))
    conn.commit()
    
    click.echo(click.style(f"Your rating has been added.", fg='green'))

@click.command()
def see_pieces():
    # Fetching and displaying all pieces from the database
    cursor.execute("SELECT piece_name, price FROM pieces")
    pieces = cursor.fetchall()
    for piece in pieces:
        click.echo(click.style(f"{piece[0]} - ${piece[1]}", fg='green'))

@click.command()
def search_pieces():
    search_term = click.prompt(click.style("Enter a search term", fg='blue'), type=str)
    
    # Searching for pieces by name and displaying the results
    cursor.execute("SELECT piece_name, price, category_of_piece FROM pieces WHERE piece_name LIKE ?", ('%' + search_term + '%',))
    matching_pieces = cursor.fetchall()
    for piece in matching_pieces:
        click.echo(click.style(f"Piece: {piece[0]}, Price: {piece[1]}, Category: {piece[2]}", fg='green'))

@click.command()
def main_menu():
    while True:
        click.echo("Welcome to art-gallery:")
        click.echo("1. Add customer details")
        click.echo("2. Add piece details")
        click.echo("3. Add company details")
        click.echo("4. Add a comment")
        click.echo("5. Add a rating")
        click.echo("6. See all pieces")
        click.echo("7. Search pieces")
        click.echo("8. Exit")

        choice = click.prompt("Your choice", type=int)

        if choice == 1:
            customer_input()
        elif choice == 2:
            piece_input()
        elif choice == 3:
            company_input()
        elif choice == 4:
            add_comment()
        elif choice == 5:
            add_piece_rating()
        elif choice == 6:
            see_pieces()
        elif choice == 7:
            search_pieces()
        elif choice == 8:
            break
        else:
            click.echo("Invalid choice. Please choose a number between 1 and 8.")

if __name__ == '__main__':
    main_menu()