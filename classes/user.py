import uuid

class User:
    def __init__(self, nome, cognome, email, password):
        # generiamo un id univoco per l'utente
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.cognome = cognome
        self.score = 0
        self.email = email
        self.password = password

