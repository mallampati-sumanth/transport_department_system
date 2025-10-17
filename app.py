"""Main application module for Transport Department System."""
from flask import Flask, jsonify
from config import config_by_name
from models import db, Vehicle, Driver, Route, License

def create_app(config_name='default'):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Register routes
    @app.route('/')
    def index():
        """Home endpoint."""
        return jsonify({
            'message': 'Transport Department System API',
            'version': '1.0.0',
            'endpoints': {
                'vehicles': '/api/vehicles',
                'drivers': '/api/drivers',
                'routes': '/api/routes',
                'licenses': '/api/licenses'
            }
        })
    
    @app.route('/api/vehicles')
    def get_vehicles():
        """Get all vehicles."""
        vehicles = Vehicle.query.all()
        return jsonify([{
            'id': v.id,
            'registration_number': v.registration_number,
            'vehicle_type': v.vehicle_type,
            'manufacturer': v.manufacturer,
            'model': v.model,
            'status': v.status
        } for v in vehicles])
    
    @app.route('/api/drivers')
    def get_drivers():
        """Get all drivers."""
        drivers = Driver.query.all()
        return jsonify([{
            'id': d.id,
            'name': d.name,
            'license_number': d.license_number,
            'license_type': d.license_type,
            'status': d.status
        } for d in drivers])
    
    @app.route('/api/routes')
    def get_routes():
        """Get all routes."""
        routes = Route.query.all()
        return jsonify([{
            'id': r.id,
            'route_number': r.route_number,
            'start_location': r.start_location,
            'end_location': r.end_location,
            'distance_km': r.distance_km,
            'status': r.status
        } for r in routes])
    
    @app.route('/api/licenses')
    def get_licenses():
        """Get all licenses."""
        licenses = License.query.all()
        return jsonify([{
            'id': l.id,
            'license_number': l.license_number,
            'license_type': l.license_type,
            'holder_name': l.holder_name,
            'status': l.status
        } for l in licenses])
    
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True, host='0.0.0.0', port=5000)
