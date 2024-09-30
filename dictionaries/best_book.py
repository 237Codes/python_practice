'''

Imagine you are working on a book review software like Goodreads. 
Write a function named highest_rated() that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter. 
Each dictionary represents data associated with a book, including its title, author, 
and rating. The function should return the dictionary for the book with the highest rating.

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
Expected Output:

{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}

'''

'''

UPI - Understand

- Given a list of dictionaries we are looking for the dictionary with the max rating (rating 
is a key in the dictionary, so we have to check the value of that key and see which is the highest)
- Return the dictionary for book with highest rating

UPI - Plan

- Loop through the list
- For each dictionary in the list, look for the key called rating,
- if the rating is > than highest so far, set the rating to highest and save the index for that dictionary'
- At the end, we use that index to return the highest rated book

UPI - Impliment

'''
def highest_rated(books):
    highest_rating = 0
    highest_rated_book = {}

    for dict in books:
        for key in dict:
            if key == "rating" and dict[key] > highest_rating:
                highest_rating = dict[key]
                highest_rated_book = dict.copy()
    return highest_rated_book

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))