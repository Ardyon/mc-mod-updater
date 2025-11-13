import argparse

from MCModUpdater.src.core.enums import ModLoader

_parser = argparse.ArgumentParser()
_parser.add_argument(
    "-v", "--version", help="Show application version", action="store_true"
)
_parser.add_argument("-g", "--gui", help="Enables GUI", action="store_true")
_parser.add_argument(
    "-o", "--options-file", help="Options file (relative or absolute path)"
)
_parser.add_argument("--mc-version", help="Override Minecraft version")
_parser.add_argument(
    "--modloader", help="Override modloader", choices=[ml.value for ml in ModLoader]
)
_parser.add_argument(
    "-u", "--urls-file", help="Override urls (relative or absolute path)"
)
_parser.add_argument("-d", "--download-directory", help="Override download directory")
_parser.add_argument("-f", "--force", help="Skip API key warning")
_parser.add_argument("-y", help="Skip confirmation")
args = _parser.parse_args()


def get_args():
    return args
