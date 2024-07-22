import unittest
from app import create_app, db
from app.domain.entities.user import User

class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        response = self.client.post('/api/users/', json={
            'username': 'testuser',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['username'], 'testuser')
    
    def test_get_user(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/api/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['username'], 'testuser')

    def test_update_user(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.put(f'/api/users/{user.id}', json={
            'username': 'updateduser',
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['username'], 'updateduser')

    def test_delete_user(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        response = self.client.delete(f'/api/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'User deleted successfully')

if __name__ == '__main__':
    unittest.main()
