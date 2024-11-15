from users.models import Cars


class CarsService:

    def __init__(self):
        self.model = Cars

    def create_car(self, data):
        return self.model.objects.create(**data)

    def check_car_by_user_id_and_number(self, user_id, number):
        return self.model.objects.filter(user_id=user_id, number=number).first()

    def get_cars_by_user_id(self, user_id):
        return self.model.objects.filter(user_id=user_id).all()
