#!/usr/bin/python3
"""Dragon class"""


class SwimMixin():
    """swiming class"""

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """flying class"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""

    def roar(self):
        print("The dragon roars!")
