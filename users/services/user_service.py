from django.db.models import Q

from users.models import CustomUser


class UserService:

    def __init__(self):
        self.model = CustomUser.objects

    def get_user_with_relation(self, user_id):
        return self.model.prefetch_related(
            'ratings',
            'history'
        ).filter(id=user_id).first()

    def get_user_by_TUID(self, id):
        return self.model.get(Q(tuid=id) | Q(id=id))

    def create_user_name_and_TUID(self, username, tuid):
        return self.model.create_user(username=username, tuid=tuid)
