"""Blog Migration."""

from masoniteorm.migrations import Migration


class Blog(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id")
            table.string("title")
            table.string("author")
            table.string("article")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")
