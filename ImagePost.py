from Post import Post
from matplotlib import pyplot as plt
from matplotlib import image as mpimg


class ImagePost(Post):
    def __init__(self, user, image: str):
        super().__init__(user)
        self._image = image

    def display(self):
        plt.title(f"{self._user.get_name()}'s picture")
        image = mpimg.imread(self._image)
        plt.imshow(image)
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self._user.get_name()} posted a picture\n"
