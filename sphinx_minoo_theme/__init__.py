import os

"""SphinxMinooTheme.
https://github.com/saeiddrv/SphinxMinooTheme.
"""


class MinooVersion():
    major = "1"
    minor = "0"
    micro = "1"
    level = "Stable"
    release = r"2024/04/06"

    def info(self):
        info = ".".join([self.major, self.minor, self.micro])
        return info

    def info_full(self):
        info = "major   = " + self.major + "\n" + \
               "minor   = " + self.minor + "\n" + \
               "micro   = " + self.micro + "\n" + \
               "level   = " + self.level + "\n" + \
               "release = " + self.release + "\n"
        return info


__version__ = MinooVersion()


# From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir
