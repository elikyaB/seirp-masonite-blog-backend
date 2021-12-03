""" A BlogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Blog import Blog


class BlogController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request:Request):
        print('wazzup')
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", TodoController)
        """
        id = self.request.param("id")
        return Blog.find(id)

    def index(self):
        print('hi')
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", BlogController)
        """
        return Blog.all()

    def whatev(self):
        return "cheese"

    def create(self):
        print('hi')
        title = self.request.input("title")
        author = self.request.input("author")
        article = self.request.input("article")
        blog = Blog.create({"title": title, "author": author, "article": article})
        return blog

    def update(self):
        title = self.request.input("title")
        author = self.request.input("author")
        article = self.request.input("article")
        id = self.request.param("id")
        blog = Blog.where("id", id).update({"title": title, "author": author, "article": article})
        return Blog.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        blog = Blog.where("id", id).get()
        Blog.where("id", id).delete()
        return blog