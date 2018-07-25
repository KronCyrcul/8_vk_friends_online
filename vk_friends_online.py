import vk
import getpass

APP_ID = 6642111


def get_user_login():
    return input("Логин:\n")


def get_user_password():
    return getpass.getpass("Пароль:\n")


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
    session = vk.Session(app_id=APP_ID)
    api = vk.API(session)
    for friend in friends_online:
        friend_info = api.users.get(user_id=friend, v=VERSION)
        first_name = friend_info[0]["first_name"]
        last_name = friend_info[0]["last_name"]
        print("{} {}".format(first_name, last_name))


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print("Ошибка авторизацииы")
    
