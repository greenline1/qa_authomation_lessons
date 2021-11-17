import unittest
import requests
import json


class TestBookCRUD(unittest.TestCase):

    def setUp(self):
        self.app_url = 'http://pulse-rest-testing.herokuapp.com/'
        r = requests.get(self.app_url)
        self.books_url = r.json()['Books']
        # new book creation
        self.new_book_details = {"title": "Test book", "author": "Test author"}
        self.new_book = requests.post(self.books_url, data=self.new_book_details)
        self.new_book_id = self.new_book.json()['id']
        self.book_url = f"{self.books_url}/{self.new_book_id}"
        print(self.book_url)

    def tearDown(self):
        requests.delete(self.book_url)

    def test_book_created_status_code(self):
        self.assertEqual(self.new_book.status_code, 201)

    def test_book_created_id_check(self):
        self.assertEqual(self.new_book_id, self.new_book_id)

    def test_book_created_author_check(self):
        self.assertEqual(self.new_book_details['author'], self.new_book.json()['author'])

    def test_book_created_title_check(self):
        self.assertEqual(self.new_book_details['title'], self.new_book.json()['title'])

    def test_book_updated_details_verification(self):
        # update book details
        updated_book_details = {"title": "Test book, new edition", "author": "John Smith"}
        updated_book = requests.put(self.book_url,
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(updated_book_details))

        request_updated_book = requests.get(self.book_url)
        request_updated_book_data = request_updated_book.json()

        self.assertEqual(updated_book.status_code, 200)
        self.assertEqual(request_updated_book.status_code, 200)
        self.assertEqual(request_updated_book_data['title'], updated_book_details['title'])
        self.assertEqual(request_updated_book_data['author'], updated_book_details['author'])
