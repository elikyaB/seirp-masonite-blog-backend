"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({
            "title": "The Life And Times Of Charlie Sheen",
            "author": "Not Charlie Sheen",
            "article": "Who's that?"
            })
        Blog.create({
            "title": "Why Arcane Is Actually A Bad Show",
            "author": "me",
            "article": "Silco is a pedo"
            })
        Blog.create({
            "title": "Why LOTR Wasn't Racist But Its Derivatives Are",
            "author": "The Hot-Take Meme Machine",
            "article": "LOTR was an allegory to WWII, in a time where the Europeans believed each other to be foundationally incompatible. Hence the use of fantasy races that were distinct but they learn to combine forces to overcome a greater evil. That was progressive for it's time. But postmodern Tolkien clones don't have that advantage, so at minimum they perpetuate the idea of genetically meaningful racial divisions that we know to not exist. It's probably why the fantasy genre in general appeals to right-wing Christian types. What was once progressive has stagnated through cliche regurgitations to become regressive."
            })
        
