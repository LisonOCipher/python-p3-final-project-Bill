import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('art_gallery.db')
cursor = conn.cursor()

# Seed data for customers
customer_input = [
    {"name": "Christoforo", "age": 18, "email": "cgrandham0@ted.com", "address": "Mombasa"},
    {"name": "Augusta", "age": 25, "email": "aduchart1@prlog.org", "address": "Nairobi"},
    {"name": "Ara", "age": 18, "email": "acapon2@intel.com", "address": "Nairobi"},
    {"name": "Jordan", "age": 37, "email": "jlegh3@gov.uk", "address": "Isiolo"},
    {"name": "Ilaire", "age": 42, "email": "ibetho4@buzzfeed.com", "address": "Nairobi"},
    {"name": "Sutherland", "age": 23, "email": "stebald5@wordpress.org", "address": "Kajiado"},
    {"name": "James", "age": 12, "email": "jflecknoe6@aol.com", "address": "Eldoret"},
    {"name": "Cynthie", "age": 18, "email": "cgibb7@rambler.ru", "address": "Nakuru"}
]

for customer_data in customer_input:
    cursor.execute("INSERT INTO customers (name, age, email, address) VALUES (?, ?, ?, ?)", 
                   (customer_data['name'], customer_data['age'], customer_data['email'], customer_data['address']))

# Seed data for companies
company_input = [
    {"company_name": "Company A", "location": "Mombasa", "established_year": 2000},
    {"company_name": "Company T", "location": "Kiambu", "established_year": 2005},
    {"company_name": "Company G", "location": "Nairobi", "established_year": 2001},
    {"company_name": "Company X", "location": "Isiolo", "established_year": 2000},
    {"company_name": "Company C", "location": "Mombasa", "established_year": 2009}
]

for company_data in company_input:
    cursor.execute("INSERT INTO companies (company_name, location, established_year) VALUES (?, ?, ?)", 
                   (company_data['company_name'], company_data['location'], company_data['established_year']))

# Seed data for pieces
piece_input = [
    {"piece_name": "Quail Eggs", "company_id": 1, "category_of_piece": "Abstract", "price": 63.71},
    {"piece_name": "Lady Shaw", "company_id": 2, "category_of_piece": "Realism", "price": 25.86},
    {"piece_name": "See Me", "company_id": 3, "category_of_piece": "Post-Modern", "price": 41.80},
    {"piece_name": "Rabbit Hole", "company_id": 4, "category_of_piece": "Modern", "price": 97.52},
    {"piece_name": "Whole", "company_id": 1, "category_of_piece": "Pre-Modern", "price": 26.91},
    {"piece_name": "The Shepard's Lamb", "company_id": 5, "category_of_piece": "Hyper-Realism", "price": 73.65}
]

for piece_data in piece_input:
    cursor.execute("INSERT INTO pieces (piece_name, company_id, category_of_piece, price) VALUES (?, ?, ?, ?)", 
                   (piece_data['piece_name'], piece_data['company_id'], piece_data['category_of_piece'], piece_data['price']))

# Commit changes and close connection
conn.commit()
conn.close()

print("Done seeding data")
