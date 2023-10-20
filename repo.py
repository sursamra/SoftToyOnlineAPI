from .db_repo import ToyDBRepository, db
from .mem_repo import ToyMeMRepository


def create_repository(app):
    repository_choice = app.config.get('REPOSITORY')
    if repository_choice == 'sqlite':
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return ToyDBRepository()
    elif repository_choice == 'memory':
        return ToyMeMRepository()
    else:
        raise ValueError("Invalid repository choice in configuration")
