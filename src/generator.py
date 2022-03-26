from random import randint


class PasswordGenerator:
    # Characters used in generating the password.
    characters: str
    
    # Length of the generated password
    digits: int
    
    __slots__ = "characters", "digits"
    
    def __init__(self, characters: str, digits: int) -> None:
        self.characters = characters
        self.digits = digits
    
    
    def random_character(self) -> str:
        """Returns a random character from the `characters` string."""
        return self.characters[randint(0, len(self.characters) - 1)]
    
    
    def generate(self) -> str:
        """
            Generates a password equal in length to the `digits` field,
            populated with random characters from the `characters` field.
            
            # Example
            ```py
            generator = PasswordGenerator("aAbBcCdDeEfF", 5)
            password = generator.generate()
            
            # While unlikely, `password` has the possibility of equaling this.
            assert password == "abfED"
            ```
        """
        
        return "".join([ self.random_character() for _ in range(0, self.digits) ])