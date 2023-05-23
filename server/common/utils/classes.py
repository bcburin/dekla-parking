

class NonNullAttributeVerifier:

    def has_updates(self):
        return any(value is not None for value in self.__dict__.values() if value is not None)
