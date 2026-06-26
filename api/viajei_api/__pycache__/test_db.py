from sqlalchemy import select 
from viajei_api.models import user

def test_create_user(session):
    new_user = User('yasmim@test.test', 'senha123')

    session.add(new_user)
    session.commit()

    user = session.scalar(select(user).where(user.email == 'yasmim@test.test'))

    assert user.email == 'yasmim@test.test' 