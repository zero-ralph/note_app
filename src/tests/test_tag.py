from fastapi.testclient import TestClient
from src.main import app


tag_client = TestClient(app)

# Integration Testing
class TestIntegrationTags:

    def test_tag_listing(self):
        response = tag_client.get("/api/tags/")
        assert response.status_code == 200

    def test_tag_create(self):
        response = tag_client.post("/api/tags/")
        assert response.status_code == 200

    def test_tag_retrieved(self):
        response = tag_client.get("/api/tags/1")
        assert response.status_code == 200

    def test_tag_update(self):
        response = tag_client.put("/api/tags/1")
        assert response.status_code == 200

    def test_tag_delete(self):
        response = tag_client.delete("/api/tags/1")
        assert response.status_code == 200

    
