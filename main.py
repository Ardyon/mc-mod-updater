import sys

from PySide6.QtWidgets import QApplication

from MCModUpdater.src.cli.mmu_cli import CLI
from MCModUpdater.src.cli.utills.screen import get_app_version
from MCModUpdater.src.core.ArgParser import get_args
from MCModUpdater.src.core.Settings import Settings
from MCModUpdater.src.utils.utils import except_hook
from MCModUpdater.src.qt.gui.mmu_qt import GUI


sys.excepthook = except_hook
args = get_args()

# TODO: Fix logger is loaded when it shouldn't
if args.version:
    print(get_app_version())
    sys.exit(0)

Settings().load()

if args.gui:
    app = QApplication(sys.argv)
    UIWindow = GUI()
    sys.exit(app.exec())
else:
    CLI()
