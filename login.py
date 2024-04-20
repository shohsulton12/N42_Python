users = [
    {
        'username': 'admin',
        'password': '123',
    },
    {
        'username': "john",
        'password': 'admin123'
    }
]


def get_user_by_username(username):
    for user in users:
        if user['username'] == username:
            return user
    return None


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = get_user_by_username(username)
    if not user:
        print("User not found")
    else:
        if user['password'] == password:
            print("Login successfully")
        else:
            print('Login failed')


if __name__ == '__main__':
    login()



