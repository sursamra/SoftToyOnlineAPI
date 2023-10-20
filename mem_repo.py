from dataclasses import dataclass


@dataclass
class ToyData:
    id: int
    name: str
    description: str
    price: float
    quantity: int

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity
        }


class ToyMeMRepository:
    def __init__(self):
        self.toys = {
            1: ToyData(1, name='Inky', description='soft', price=10, quantity=100),
            2: ToyData(2, name='Tumbleuft', description='medium soft', price=20, quantity=200),
            3: ToyData(3, name='Harkle', description='very soft', price=30, quantity=300),
            4: ToyData(4, name='Bartholomew', description='bear bed time', price=40, quantity=400),
            5: ToyData(5, name='Ronnie', description='rock hopper penguin', price=50, quantity=500)
        }
        self.current_id = 4

    def get_toys(self):
        return list(self.toys.values())

    def add_toy(self, toy):
        if id not in toy:
            toy['id'] = self.current_id
        new_toy = ToyData(**toy)
        self.toys[self.current_id] = new_toy
        self.current_id += 1
        return new_toy

    def update_toy(self, toy_id, updated_toy):
        if toy_id not in self.toys:
            return None
        toy_to_update = self.toys[toy_id]
        for key, value in updated_toy.items():
            setattr(toy_to_update, key, value)
        return toy_to_update

    def delete_toy(self, toy_id):
        if toy_id not in self.toys:
            return None
        del_toy = self.toys.pop(toy_id)
        return del_toy
