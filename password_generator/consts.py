from string import ascii_letters
from typing import Dict, List, Union


DEFAULT_PASSWORD_SIZE: int = 18

DEFAULT_USED_CHARACTERS: str = ascii_letters + \
    "0123456789" + "!@#$%^&*()-=_+[]{};:,."

# "-FlagName": { "parameters": [ NAME : TYPE ], "description": "This Flag does X." .. },
FLAGS: Dict[str, Dict[str, Union[List[str], str]]] = {
    "-c": {
        "parameters": [ "Characters : String" ],
        "description": "Defines the characters used in password generation.",
        "default_value": f"{DEFAULT_USED_CHARACTERS}",
        "example": "-c aAbBcCdDeEfF0123456789",
    },

    "-d": {
        "parameters": [ "Amount : Integer" ],
        "description": "Defines the length of the generated password.",
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
