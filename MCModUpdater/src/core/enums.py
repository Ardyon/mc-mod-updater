from enum import Enum


class ModLoader(int, Enum):
    FORGE = 1
    NEOFORGE = 2
    FABRIC = 3
    QUILT = 4
    QUILT_FABRIC_FALLBACK = 5


class SearchResult(int, Enum):
    INITIALISED = 1
    BUSY = 2
    SUCCESS = 3
    API_KEY_INCORRECT = 4
    MOD_NOT_FOUND = 5
    FILE_NOT_FOUND = 6
    URL_NOT_SUPPORTED = 7


class BackupOption(int, Enum):
    BACKUP_IN_DIRECTORY = 1
    DELETE_OLD_FILES = 2
    NO_BACKUP = 3


class ApiKeyRequirement(int, Enum):
    NOT_REQUIRED = 1
    OPTIONAL = 2
    REQUIRED = 3
