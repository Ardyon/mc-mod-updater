import sys

from MCModUpdater.src.core.ArgParser import get_args
from MCModUpdater.src.core.Settings import Settings
from MCModUpdater.src.core.enums import ModLoader
from MCModUpdater.src.core.mmu_core import _logger

args = get_args()


class CLI:
    def __init__(self):
        # TODO: Check for all the necessary arguments
        if args.options_file is None:
            _logger.info(
                "No options file specified, generate one with the GUI, or use the CLI arguments."
            )
            sys.exit(-1)

        self.settings = Settings()

        if args.mc_version:
            self.settings.mc_version = args.mc_version

        if args.modloader:
            self.settings.modloader = ModLoader(args.modloader)

        if args.urls_file:
            # TODO: Read url file
            self.settings.urls = args.urls_file

        if args.download_dir:
            self.settings.download_dir = args.download_dir

        print("Dit is de CLI")

        print(args)


if __name__ == "__main__":
    CLI()
