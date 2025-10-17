"""Database models for Transport Department System."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicle(db.Model):
    """Vehicle model representing vehicles in the transport department."""
    __tablename__ = 'vehicles'
    
    id = db.Column(db.Integer, primary_key=True)
    registration_number = db.Column(db.String(20), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)  # Bus, Truck, Car, etc.
    manufacturer = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    capacity = db.Column(db.Integer)  # Passenger capacity or load capacity
    status = db.Column(db.String(20), default='active')  # active, maintenance, retired
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    routes = db.relationship('Route', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return f'<Vehicle {self.registration_number}>'

class Driver(db.Model):
    """Driver model representing drivers in the transport department."""
    __tablename__ = 'drivers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(20), unique=True, nullable=False)
    license_type = db.Column(db.String(10), nullable=False)  # A, B, C, etc.
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    hire_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')  # active, on_leave, retired
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    routes = db.relationship('Route', backref='driver', lazy=True)
    
    def __repr__(self):
        return f'<Driver {self.name}>'

class Route(db.Model):
    """Route model representing transport routes."""
    __tablename__ = 'routes'
    
    id = db.Column(db.Integer, primary_key=True)
    route_number = db.Column(db.String(20), unique=True, nullable=False)
    start_location = db.Column(db.String(100), nullable=False)
    end_location = db.Column(db.String(100), nullable=False)
    distance_km = db.Column(db.Float)
    estimated_duration_minutes = db.Column(db.Integer)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    status = db.Column(db.String(20), default='active')  # active, inactive, suspended
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Route {self.route_number}: {self.start_location} to {self.end_location}>'

class License(db.Model):
    """License model for tracking license renewals and compliance."""
    __tablename__ = 'licenses'
    
    id = db.Column(db.Integer, primary_key=True)
    license_number = db.Column(db.String(20), unique=True, nullable=False)
    license_type = db.Column(db.String(50), nullable=False)  # Vehicle, Driver, Operating Permit
    holder_name = db.Column(db.String(100), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='valid')  # valid, expired, suspended, revoked
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<License {self.license_number}>'
