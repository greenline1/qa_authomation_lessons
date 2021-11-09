import requests
import json


def is_book_id_exist(book_id, books_url):
    all_books = requests.get(books_url).json()
    books_id_list = [book['id'] for book in all_books]
    if book_id in books_id_list:
        return True
    return False

def check_book_by_id(book_id, books_url):
    book_id_url = books_url + '/' + str(book_id)
    check_id = requests.get(book_id_url)
    if check_id.status_code == 200:
        return True
    return False



if __name__ == '__main__':
    # GET request. URLs for Books API
    url = 'http://pulse-rest-testing.herokuapp.com/'
    r = requests.get(url)
    books_url = r.json()['Books']

    # POST request. Add new book and save its id
    new_book_details = {"title": "Python Cookbook", "author": "David Beazley"}
    new_book = requests.post(books_url, data=new_book_details)
    new_book_id = new_book.json()['id']

    # Check if book id is created and is seen on the site
    book_url = f"{books_url}/{new_book_id}"
    print(book_url)

    assert new_book.json()['id'] == new_book_id, "Saved book_id should be the same as created on server"
    assert is_book_id_exist(new_book_id, books_url), "Book id is not in the book list"

    # PUT request. Update book details.
    updated_book_details = {"title": "Python Cookbook, Third Edition.", "author": "David Beazley and Brian K. Jones."}
    updated_book = requests.put(book_url,
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(updated_book_details))





