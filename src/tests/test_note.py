import pytest
from src.config.settings import Settings
from src.config.database import configure_database, SESSIONLOCAL
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="module")
def db_session():
    # Setup database session
    settings = Settings()  # Your settings configuration
    configure_database(settings)

    db = SESSIONLOCAL()  # This should work now if SESSIONLOCAL is properly initialized
    yield db
    db.close()

@pytest.fixture(scope="module")
def note_client():
    return TestClient(app)


# Integration Testing
class TestIntegrationNotes:

    def test_note_listing(self, note_client, db_session):
        response = note_client.get("/api/notes/")
        assert response.status_code == 200

    def test_note_create(self, note_client, db_session):
        new_note = {
            "title": "Guitar Pedal",
            "description": "All about guitar pedal and how they work"
        }
        response = note_client.post("/api/notes/", json=new_note)
        assert response.status_code == 201
        

    def test_note_retrieved(self, note_client, db_session):
        response = note_client.get("/api/notes/1")
        assert response.status_code == 200

    def test_note_update(self, note_client, db_session):
        response = note_client.put("/api/notes/1")
        assert response.status_code == 200

    def test_note_delete(self, note_client, db_session):
        response = note_client.delete("/api/notes/1")
        assert response.status_code == 200

    
