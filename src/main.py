from generator import PasswordGenerator
from flags import get_flags

from qrcode import make as make_qr_code
from typing import Dict, List, Union
from rich.console import Console
from string import ascii_letters
from sys import argv


DEFAULT_PASSWORD_SIZE: int = 16

DEFAULT_USED_CHARACTERS: str = ascii_letters + \
    "0123456789" + "!@#$%^&*()-=_+[]{};:,."

# "-FlagName": [ "Required : Type", "Parameters : Type" ],
VALID_FLAGS: Dict[str, Dict[str, Union[List[str], str]]] = {
    # Characters used in generation, defaults to `DEFAULT_USED_CHARACTERS`.
    "-c": {
        "parameters": [ "Characters : String" ],
        "description": f"Defines the characters used in password generation.",
        "default_value": f"{DEFAULT_USED_CHARACTERS}",
    },
    
    # Digits in the outputed password, defaults to `DEFAULT_PASSWORD_SIZE`.
    "-d": {
        "parameters": [ "Amount : Integer" ],
        "description": f"Defines the length of the generated password.",
        "default_value": f"{DEFAULT_PASSWORD_SIZE}",
    },
    
    # If present, saves the password as a QR Code.
    "-qr": {
        "parameters": [ "FilePath : String" ],
        "description": "If present within the flags, the application will save the generated password as a QR Code.",
    },
    
    # If present, saves the password as a file.
    "-f": {
        "parameters": [ "FilePath : String" ],
        "description": "If present within the flags, the application will save the generated password as text in a file.",
    },
    
    # If present, calls the `print_helpful_info()` method.
    "-h": {
        "parameters": [  ],
        "description": "Outputs all valid flags and other helpful information.",
    }
}


def print_helpful_info(console: Console) -> None:
    """
        Method called by the `-h` flag,
        and when automatically when there are no arugments given to the application.
    """
    
    console.print("[bold cyan]Password Generator[/bold cyan] ~ [bold green]Help[/bold green]\n")
    
    for flag, values in VALID_FLAGS.items():
        console.print(f"[yellow]Flag [bold]'{flag}'[/bold][/yellow]:")

        for inner_flag, inner_values in values.items():
            console.print(f"\t[bold blue]{inner_flag}[/bold blue]:")
            console.print(f"\t\t[bold]{inner_values}[/bold]")
        
        print()


def main() -> None:
    console = Console()
    
    # if len(argv) <= 1:
    #     print_helpful_info(console)
    #     return

    flags = get_flags(args=argv[1::])
    
    for flag, parameters in flags.items():
        if flag in VALID_FLAGS:
            if len(parameters) != len(VALID_FLAGS[flag]["parameters"]):
                raise Exception(f"Invalid amount of parameters passed to flag '{flag}', expected parameters {VALID_FLAGS[flag]['parameters']}.")
        else:
            raise Exception(f"Passed flag '{flag}' does not exist and cannot be processed.")
    
    characters: str = DEFAULT_USED_CHARACTERS if "-c" not in flags else flags["-c"][0]
    password_size: int = DEFAULT_PASSWORD_SIZE if "-d" not in flags else int(flags["-d"][0])
    
    generator = PasswordGenerator(characters, password_size)
    password = generator.generate()
    
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


if __name__ == "__main__":
    main()