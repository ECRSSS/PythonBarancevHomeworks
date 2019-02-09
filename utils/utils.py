from random import randrange
from sys import maxsize


def list_sort(list):
    def id_or_max(obj):
        if obj.elm_id:
            return int(obj.elm_id)
        else:
            return maxsize

    sorted(list, key=id_or_max)


def get_random_index_from_list(list_of_elements):
    if len(list_of_elements) == 0:
        index = 0
    else:
        index = randrange(len(list_of_elements))
    return index


def clear(string_to_clear):
    import string

    class Del:
        def __init__(self, keep=string.digits):
            self.comp = dict((ord(c), c) for c in keep)

        def __getitem__(self, k):
            return self.comp.get(k)

    d = Del()
    x = str(string_to_clear)
    return x.translate(d)
