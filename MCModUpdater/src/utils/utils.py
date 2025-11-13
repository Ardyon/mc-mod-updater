import enum
import json
import logging
import os
import platform
import sys
import urllib.parse

from MCModUpdater.src.core.mmu_core import _logger

# To stop logging of these libraries
logging.getLogger("urllib").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)


def get_slug_from_url(url: str):
    return url.strip().split("/")[-1]


def get_file_name_from_url(url: str):
    file_name = url.strip().split("/")[-1]
    return urllib.parse.unquote(file_name)


def format_json(json_string: str | dict):
    return json.dumps(json_string, indent=4, sort_keys=True)


def except_hook(cls, exception, traceback):
    _logger.critical(
        f"{exception.__class__.__name__}: '{exception}' on line {traceback.tb_lineno} "
        f"in file '{os.path.basename(exception.__traceback__.tb_frame.f_code.co_filename)}'"
    )
    sys.__excepthook__(cls, exception, traceback)


def get_default_download_directory():
    system = platform.system()
    if system == "Windows":
        return os.path.expanduser(r"~\AppData\Roaming\.minecraft\mods").replace(
            "\\", "/"
        )
    elif system == "Linux":
        return os.path.expanduser(r"~/.minecraft/mods")
    elif system == "Darwin":
        return os.path.expanduser(r"~/Library/Application Support/minecraft/mods")
    else:
        return ""


def clean_url_list(urls: list[str]) -> list[str]:
    cleaned: list[str] = []

    for url in urls:
        url = url.strip()

        if url.startswith("#"):
            continue

        if url == "\n" or not url:
            continue

        cleaned.append(url)

    return cleaned


def load_enum(enum_type: enum, name_or_index: int | str) -> enum.Enum | None:
    """
    Args:
        enum_type: An enum
        name_or_index: The enum value, can be index or name

    Returns:
        The enum, or None if the value is not found, or index is out of range
    """

    try:
        if isinstance(name_or_index, int):
            enum_var = enum_type(name_or_index)
            return enum_var
        elif isinstance(name_or_index, str):
            enum_var = enum_type[name_or_index]
            return enum_var
    except (ValueError, KeyError):
        return None
