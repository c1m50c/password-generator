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
    "-characters": [ "String" ],
    
    # Digits in the outputed password, defaults to `DEFAULT_PASSWORD_SIZE`.
    "-digits": [ "Integer" ],
    
    # If present, saves the password as a QR Code.
    "-qr": [  ],
}


def main() -> None:
    used_characters: str = DEFAULT_USED_CHARACTERS
    password_size: int = DEFAULT_PASSWORD_SIZE
    
    flags = get_flags(args=argv[1::])
    
    generator = PasswordGenerator(used_characters, password_size)
    password = generator.generate()


if __name__ == "__main__":
    main()