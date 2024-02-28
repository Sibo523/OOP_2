

class Post:

    def __init__(self, user):
        self._user = user
        self._likes = 0
        self._liked_by = []
        self._comments = {}     # User x comment dict
        return

    def comment(self, user, comment):
        if user.is_logged():
            self._comments[user] = comment
            if not self._user.get_name() == user.get_name():
                print(f"notification to {self._user.get_name()}: {user.get_name()} commented on your post: {comment}")
                self._user.add_notif(f"{user.get_name()} commented on your post")
            return True
        raise Exception('user not logged in')

    def like(self, user):
        if user.is_logged():
            if not self._is_liked_by(user):
                if not self._user.get_name() == user.get_name():
                    print(f"notification to {self._user.get_name()}: {user.get_name()} liked your post")
                    self._user.add_notif(f"{user.get_name()} liked your post")
                self._likes += 1
                self._liked_by.append(user)

    def _is_liked_by(self, user):
        if user in self._liked_by:
            return True
        return False

    def __str__(self):
        pass
