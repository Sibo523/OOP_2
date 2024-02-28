from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost
from Post import Post


class PostFactory:
    def __init__(self):
        pass

    def generate_post(self, user, typ: str, *data) -> Post:
        if typ == "Text":
            print(f'{user.get_name()} published a post:\n"{data[0][0]}"\n')
            return TextPost(user, data[0][0])
        elif typ == "Image":
            print(f"{user.get_name()} posted a picture\n")
            return ImagePost(user, data[0][0])
        elif typ == "Sale":
            print(f"{user.get_name()} posted a product for sale:\n"
                  f"For sale! {data[0][0]}, price: {data[0][1]}, pickup from: {data[0][2]}\n")
            return SalePost(user, data[0][0], data[0][1], data[0][2])

