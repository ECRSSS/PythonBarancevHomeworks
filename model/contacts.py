# -*- coding: utf-8 -*-


class Contact:

    def __init__(self, first_name, middle_name, last_name, elm_id):
        self.elm_id = elm_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def __eq__(self, o: object) -> bool:
        return (self.elm_id is None or o.elm_id is None or self.elm_id == o.elm_id) \
               and self.middle_name == o.middle_name and self.first_name == o.first_name and self.last_name == o.last_name

    def __repr__(self):
        return str(self.elm_id) + " " + self.first_name + " " + self.middle_name + " " + self.last_name

    def __lt__(self, other):
        return self.elm_id < other.elm_id
