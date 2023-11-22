from typing import TextIO

from utils import vars


def write_box_dimensions(file: TextIO, branch: bool) -> None:
    file.write(f"{-1} {2} xlo xhi\n")
    file.write(f"{vars.SYSTEM_SIZE_MIN_Y if branch else - 1} {vars.SYSTEM_SIZE_MAX_Y if branch else 2} ylo yhi\n")
    file.write(f"{vars.SYSTEM_SIZE_MIN} {vars.SYSTEM_SIZE_MAX} zlo zhi\n")
    file.write("\n")
