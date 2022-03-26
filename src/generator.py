class PasswordGenerator:
    characters: str
    digits: int
    
    __slots__ = "charcters", "digits"
    
    def __init__(self, characters: str, digits: int) -> None:
        self.characters = characters
        self.digits = digits
    
    
    def generate(self) -> str:
        ...