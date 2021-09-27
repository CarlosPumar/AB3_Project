from ..models import Relation


def get_list():
    relations = Relation.objects.all()
    return relations
