from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import QuerySet


class MyJsonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return tuple(obj)
        # elif isinstance(obj, Instagram):
        #     return {'id': obj.id, 'title': obj.title, 'content': obj.content}
        elif hasattr(obj, 'as_dict'):
            return obj.as_dict()

        return super().default(obj)
