from gallery import session, Customer, Company, Pieces ,Rating,Comment

session.query(Customer).delete()
session.query(Pieces).delete()
session.query(Rating).delete()
session.query(Comment).delete()

session.commit()

customer_input = [{
  
  "name": "Christoforo",
  "age": 18,
  "email": "cgrandham0@ted.com",
  "address": "Mombasa"
}, {
  
  "name": "Augusta",
  "age": 25,
  "email": "aduchart1@prlog.org",
  "address": "Nairobi"
}, {
  
  "name": "Ara",
  "age": 18,
  "email": "acapon2@intel.com",
  "address": "Nairobi"
}, {
  
  "name": "Jordan",
  "age": 37,
  "email": "jlegh3@gov.uk",
  "address": "Isiolo"
}, {
  
  "name": "Ilaire",
  "age": 42,
  "email": "ibetho4@buzzfeed.com",
  "address": "Nairobi"
}, {
  
  "name": "Sutherland",
  "age": 23,
  "email": "stebald5@wordpress.org",
  "address": "Kajiado"
}, {
  
  "name": "James",
  "age": 12,
  "email": "jflecknoe6@aol.com",
  "address": "Eldoret"
}, {
  
  "name": "Cynthie",
  "age": 18,
  "email": "cgibb7@rambler.ru",
  "address": "Nakuru"
}]
 

customers = []

for datum in customer_input:
    customer = Customer(**datum)
    customers.append(customer)

session.add_all(customers)
session.commit()

print("Done seeding data")

piece_input = [{
  
  "piece_name": "Quail Eggs",
  "company_id": 143,
  "category": "abstruct",
  "price": "$63.71"

  }, {
      
  "piece_name": "lady shaw",
  "company_id": 643,
  "category": "realism",
  "price": "$25.86"
  
  }, {
      
  "piece_name": "see me",
  "company_id": 546,
  "category": "post-modern",
  "price": "$41.80"
  
}, {
  "piece_name": "rabbit hole",
  "company_id": 359,
  "category": "modern",
  "price": "$97.52"

}, {
 "piece_name": "whole",
  "company_id": 143,
  "category": "pre-modern",
  "price": "$26.91",
  
}, {
  "piece_name": "the shepard's lamb",
  "company_id": 350,
  "category": "hyper-realism",
  "price": "$73.65",

}]

pieces = []

for datum in piece_input:
    Piece = Piece(**datum)
    pieces.append(Piece)

session.add_all(Piece)
session.commit()

print("Done seeding data")


company_input = [{
  "company_name": "company A" ,
  "location": "Mombasa",
  "established_year": 2000
}, {
   "company_name": "company T" ,
  "location": "Kiambu",
  "established_year": 2005
}, {
   "company_name": "company G" ,
  "location": "Nairobi",
  "established_year": 2001
}, {
   "company_name": "company X" ,
  "location": "Isiolo",
  "established_year": 2000
  }, {
   "company_name": "company C" ,
  "location": "Mombasa",
  "established_year": 2009

}]

companies = []

for datum in company_input:
    companies = Company(**datum)
    companies.append(Company)

session.add_all(Company)
session.commit()

print("Done seeding data")

add_comment = [{
 "piece_name" : "Quail Eggs",
  "comment_text": "it is so intriguing!"
}, {
  "piece_name" : "lady shaw",
  "comment_text": "this is a real think piece"
}, {
  "piece_name" : "see me",
  "comment_text": "I see you"
}, {
"piece_name" : "rabbit hole",
  "comment_text": "the world so wake up and this"
}, {
  "piece_name" : "whole",
  "comment_text": "I'm impressed"
}, {
  "piece_name" : "the shepard's lamb",
  "comment_text": "this spoke to me. I want it"
}]

Comments = []

for datum in add_comment:
    item = Comment(**datum)
    Comments.append(item)

session.add_all(Comments)
session.commit()

print("Done seeding data")

add_piece_ratings = [{
  "piece_name" : "Quail Eggs",
  "rating"     : 4
  }, {
  "piece_name" : "lady shaw",
  "rating"     : 5
  }, {
      
  "piece_name" : "see me",
  "rating"     : 3
  }, {
      
  "piece_name" : "rabbit hole",
  "rating"     : 5
  }, {
      
  "piece_name" : "whole",
  "rating"     : 4

}]

Ratings = []

for datum in add_piece_ratings:
    rate = Rating(**datum)
    Ratings.append(item)

session.add_all(Ratings)
session.commit()

print("Done seeding data")
