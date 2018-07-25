import vk
import getpass

APP_ID = 6642111


def get_user_login():
    return input("Логин:\n")


def get_user_password():
    return getpass.getpass("Пароль:\n")


def get_online_friends(login, password, version=5.73):
    friends_online = []
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends",
    )
    api = vk.API(session, v=version)
    online_friends_id = api.friends.getOnline()
    friends_online = api.users.get(user_ids=online_friends_id)
    return friends_online


def output_friends_to_console(friends_online):
    print("Друзья онлайн:")
    for friend in friends_online:
        print("{} {}".format(friend["first_name"], friend["last_name"]))


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print("Ошибка авторизацииы")
