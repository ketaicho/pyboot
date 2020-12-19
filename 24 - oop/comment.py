class Comment:
    def __init__(self, username, text="", likes=0):
        self.username = username
        self.text = text
        self.likes = likes

com = Comment("davery134", "lol you're so silly!")
print(com.likes)

