class InitSessionSignedRequest:
    def __init__(self, bytes) -> None:
        self._bytes = bytes

    @property
    def bytes(self):
        return self._bytes
    
    @property
    def content(self):
        return self.bytes.decode('UTF-8')
    