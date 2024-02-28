from Observer import Observer

# Observer as follower
class FollowObserver(Observer):
    def __init__(self, user):
        self._user = user

    # Updating the follower
    def update(self, other):
        str = other.get_name()
        self._user.add_notif(f'{str} has a new post')
