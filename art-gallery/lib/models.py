import click
import random
from decimal import Decimal
from gallery import session, Customer, Company, Piece ,Rating,Comment
from see_pieces import see_all_pieces
from view_all_comments import view_all_comments
from view_all_piece_rating import view_all_piece_ratings
from view_all_companies import view_all_companies


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

        new_customer = Customer(name=name, age=age, email=email, address=address, points_per_purchase=points_per_purchase)
        session.add(new_customer)
        session.commit()
        click.echo("Customer details added to the database.")
    else:
        click.echo(click.style("Sorry, we cannot process your order.", fg='red'))
    



@click.command()
def piece_input():
    piece_name = click.prompt(click.style("Piece", fg='blue'), type=str)
    company_id = click.prompt(click.style("Company ID", fg='blue'), type=int)
    category_of_piece = click.prompt(click.style("Category", fg='blue'), type=str)
    price = click.prompt(click.style("Price", fg='blue'), type=float)
    
    new_piece = Piece(Name=piece_name, company_id=company_id, Category=category_of_piece, price=price)
    
    session.add(new_piece)
    session.commit()

    click.echo(click.style(f"Piece '{piece_name}' has been added to the database.", fg='green'))




@click.command()
def company_input():
    company_name = click.prompt(click.style("Company Name", fg='blue'), type=str)
    location = click.prompt(click.style("Location", fg='blue'), type=str)
    established_year = click.prompt(click.style("Established Year", fg='blue'), type=int)
    

   
    new_company = Company(name=company_name, location=location, established_year=established_year)
    session.add(new_company)
    session.commit()

    click.echo(click.style(f"Company '{company_name}' has been added to the database.", fg='green'))

@click.command()
def add_comment():
    piece_name = click.prompt(click.style("Name", fg='blue'), type=int)
    comment_text = click.prompt(click.style("Comment", fg='blue'), type=str)
    new_comment = Comment(piece_name=piece_name, text=comment_text)
    session.add(new_comment)
    session.commit()
    click.echo(click.style(f"Your comment has been added.", fg='green'))


@click.command()
def add_piece_rating():
    piece_name = click.prompt(click.style("Piece Name", fg='blue'), type=int)
    rating_score = click.prompt(click.style("Rating (1-5)", fg='blue'), type=int)
    new_rating = Rating(piece_name=piece_name, score=rating_score)
    session.add(new_rating)
    session.commit()
    click.echo(click.style(f"Your rating has been added.", fg='green'))

@click.command()
def see_pieces():
    pieces = session.query(Piece).all()
    for pieces in pieces:
        click.echo(click.style(f"{Piece.name} - ${Piece.price}", fg='green'))

@click.command()

def search_pieces():
    search_term = click.prompt(click.style("Enter a search term", fg='blue'), type=str)
    matching_pieces = session.query(Piece).filter(Piece.name.contains(search_term)).all()
def search_all():
    search_term = click.prompt(click.style("Enter a search term", fg='blue'), type=str)
    matching_customers = session.query(Customer).filter(Customer.name.contains(search_term)).all()

    for customer in matching_customers:
        click.echo(click.style(f"Customer Name: {customer.name}, Email: {customer.email}", fg='green'))
    matching_pieces = session.query(Piece).filter(Piece.name.contains(search_term)).all()
    for Piece in matching_pieces:
        click.echo(click.style(f"Piece: {Piece.name}, Price: {Piece.price}, Category: {Piece.category}", fg='green'))

    matching_companies = session.query(Company).filter(Company.name.contains(search_term)).all()
    for company in matching_companies:
        click.echo(click.style(f"Company Name: {company.name}, Location: {company.location}", fg='green'))
    for Piece in matching_pieces:
        price = Decimal(Piece.price) 
        click.echo(click.style(f"Piece: {Piece.name}, Price: {price}, Category: {Piece.category}", fg='green'))


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
        click.echo("7. View all comments")
        click.echo("8. View all ratings")
        click.echo("9. View all companies")
        click.echo("10. Search pieces")
        click.echo("11. Search all") 
        click.echo("12. Exit")  

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
            see_all_pieces()
        elif choice == 7:
            view_all_comments()
        elif choice == 8:
            view_all_piece_ratings()
        elif choice == 9:
            view_all_companies()
        elif choice == 10:
            search_pieces()
        elif choice == 11:
            search_all()  
        elif choice == 12:
            break  
        else:
            click.echo("Invalid choice. Please choose a number between 1 to 12.")

if __name__ == '__main__':
    main_menu()


   