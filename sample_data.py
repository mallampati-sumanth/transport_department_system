"""Sample data for testing the Transport Department System."""
from datetime import date, datetime, timedelta
from app import create_app
from models import db, Vehicle, Driver, Route, License

def create_sample_data():
    """Create sample data for development and testing."""
    app = create_app('development')
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create sample vehicles
        vehicles = [
            Vehicle(
                registration_number='BUS-001',
                vehicle_type='Bus',
                manufacturer='Mercedes',
                model='Sprinter',
                year=2022,
                capacity=25,
                status='active'
            ),
            Vehicle(
                registration_number='BUS-002',
                vehicle_type='Bus',
                manufacturer='Toyota',
                model='Coaster',
                year=2021,
                capacity=20,
                status='active'
            ),
            Vehicle(
                registration_number='TRUCK-001',
                vehicle_type='Truck',
                manufacturer='Ford',
                model='F-350',
                year=2020,
                capacity=5000,
                status='active'
            ),
            Vehicle(
                registration_number='VAN-001',
                vehicle_type='Van',
                manufacturer='Volkswagen',
                model='Transporter',
                year=2023,
                capacity=12,
                status='maintenance'
            )
        ]
        
        for vehicle in vehicles:
            db.session.add(vehicle)
        
        # Create sample drivers
        drivers = [
            Driver(
                name='John Smith',
                license_number='DL-001234',
                license_type='B',
                phone='555-1001',
                email='john.smith@transport.com',
                address='123 Main Street, City',
                hire_date=date(2020, 1, 15),
                status='active'
            ),
            Driver(
                name='Sarah Johnson',
                license_number='DL-002345',
                license_type='B',
                phone='555-1002',
                email='sarah.johnson@transport.com',
                address='456 Oak Avenue, City',
                hire_date=date(2019, 6, 1),
                status='active'
            ),
            Driver(
                name='Michael Chen',
                license_number='DL-003456',
                license_type='C',
                phone='555-1003',
                email='michael.chen@transport.com',
                address='789 Pine Road, City',
                hire_date=date(2021, 3, 10),
                status='active'
            ),
            Driver(
                name='Emma Davis',
                license_number='DL-004567',
                license_type='B',
                phone='555-1004',
                email='emma.davis@transport.com',
                address='321 Elm Street, City',
                hire_date=date(2022, 9, 5),
                status='on_leave'
            )
        ]
        
        for driver in drivers:
            db.session.add(driver)
        
        db.session.commit()
        
        # Create sample routes (assign vehicles and drivers)
        routes = [
            Route(
                route_number='R-001',
                start_location='City Center',
                end_location='Airport',
                distance_km=25.5,
                estimated_duration_minutes=45,
                vehicle_id=1,
                driver_id=1,
                status='active'
            ),
            Route(
                route_number='R-002',
                start_location='North Station',
                end_location='South Terminal',
                distance_km=18.3,
                estimated_duration_minutes=35,
                vehicle_id=2,
                driver_id=2,
                status='active'
            ),
            Route(
                route_number='R-003',
                start_location='Industrial Zone',
                end_location='Port',
                distance_km=42.0,
                estimated_duration_minutes=60,
                vehicle_id=3,
                driver_id=3,
                status='active'
            ),
            Route(
                route_number='R-004',
                start_location='University',
                end_location='Shopping District',
                distance_km=12.5,
                estimated_duration_minutes=25,
                vehicle_id=None,
                driver_id=None,
                status='inactive'
            )
        ]
        
        for route in routes:
            db.session.add(route)
        
        # Create sample licenses
        today = date.today()
        licenses = [
            License(
                license_number='VL-BUS-001',
                license_type='Vehicle License',
                holder_name='BUS-001',
                issue_date=date(2022, 1, 1),
                expiry_date=date(2025, 1, 1),
                status='valid'
            ),
            License(
                license_number='VL-BUS-002',
                license_type='Vehicle License',
                holder_name='BUS-002',
                issue_date=date(2021, 6, 1),
                expiry_date=date(2024, 6, 1),
                status='valid'
            ),
            License(
                license_number='OP-2024-001',
                license_type='Operating Permit',
                holder_name='Transport Department',
                issue_date=date(2024, 1, 1),
                expiry_date=date(2025, 1, 1),
                status='valid'
            ),
            License(
                license_number='DL-RENEW-001',
                license_type='Driver License',
                holder_name='John Smith',
                issue_date=date(2020, 1, 1),
                expiry_date=today + timedelta(days=20),
                status='valid'
            )
        ]
        
        for license in licenses:
            db.session.add(license)
        
        db.session.commit()
        
        print("Sample data created successfully!")
        print(f"- {len(vehicles)} vehicles")
        print(f"- {len(drivers)} drivers")
        print(f"- {len(routes)} routes")
        print(f"- {len(licenses)} licenses")

if __name__ == '__main__':
    create_sample_data()
