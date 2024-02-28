from Post import Post
from PostFactory import PostFactory


class User(object):

    _factory = PostFactory()

    # Create a User
    def __init__(self, name, password) -> None:
        self._name = name
        self._password = password
        self._following = {}
        self._followers = {}
        self._notif = []
        self._posts = []
        self._logged = True

    def __str__(self):
        return (f"User name: {self._name}, Number of posts:"
                f" {len(self._posts)}, Number of followers: {len(self._followers.keys())}")

    # When a user tries to log in check if the password is the right one
    def check_password(self, password: str) -> bool:
        if password == self._password:
            return True
        return False

    # Log user in
    def log_in(self, password) -> bool:
        if self.check_password(password):
            self._logged = True
            print(f"{self._name} connected")
            return True
        raise ValueError(f"Wrong password for user {self._name}")

    # Log user out
    def log_out(self) -> None:
        self._logged = False
        print(f"{self._name} disconnected")

    # Check if a user is logged
    def is_logged(self) -> bool:
        return self._logged

    # Follow other users
    def follow(self, foll: 'User') -> bool:
        if self._logged:
            if foll._name not in self._following:
                self._following[foll._name] = foll
                foll._followers[self._name] = self
                print(f"{self._name} started following {foll._name}")
                return True
        return False

    # Unfollow other users
    def unfollow(self, foll: 'User') -> bool:
        if self._logged:
            if foll._name in self._following:
                del self._following[foll._name]
                del foll._followers[self._name]
                print(f"{self._name} unfollowed {foll._name}")
                return True
        return False

    def add_notif(self, notif: str) -> None:
        self._notif.append(notif)

    def get_name(self) -> str:
        return self._name

    def publish_post(self, typ: str, *data) -> Post:
        p1 = self._factory.generate_post(self, typ, data)
        self._posts.append(p1)
        return p1

    def print_notifications(self):
        print(f"{self._name}'s notifications:")
        for notif in self._notif:
            print(notif)
