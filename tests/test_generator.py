from password_generator.flags import get_flags
from password_generator.main import generate_password


def test_password_generation() -> None:
    """
        Tests the `password_generator.main.generate_password()` method to ensure it
        returns a string of proper length and contains the right set of characters.
    """

    password = generate_password("ab", 2)

    assert "a" in password or "b" in password
    assert len(password) == 2


def test_get_flags() -> None:
    """
        Tests the `password_generator.flags.get_flags()` method to ensure it
        returns the given flags and parameters in proper order.
    """
    
    test_flags = "-c aAbBcC -qr ./output.bmp -copy -d 16".split(" ")
    flags = get_flags(test_flags)
    
    assert flags == {
        "-c": [ "aAbBcC" ],
        "-qr": [ "./output.bmp" ],
        "-copy": [  ],
        "-d": [ "16" ],
    }
