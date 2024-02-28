from Post import Post


class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)
        self._text = text
        return

    def __str__(self):
        return (f"{self._user.get_name()} published a post:\n"
                f'"{self._text}"\n')
