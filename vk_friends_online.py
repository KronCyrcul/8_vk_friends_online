import vk


APP_ID = 6642111
ACCESS_TOKEN = "f8eba6cef8eba6cef8eba6cedef88eff71ff8ebf8eba6cea3bcd37667d7e6d4446f46d6"
VERSION = 5.73


def get_user_login():
    return input("Логин:\n")


def get_user_password():
    return input("Пароль:\n")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends",
    )
    api = vk.API(session)
    current_user_id = api.users.get(v=VERSION)[0]["id"]
    online_friends_id = api.friends.getOnline(user_id=current_user_id,
        v=VERSION)
    return online_friends_id


def output_friends_to_console(friends_online):
    session = vk.Session(ACCESS_TOKEN)
    api = vk.API(session)
    for friend in friends_online:
        friend_info = api.users.get(user_id=friend, v=VERSION)
        first_name = friend_info[0]["first_name"]
        last_name = friend_info[0]["last_name"]
        print("{} {}".format(first_name, last_name))


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
