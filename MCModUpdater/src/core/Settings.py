import json
import os
from json import JSONDecodeError

from dotenv import load_dotenv

from MCModUpdater.src.core.constants import (
    CONFIG_FILE_PATH,
    CONFIG_DIR_PATH,
    ENV_FILE_PATH,
)
from MCModUpdater.src.core.enums import ModLoader, BackupOption, ApiKeyRequirement
from MCModUpdater.src.core.mmu_core import get_all_apis
from MCModUpdater.src.utils.logger import get_logger
from MCModUpdater.src.utils.utils import load_enum, get_default_download_directory


class Settings:
    _instance = None
    _initialized = False

    ignore_api_warning: bool = False
    download_dir: str = get_default_download_directory()
    mc_version: str = ""
    mod_loader: ModLoader = ModLoader.FABRIC
    backup_option: BackupOption = BackupOption.BACKUP_IN_DIRECTORY
    urls: list[str] = []

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         cls._instance.load()
    #     return cls._instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.logger = get_logger()
        return cls._instance

    def load(self):
        """
        Loads the settings
        """

        if self._initialized:
            return

        self.logger.info("Loading global settings...")
        if not os.path.exists(CONFIG_FILE_PATH):
            self.logger.warning("Settings file does not exist, loaded defaults")
            return

        with open(CONFIG_FILE_PATH, "r") as f:
            try:
                data: dict = json.load(f)
                self.ignore_api_warning = data.get(
                    "api_warning_ignore", self.ignore_api_warning
                )
                self.download_dir = data.get("download_dir", self.download_dir)
                self.mc_version = data.get("mc_version", self.mc_version)
                self.mod_loader = (
                    load_enum(ModLoader, data.get("mod_loader")) or self.mod_loader
                )
                self.backup_option = (
                    load_enum(BackupOption, data.get("backup_option"))
                    or self.backup_option
                )
                self.urls = data.get("urls", self.urls)
            except JSONDecodeError:
                self.logger.warning("Settings couldn't be loaded, loaded defaults")
                return

        self.logger.info("Global settings loaded")
        self.load_env()

    def save(self):
        """
        Saves the settings to the config file and ENV file
        """

        self.logger.info("Saving global settings...")

        if not os.path.exists(CONFIG_DIR_PATH):
            os.makedirs(CONFIG_DIR_PATH, exist_ok=True)

        with open(CONFIG_FILE_PATH, "w") as f:
            data: dict = {
                "api_warning_ignore": self.ignore_api_warning,
                "download_dir": self.download_dir,
                "mc_version": self.mc_version,
                "mod_loader": self.mod_loader,
                "backup_option": self.backup_option,
                "urls": self.urls,
            }
            json.dump(data, f, indent=4)
        self.logger.info("Global settings saved")
        self.save_env()

    def load_env(self):
        """
        Loads the API keys to the ENV file
        """

        self.logger.info("Loading ENV file...")

        if not os.path.exists(ENV_FILE_PATH):
            self.logger.info("ENV file not found")
            return

        load_dotenv(ENV_FILE_PATH)
        for api in get_all_apis():
            if api.api_key_requirement is ApiKeyRequirement.REQUIRED:
                api.set_api_key(os.getenv(api.env_name))

        self.logger.info("ENV file loaded")

    def save_env(self):
        """
        Saves the API keys to the ENV file
        """

        self.logger.info("Saving ENV file...")

        with open(ENV_FILE_PATH, "w") as f:
            f.write("# NEVER SHOW/SHARE THIS FILE WITH ANYONE!\n")
            for api in get_all_apis():
                if api.api_key_requirement is not ApiKeyRequirement.REQUIRED:
                    continue
                if api.get_api_key() is None:
                    continue

                f.write(f"{api.env_name}={api.get_api_key()}\n")
        self.logger.info("ENV file saved")
