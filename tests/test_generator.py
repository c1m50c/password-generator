from app.main import generate_password


def test_password_generation() -> None:
    """
    Tests the `app.main.generate_password()` method to ensure it
    returns a string of proper length and contains the right set of characters.
    """

    password = generate_password("ab", 2)

    assert "a" in password or "b" in password
    assert len(password) == 2
