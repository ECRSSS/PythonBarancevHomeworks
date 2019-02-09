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
