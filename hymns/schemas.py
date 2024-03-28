from ninja import ModelSchema
from .models import Hymn


class HymnSchema(ModelSchema):
    class Meta:
        model = Hymn
        fields = "__all__"