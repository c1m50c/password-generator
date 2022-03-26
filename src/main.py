# TODO: Functionality for saving to a `.txt` file.
# TODO: Functionality for saving to a QR Code.

from generator import PasswordGenerator
from flags import get_flags

from string import ascii_letters
from typing import Dict, List
from sys import argv


DEFAULT_PASSWORD_SIZE: int = 16

DEFAULT_USED_CHARACTERS: str = ascii_letters + \
    "0123456789" + "!@#$%^&*()-=_+[]{};:,."

# "-FlagName": [ "Required", "Parameters" ],
VALID_FLAGS: Dict[str, List[str]] = {
    # Characters used in generation, defaults to `DEFAULT_USED_CHARACTERS`.
    "-c": [ "String" ],
    
    # Digits in the outputed password, defaults to `DEFAULT_PASSWORD_SIZE`.
    "-d": [ "Integer" ],
    
    # If present, saves the password as a QR Code.
    "-qr": [  ],
}


def main() -> None:
    flags = get_flags(args=argv[1::])
    
    for flag, parameters in flags.items():
        if flag in VALID_FLAGS:
            if len(parameters) != len(VALID_FLAGS[flag]):
                raise Exception(f"Invalid amount of parameters passed to flag '{flag}', expected parameters {VALID_FLAGS[flag]}.")
        else:
            raise Exception(f"Passed flag '{flag}' does not exist and cannot be processed.")
    
    characters: str = DEFAULT_USED_CHARACTERS if "-c" not in flags else flags["-c"][0]
    password_size: int = DEFAULT_PASSWORD_SIZE if "-d" not in flags else int(flags["-d"][0])
    
    generator = PasswordGenerator(characters, password_size)
    password = generator.generate()
    
    print(password)


if __name__ == "__main__":
    main()