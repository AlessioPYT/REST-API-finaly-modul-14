import unittest
from models import Contact
from crud import create_contact, get_contact_by_id

class TestContactCRUD(unittest.TestCase):

    def setUp(self):
        # Налаштування, яке виконується перед кожним тестом
        self.db = SessionLocal()

    def tearDown(self):
        # Закриття сеансу бази даних після кожного тесту
        self.db.close()

    def test_create_contact(self):
        # Тест створення контакту
        contact_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone_number": "123456789",
            "birthday": "1980-01-01"
        }
        contact = create_contact(self.db, contact_data)
        self.assertEqual(contact.first_name, "John")
        self.assertEqual(contact.email, "johndoe@example.com")

    def test_get_contact_by_id(self):
        # Тест отримання контакту за ID
        contact = get_contact_by_id(self.db, 1)
        self.assertIsNotNone(contact)
        self.assertEqual(contact.id, 1)

if __name__ == '__main__':
    unittest.main()


# щоб запустити python -m unittest discover
