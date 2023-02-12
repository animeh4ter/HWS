def add_title(title: str):
    def deco(method):
        def wrapper(self, *args):
            print(title.center(50, "="))
            return method(self, *args)
        return wrapper
    return deco


class UserInterface:

    @add_title(" User input ")
    def wait_user_answer(self):
        print("Actions with news:")
        print("1 - Create article"
              "\n2 - View all articles"
              "\n3 - View certain article"
              "\n4 - Delete article")
        print("q - Quit program")
        user_answer = input("Choose action: ")
        return user_answer

    @add_title(" Creating article ")
    def add_user_article(self):
        dict_article = {"name": None,
                        "author": None,
                        "pages": None,
                        "description": None
                        }
        for key in dict_article:
            dict_article[key] = input(f"Type {key}: ")
        return dict_article

    @add_title(" Articles list ")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
