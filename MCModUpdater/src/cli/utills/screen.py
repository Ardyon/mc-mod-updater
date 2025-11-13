import os
import platform

from MCModUpdater.src.core.constants import APP_VERSION, APP_NAME


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def get_app_version():
    return f"{APP_NAME} {APP_VERSION}"
