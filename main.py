"""Deliver the bundled one-day news picture to the harness output folder."""

from os import environ
from pathlib import Path
from shutil import copyfile


def picture_beside_this_script() -> Path:
    return Path(__file__).resolve().with_name("entry.png")


def chosen_output_folder() -> Path:
    configured = environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(configured) if configured else Path("/output")


def deliver_picture() -> None:
    source_picture = picture_beside_this_script()
    target_folder = chosen_output_folder()
    target_folder.mkdir(parents=True, exist_ok=True)
    copyfile(source_picture, target_folder / source_picture.name)


if __name__ == "__main__":
    deliver_picture()
