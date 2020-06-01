# PB1 ABHISHEK WAHANE
# PyMongo Connectivity

# Create Connection usign pymongo
from pymongo import MongoClient

# Create instance
client = MongoClient()

# Create databases
db = client.news2020

# Create collections and insert documents
posts = db.posts

post_1 = {
    'title': 'Covid-19 Vaccine',
    'content': 'This might take 18 months',
    'author': 'Bill'
}

post_2 = {
    'title': 'Learn From Home',
    'content': 'Learning from Home essential',
    'author' : 'Sal Khan'
}

post_3 = {
    'title': 'Work From Home',
    'content': 'This might affect Work Life Balance',
    'author' : 'Rajan'
}

result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(result.inserted_ids))

#find documents
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)

#Count total documnets
posts.count_documents({})

#deleting record
posts.delete_one({'author':'Rajan'})
