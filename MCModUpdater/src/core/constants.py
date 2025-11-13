import os
import sys


def _get_root_dir(
    target_dir: str, use_normal_path: bool = False, max_attempts: int = 10
) -> str:
    """
    Finds the absolute path to the specified target directory by searching upwards from the current directory.

    Args:
        target_dir: Name of the directory to search for.
        use_normal_path: If True, always return the normal directory path instead of the PyInstaller temporary directory.
        max_attempts: Maximum number of directory levels to search before raising a FileNotFoundError.

    Returns:
        Absolute path to the `target_directory`.

    Raises:
        FileNotFoundError: If unable to find `target_directory` within the specified number of attempts.
    """

    # Check if running in a PyInstaller bundle and `use_normal_path` is True
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") and use_normal_path:
        return os.path.join(os.getcwd(), target_dir)

    curr_dir: str = os.path.dirname(__file__)
    for attempt in range(max_attempts):
        for item in os.listdir(curr_dir):
            if item == target_dir and os.path.isdir(os.path.join(curr_dir, item)):
                return os.path.join(curr_dir, item)

        # Move up one directory level
        curr_dir = os.path.realpath(os.path.join(curr_dir, ".."), strict=True)

    raise FileNotFoundError(
        f"Directory '{target_dir}' not found after {max_attempts} attempts"
    )


def _get_config_dir(root_dir: str, config_dir_name: str) -> str:
    """
    Constructs the absolute path to the configuration directory based on the specified root directory
    and configuration directory name.

    Args:
        root_dir: The root directory where the search for the configuration directory will start.
        config_dir_name: The name of the configuration directory to find within the root directory.

    Returns:
        Absolute path to the configuration directory.

    Raises:
        FileNotFoundError: If the configuration directory cannot be found within the specified root directory.
    """

    root_dir_name: str = os.path.basename(root_dir)
    config_path: str = os.path.join(
        _get_root_dir(root_dir_name, use_normal_path=True), config_dir_name
    )
    return os.path.realpath(config_path)


# General
APP_NAME: str = "MCModUpdater"
APP_VERSION: str = "v2.0.0"
GITHUB_REPO_NAME: str = "AidenRaaphorst/mc-mod-updater"

# ========
# Paths
# ========
ROOT_DIR_PATH: str = _get_root_dir(APP_NAME)

# Resource paths
RESOURCES_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "resources")
ICONS_DIR_PATH: str = os.path.join(RESOURCES_DIR_PATH, "icons")
LOGO_DIR_PATH: str = os.path.join(RESOURCES_DIR_PATH, "logo")
UI_DIR_PATH: str = os.path.join(RESOURCES_DIR_PATH, "ui")
DESIGNER_DIR_PATH: str = os.path.join(RESOURCES_DIR_PATH, "designer")

# Source paths
CORE_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "src", "core")
CLI_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "src", "cli")
QT_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "src", "qt")
GUI_DIR_PATH: str = os.path.join(QT_DIR_PATH, "gui")

# Configuration paths
CONFIG_DIR_PATH: str = _get_config_dir(ROOT_DIR_PATH, os.path.join("..", "config"))
CONFIG_FILE_PATH: str = os.path.join(CONFIG_DIR_PATH, "settings.json")
ENV_FILE_PATH: str = os.path.join(CONFIG_DIR_PATH, ".env")
LOG_FILE_PATH: str = os.path.join(CONFIG_DIR_PATH, "log.txt")
PLUGINS_DIR_PATH: str = os.path.join(CONFIG_DIR_PATH, "plugins")
