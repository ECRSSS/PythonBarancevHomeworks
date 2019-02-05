from sys import maxsize


def list_sort(list):
    def id_or_max(obj):
        if obj.elm_id:
            return int(obj.elm_id)
        else:
            return maxsize

    sorted(list, key=id_or_max)
