class Comment:
    def __init__(self, user_name, content , likes=0):
        self.user_name = user_name
        self.content = content
        self.likes = likes


comment = Comment("user one", "I like this book")
print(comment.user_name)
print(comment.content)
print(comment.likes)