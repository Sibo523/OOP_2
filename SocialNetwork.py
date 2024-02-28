from User import User


class SocialNetwork(object):
    _instance = None

    def __new__(cls, name):
        # If an instance does not exist, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Additional initialization can be done here
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, '_initialized'):
            self.name = name
            self._users = {}
            self._initialized = True
            print(f"The social network {self.name} was created!")

    def sign_up(self, name, password):
        if name not in self._users:
            if 4 <= len(password) <= 8:
                u1 = User(name, password)
                self._users[name] = u1
                return u1
            else:
                raise ValueError(f"password must be between 4 and 8 characters long")
        else:
            raise ValueError(f"The user {name} already exists!")

    def log_in(self, name, password):
        if name in self._users:
            self._users[name].log_in(password)
            return True
        raise ValueError(f"The user {name} doesn't exists")

    def log_out(self, name):
        if name in self._users:
            self._users[name].log_out()
            return True
        raise ValueError(f"The user {name} doesn't exists")

    def __str__(self):
        s = f"{self.name} social network:"
        for user in self._users:
            s += "\n" + self._users[user].__str__()
        return s
