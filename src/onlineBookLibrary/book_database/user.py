import json

users_file = 'users.json'


def get_all_users():
    with open(users_file, 'r') as file:
        return json.load(file)


def save_all_users(users):
    with open(users_file, 'w') as file:
        json.dump(users, file)


def add_user(user_name, user_role):
    users = get_all_users()
    users.append({'user_name': user_name, 'user_role': user_role})
    save_all_users(users)


def verify_admin_user(user_name) -> bool:
    users = get_all_users()
    for user in users:
        if user['user_name'] == user_name and user['user_role'] == 'admin':
            return True
    return False
