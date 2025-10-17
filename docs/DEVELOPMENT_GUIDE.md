# Development Guide - Transport Department System

## Project Overview

The Transport Department System is a web-based application designed to manage all aspects of a transportation department's operations. The system is developed using Scrum methodology with iterative sprints.

## System Architecture

### Technology Stack
- **Backend Framework**: Flask (Python)
- **Database ORM**: SQLAlchemy
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Testing Framework**: pytest
- **Methodology**: Scrum Agile

### Application Structure

```
transport_department_system/
├── app.py                      # Main Flask application
├── models.py                   # Database models (Vehicle, Driver, Route, License)
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── setup.sh                    # Setup script
├── sample_data.py             # Sample data generator
├── tests/                      # Unit tests
│   ├── __init__.py
│   └── test_models.py
├── docs/                       # Documentation
│   ├── API_DOCUMENTATION.md   # API reference
│   ├── PRODUCT_BACKLOG.md     # Product backlog with user stories
│   ├── SPRINT_PLANNING.md     # Sprint planning details
│   └── SCRUM_TEAM.md          # Team roles and responsibilities
└── README.md                   # Project overview
```

## Core Features

### 1. Vehicle Management
- Track vehicle inventory (buses, trucks, vans, cars)
- Manage vehicle details (registration, manufacturer, model, capacity)
- Monitor vehicle status (active, maintenance, retired)
- Maintain vehicle history

### 2. Driver Management
- Maintain driver records
- Track driver licenses and certifications
- Monitor license expiry dates
- Manage driver assignments

### 3. Route Management
- Create and manage transportation routes
- Assign vehicles and drivers to routes
- Track route details (distance, duration)
- Monitor route status

### 4. License & Compliance
- Track all licenses (vehicle licenses, driver licenses, operating permits)
- Monitor expiry dates
- Generate compliance reports
- Alert system for upcoming renewals

## Database Schema

### Vehicle Table
- `id`: Primary key
- `registration_number`: Unique identifier
- `vehicle_type`: Type of vehicle (Bus, Truck, etc.)
- `manufacturer`: Vehicle manufacturer
- `model`: Vehicle model
- `year`: Manufacturing year
- `capacity`: Passenger/load capacity
- `status`: Current status
- `created_at`, `updated_at`: Timestamps

### Driver Table
- `id`: Primary key
- `name`: Driver full name
- `license_number`: Unique license number
- `license_type`: License category (A, B, C, etc.)
- `phone`, `email`, `address`: Contact information
- `hire_date`: Date of hiring
- `status`: Current status
- `created_at`, `updated_at`: Timestamps

### Route Table
- `id`: Primary key
- `route_number`: Unique route identifier
- `start_location`: Starting point
- `end_location`: Destination
- `distance_km`: Route distance
- `estimated_duration_minutes`: Expected duration
- `vehicle_id`: Foreign key to Vehicle
- `driver_id`: Foreign key to Driver
- `status`: Current status
- `created_at`, `updated_at`: Timestamps

### License Table
- `id`: Primary key
- `license_number`: Unique license number
- `license_type`: Type of license
- `holder_name`: License holder
- `issue_date`: Date issued
- `expiry_date`: Expiration date
- `status`: Current status
- `created_at`, `updated_at`: Timestamps

## Development Workflow

### 1. Sprint Planning
- Conducted at the beginning of each 2-week sprint
- Product Owner presents prioritized backlog items
- Team selects user stories to complete
- Stories are broken down into tasks
- Team commits to Sprint Goal

### 2. Daily Standup
- 15-minute meeting at 9:00 AM
- Each team member answers:
  - What did I complete yesterday?
  - What will I work on today?
  - Are there any blockers?

### 3. Development Process
1. Pick a task from Sprint Backlog
2. Create feature branch: `git checkout -b feature/task-name`
3. Implement the feature with TDD approach:
   - Write failing test
   - Implement minimum code to pass
   - Refactor
4. Run tests: `pytest tests/`
5. Commit changes with meaningful message
6. Push and create Pull Request
7. Code review by team member
8. Merge to main after approval

### 4. Sprint Review
- Conducted at end of sprint
- Demo completed features to stakeholders
- Gather feedback
- Update Product Backlog based on feedback

### 5. Sprint Retrospective
- Team reflects on the sprint
- Discuss what went well
- Identify improvements
- Create action items for next sprint

## Testing Strategy

### Unit Tests
- Test individual functions and methods
- Located in `tests/` directory
- Run with: `pytest tests/`
- Aim for 80%+ code coverage

### Integration Tests
- Test API endpoints
- Test database operations
- Verify module interactions

### Manual Testing
- UI testing (when frontend is added)
- End-to-end user flows
- Browser compatibility

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment support

### Installation
```bash
# Clone repository
git clone https://github.com/mallampati-sumanth/transport_department_system.git
cd transport_department_system

# Run setup script
./setup.sh

# Or manually:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Application
```bash
# Activate virtual environment
source venv/bin/activate

# Run application
python app.py

# Application will be available at http://localhost:5000
```

### Running Tests
```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=.

# Run specific test file
pytest tests/test_models.py -v
```

### Loading Sample Data
```bash
# Activate virtual environment
source venv/bin/activate

# Load sample data
python sample_data.py
```

## API Endpoints

See [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) for complete API reference.

Basic endpoints:
- `GET /` - API information
- `GET /api/vehicles` - List all vehicles
- `GET /api/drivers` - List all drivers
- `GET /api/routes` - List all routes
- `GET /api/licenses` - List all licenses

## Contributing

### Code Style
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Git Workflow
1. Create feature branch from main
2. Make changes in small, logical commits
3. Write/update tests
4. Ensure all tests pass
5. Create Pull Request
6. Address code review feedback
7. Merge after approval

### Definition of Done
Before marking a user story as complete:
- [ ] Code is written and follows style guide
- [ ] Unit tests are written and passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Feature tested in development
- [ ] No critical bugs

## Future Enhancements

### Sprint 2 (Planned)
- CRUD operations for all entities
- Advanced filtering and search
- User authentication and authorization

### Sprint 3 (Planned)
- Dashboard with analytics
- Reporting system
- Email notifications for license expiry

### Sprint 4 (Planned)
- Frontend UI with React/Vue.js
- Real-time updates with WebSockets
- Mobile app support

## Troubleshooting

### Common Issues

**Issue**: Database file not found
**Solution**: Run `python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.create_all()"`

**Issue**: Import errors
**Solution**: Ensure virtual environment is activated and dependencies are installed

**Issue**: Port already in use
**Solution**: Kill process on port 5000 or change port in app.py

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Scrum Guide](https://scrumguides.org/)

## License

This project is developed for educational purposes as part of a Scrum-based software development initiative.
