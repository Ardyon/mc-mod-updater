import os
import subprocess

from MCModUpdater.src.core.constants import GUI_DIR_PATH, UI_DIR_PATH

input_directory = UI_DIR_PATH
output_directory = GUI_DIR_PATH

# This converts all .ui files in the input directory to .py files in the output directory.
for root, _, files in os.walk(input_directory):
    for file in files:
        if file.endswith(".ui"):
            ui_file_path = os.path.join(root, file)
            base_name = os.path.splitext(file)[0]
            if output_directory:
                # Create the output directory if it doesn't exist (including
                # any necessary intermediate directories)
                output_path = os.path.join(
                    output_directory,
                    os.path.relpath(root, input_directory),
                )
                os.makedirs(output_path, exist_ok=True)  # Creates needed dirs

                py_file_name = base_name + "_ui.py"
                py_file_path = os.path.join(output_path, py_file_name)
            else:
                py_file_path = os.path.join(root, base_name + "_ui.py")

            try:
                subprocess.run(
                    [
                        "pyside6-uic",
                        ui_file_path,
                        "-o",
                        py_file_path,
                    ],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                print(f"Successfully converted {ui_file_path} to {py_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {ui_file_path}:")
                # Print the error message from pyside6-uic
                print(e.stderr)

# This converts the resources file to a .py file.
try:
    subprocess.run(
        [
            "pyside6-uic",
            ui_file_path,
            "-o",
            py_file_path,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    print(f"Successfully converted {ui_file_path} to {py_file_path}")
except subprocess.CalledProcessError as e:
    print(f"Error converting {ui_file_path}:")
    # Print the error message from pyside6-uic
    print(e.stderr)