"""Unit tests for Transport Department System models."""
import pytest
from datetime import date, datetime
from app import create_app
from models import db, Vehicle, Driver, Route, License

@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

class TestVehicleModel:
    """Tests for Vehicle model."""
    
    def test_create_vehicle(self, app):
        """Test creating a vehicle."""
        with app.app_context():
            vehicle = Vehicle(
                registration_number='ABC-1234',
                vehicle_type='Bus',
                manufacturer='Toyota',
                model='Coaster',
                year=2020,
                capacity=25,
                status='active'
            )
            db.session.add(vehicle)
            db.session.commit()
            
            assert vehicle.id is not None
            assert vehicle.registration_number == 'ABC-1234'
            assert vehicle.vehicle_type == 'Bus'
            assert vehicle.status == 'active'
    
    def test_vehicle_unique_registration(self, app):
        """Test that registration numbers must be unique."""
        with app.app_context():
            vehicle1 = Vehicle(
                registration_number='XYZ-5678',
                vehicle_type='Truck',
                manufacturer='Ford',
                model='F-150'
            )
            db.session.add(vehicle1)
            db.session.commit()
            
            vehicle2 = Vehicle(
                registration_number='XYZ-5678',
                vehicle_type='Car',
                manufacturer='Honda',
                model='Civic'
            )
            db.session.add(vehicle2)
            
            with pytest.raises(Exception):
                db.session.commit()

class TestDriverModel:
    """Tests for Driver model."""
    
    def test_create_driver(self, app):
        """Test creating a driver."""
        with app.app_context():
            driver = Driver(
                name='John Doe',
                license_number='DL-123456',
                license_type='B',
                phone='555-1234',
                email='john@example.com',
                status='active'
            )
            db.session.add(driver)
            db.session.commit()
            
            assert driver.id is not None
            assert driver.name == 'John Doe'
            assert driver.license_number == 'DL-123456'
            assert driver.status == 'active'
    
    def test_driver_unique_license(self, app):
        """Test that license numbers must be unique."""
        with app.app_context():
            driver1 = Driver(
                name='Jane Smith',
                license_number='DL-999999',
                license_type='A'
            )
            db.session.add(driver1)
            db.session.commit()
            
            driver2 = Driver(
                name='Bob Jones',
                license_number='DL-999999',
                license_type='B'
            )
            db.session.add(driver2)
            
            with pytest.raises(Exception):
                db.session.commit()

class TestRouteModel:
    """Tests for Route model."""
    
    def test_create_route(self, app):
        """Test creating a route."""
        with app.app_context():
            route = Route(
                route_number='R-001',
                start_location='City Center',
                end_location='Airport',
                distance_km=25.5,
                estimated_duration_minutes=45,
                status='active'
            )
            db.session.add(route)
            db.session.commit()
            
            assert route.id is not None
            assert route.route_number == 'R-001'
            assert route.start_location == 'City Center'
            assert route.end_location == 'Airport'
            assert route.distance_km == 25.5

class TestLicenseModel:
    """Tests for License model."""
    
    def test_create_license(self, app):
        """Test creating a license."""
        with app.app_context():
            license = License(
                license_number='LIC-2024-001',
                license_type='Operating Permit',
                holder_name='Transport Department',
                issue_date=date(2024, 1, 1),
                expiry_date=date(2025, 1, 1),
                status='valid'
            )
            db.session.add(license)
            db.session.commit()
            
            assert license.id is not None
            assert license.license_number == 'LIC-2024-001'
            assert license.status == 'valid'

class TestAPI:
    """Tests for API endpoints."""
    
    def test_index_endpoint(self, client):
        """Test the index endpoint."""
        response = client.get('/')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data
        assert 'Transport Department System' in data['message']
    
    def test_vehicles_endpoint(self, client, app):
        """Test the vehicles endpoint."""
        with app.app_context():
            vehicle = Vehicle(
                registration_number='TEST-001',
                vehicle_type='Bus',
                manufacturer='Mercedes',
                model='Sprinter'
            )
            db.session.add(vehicle)
            db.session.commit()
        
        response = client.get('/api/vehicles')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) > 0
    
    def test_drivers_endpoint(self, client):
        """Test the drivers endpoint."""
        response = client.get('/api/drivers')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
    
    def test_routes_endpoint(self, client):
        """Test the routes endpoint."""
        response = client.get('/api/routes')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
    
    def test_licenses_endpoint(self, client):
        """Test the licenses endpoint."""
        response = client.get('/api/licenses')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
