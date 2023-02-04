import unittest
import base64
import json
import pyperclip

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password(self):
        password_entry = Entry()
        generate_password(password_entry)

        password = password_entry.get()
        self.assertTrue(password)
        self.assertEqual(pyperclip.paste(), password)

    def test_save(self):
        website = "test_website"
        email = "test_email@example.com"
        password = "test_password"

        save_data = {}

        save(website, email, password, save_data)

        self.assertIn(website, save_data)
        self.assertEqual(save_data[website]["email"], email)
        self.assertEqual(base64.b64decode(save_data[website]["password"].encode()).decode(), password)

