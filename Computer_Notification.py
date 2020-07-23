from plyer import notification
from time import sleep

if __name__ == '__main__':
    while True:
        sleep(60 * 60)
        notification.notify(
            title="Leave your Computer NOW!!!",
            message="You have been on your computer for one hour. Get up now.",
            app_icon="D:\MARGORP\Python Code\laptop.ico",
            timeout=10
        )
