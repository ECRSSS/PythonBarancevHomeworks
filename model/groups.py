# -*- coding: utf-8 -*-


class Group:
    def __init__(self, name, header, footer, elm_id):
        self.name = name
        self.header = header
        self.footer = footer
        self.elm_id = elm_id

    def __eq__(self, o: object) -> bool:
        return (self.elm_id is None or o.elm_id is None or self.elm_id == o.elm_id) \
               and self.name == o.name

    def __repr__(self):
        return str(self.elm_id) + " " + self.name + " " + str(self.header) + " " + str(self.footer)

    def __lt__(self, other):
        return self.elm_id < other.elm_id
