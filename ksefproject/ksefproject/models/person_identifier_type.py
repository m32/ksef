from enum import Enum

class PersonIdentifierType(str, Enum):
    NIP = "Nip"
    PESEL = "Pesel"

    def __str__(self) -> str:
        return str(self.value)
