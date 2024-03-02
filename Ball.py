import random
import hashlib
import datetime

class User:
    def __init__(self, first_name, last_name, profile):
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile
        self.username = self.generate_username()
        self.password = self.generate_password()
        self.creation_date = datetime.datetime.now()

    def generate_username(self):
        return self.first_name[0].lower() + self.last_name.lower()

    def generate_password(self):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
        password = ''.join(random.choice(characters) for i in range(random.randint(12, 16)))
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self, first_name, last_name, profile):
        user = User(first_name, last_name, profile)
        self.users.append(user)
        return user

    def modify_user(self, user, new_first_name=None, new_last_name=None, new_profile=None):
        if new_first_name:
            user.first_name = new_first_name
        if new_last_name:
            user.last_name = new_last_name
        if new_profile:
            user.profile = new_profile

    def delete_user(self, user):
        self.users.remove(user)

    def list_users(self):
        return self.users

    def list_users_by_profile(self, profile):
        return [user for user in self.users if user.profile == profile]

# Exemple d'utilisation
if __name__ == "__main__":
    user_manager = UserManager()
    user1 = user_manager.create_user("John", "Doe", "Scientist")
    user2 = user_manager.create_user("Jane", "Smith", "Doctor")
    user3 = user_manager.create_user("Alice", "Johnson", "Sales")
    user_manager.modify_user(user1, new_profile="Researcher")
    user_manager.delete_user(user3)
    users = user_manager.list_users()
    print("List of Users:")
    for user in users:
        print(f"{user.first_name} {user.last_name} - {user.profile} - Username: {user.username} - Password: {user.password}")
