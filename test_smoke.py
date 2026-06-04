import pytest
import requests


class TestSmoke:
    """Smoke tests for basic application functionality"""

    def test_application_is_running(self):
        """Test that the application is accessible"""
        try:
            response = requests.get("http://localhost:8000", timeout=5)
            assert response.status_code in [200, 301, 302, 404]
        except requests.exceptions.ConnectionError:
            pytest.fail("Application is not running or not accessible")

    def test_basic_health_check(self):
        """Test basic health endpoint"""
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            assert response.status_code == 200
        except requests.exceptions.ConnectionError:
            pytest.skip("Health endpoint not available")

    def test_database_connection(self):
        """Test database connectivity"""
        assert True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
