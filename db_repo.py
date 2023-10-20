from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Toy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity
        }


class ToyDBRepository:
    def get_toys(self):
        return Toy.query.all()

    def add_toy(self, toy_data):
        new_toy = Toy(name=toy_data['name'], description=toy_data['description'], price=toy_data['price'],
                      quantity=toy_data['quantity'])
        db.session.add(new_toy)
        db.session.commit()
        return new_toy

    def update_toy(self, toy_id, updated_toy_data):
        toy_to_update = Toy.query.get(toy_id)
        if toy_to_update is None:
            return None

        for key, value in updated_toy_data.items():
            setattr(toy_to_update, key, value)

        db.session.commit()
        return toy_to_update

    def delete_toy(self, toy_id):
        toy_to_delete = Toy.query.get(toy_id)
        if toy_to_delete is None:
            return None

        db.session.delete(toy_to_delete)
        db.session.commit()
        return toy_to_delete
