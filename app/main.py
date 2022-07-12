from sys import argv
from random import randint
from string import ascii_letters
from typing import Dict, List, Union
from qrcode import make as make_qr_code
from pyperclip import copy as copy_to_clipboard
from rich.console import Console

from app.flags import get_flags

DEFAULT_PASSWORD_SIZE: int = 18
DEFAULT_USED_CHARACTERS: str = ascii_letters + \
    "0123456789" + "!@#$%^&*()-=_+[]{};:,."


# "-FlagName": { "parameters": [ NAME : TYPE ], "description": "This Flag does X." .. },
FLAGS: Dict[str, Dict[str, Union[List[str], str]]] = {
    "-c": {
        "parameters": [ "Characters : String" ],
        "description": f"Defines the characters used in password generation.",
        "default_value": f"{DEFAULT_USED_CHARACTERS}",
        "example": "-c aAbBcCdDeEfF0123456789",
    },

    "-d": {
        "parameters": [ "Amount : Integer" ],
        "description": f"Defines the length of the generated password.",
        "default_value": f"{DEFAULT_PASSWORD_SIZE}",
        "example": "-d 32",
    },

    "-qr": {
        "parameters": [ "FilePath : String" ],
        "description": "If present within the flags, the application will save the generated password as a QR Code.",
        "example": "-qr ./output.bmp",
    },

    "-f": {
        "parameters": [ "FilePath : String" ],
        "description": "If present within the flags, the application will save the generated password as text in a file.",
        "example": "-f ./output.txt",
    },

    "-h": {
        "parameters": [  ],
        "description": "Outputs all valid flags and other helpful information.",
        "example": "-h",
    },

    "-copy": {
        "parameters": [  ],
        "description": "If present, copies the generated password to the clipboard.",
        "example": "-copy",
    },
}


def print_helpful_info(console: Console) -> None:
    """
        Method called by the `-h` flag,
        prints the contents of the `FLAGS` dictionary to the standard output.
    """

    console.print("[bold cyan]Password Generator[/bold cyan] ~ [bold green]Help[/bold green]\n")

    for flag, values in FLAGS.items():
        console.print(f"[yellow]Flag [bold]'{flag}'[/bold][/yellow]:")

        for inner_flag, inner_values in values.items():
            console.print(f"\t[bold blue]{inner_flag}[/bold blue]:")
            console.print(f"\t\t[bold]{inner_values}[/bold]")

        print()


def generate_password(characters: str, size: int) -> str:
    """
        Generates a random password equal in length to `size`, while containing the `characters` within the string.

        # Example
        ```py
        password = generate_password("aAbBcC", 4)
        assert password == aBCa # Value is not concrete, but could equal this.
        ```
    """

    get_random_char = lambda : characters[randint(0, len(characters) - 1)]
    return "".join([ get_random_char() for _ in range(0, size) ])


def main() -> None:
    flags = get_flags(args=argv[1::])
    console = Console()

    for flag, parameters in flags.items():
        if flag in FLAGS:
            if len(parameters) != len(FLAGS[flag]["parameters"]):
                raise Exception(f"Invalid amount of parameters passed to flag '{flag}', expected parameters {FLAGS[flag]['parameters']}.")
        else:
            raise Exception(f"Passed flag '{flag}' does not exist and cannot be processed.")

    characters = DEFAULT_USED_CHARACTERS if "-c" not in flags else flags["-c"][0]
    password_size = DEFAULT_PASSWORD_SIZE if "-d" not in flags else int(flags["-d"][0])
    password = generate_password(characters, password_size)

    console.print(f"[bold][yellow]>>>[/yellow] [magenta]{password}[/magenta][/bold]")

    if "-qr" in flags:
        qr_code = make_qr_code(password)
        path = flags["-qr"][0]
        
        qr_code.save(path)
        console.print(f"[bold green]Saved generated password as a QR Code to [white]'{path}'[/white].[/bold green]")

    if "-f" in flags:
        path = flags["-f"][0]
        with open(path, "w") as file:
            file.write(password)
            console.print(f"[bold green]Saved generated password as a text file to [white]'{path}'[/white].[/bold green]")

    if "-h" in flags:
        print_helpful_info(console)

    if "-copy" in flags:
        copy_to_clipboard(password)
        console.print(f"[bold green]Copied generated password to clipboard.[/bold green]")


if __name__ == "__main__":
    main()
