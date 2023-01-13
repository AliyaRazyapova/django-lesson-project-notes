from django.db.models import Func, F
from django.db.models.expressions import RawSQL


class SplitPartFunc(Func):
    # split_part("web_user"."email", '@', 2)
    def __init__(self, field_name: str, delimiter: str, number: int):
        super().__init__(
            F(field_name),
            RawSQL("%s", [delimiter]),
            RawSQL("%s", [number]),
            function='split_part'
        )
