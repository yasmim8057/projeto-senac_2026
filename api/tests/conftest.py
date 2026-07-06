import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import Session 

from viajei_api.app import app

from viajei_api.models import table_registry

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def session():
    engine = create_engine('sql://:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

        table_registry.metadata.drop_all(engine)
        engine.dispose()
        
        @pytest.fixture 
        def user(session):
            user = user(
                email ="example@example.com", 
                                                                                                                                                                                                                                                                                                                                                                               
            )