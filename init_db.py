#!/usr/bin/env python3
"""Initialize the database for Transport Department System."""

import sys
from app import create_app
from models import db

def init_database(environment='development'):
    """Initialize database tables.
    
    Args:
        environment: Configuration environment (development, testing, production)
    """
    print(f"Initializing database for {environment} environment...")
    
    try:
        app = create_app(environment)
        
        with app.app_context():
            # Create all tables
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Print table information
            tables = db.metadata.tables.keys()
            print(f"Created {len(tables)} tables:")
            for table in tables:
                print(f"  - {table}")
                
        return 0
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return 1

if __name__ == '__main__':
    environment = sys.argv[1] if len(sys.argv) > 1 else 'development'
    sys.exit(init_database(environment))
