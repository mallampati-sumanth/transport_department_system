# Quick Start Guide - Transport Department System

## Get Started in 5 Minutes

### Step 1: Clone the Repository
```bash
git clone https://github.com/mallampati-sumanth/transport_department_system.git
cd transport_department_system
```

### Step 2: Set Up the Environment
```bash
# Option A: Use the setup script (recommended)
./setup.sh

# Option B: Manual setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Initialize the Database
```bash
source venv/bin/activate  # If not already activated

# Create database tables
python -c "from app import create_app; from models import db; app = create_app('development'); app.app_context().push(); db.create_all(); print('Database initialized!')"

# (Optional) Load sample data
python sample_data.py
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 5: Test the API
Open your browser or use curl to test the endpoints:

```bash
# Get API information
curl http://localhost:5000/

# Get all vehicles
curl http://localhost:5000/api/vehicles

# Get all drivers
curl http://localhost:5000/api/drivers

# Get all routes
curl http://localhost:5000/api/routes

# Get all licenses
curl http://localhost:5000/api/licenses
```

## Project Structure Overview

```
transport_department_system/
├── app.py                          # Main Flask application
├── models.py                       # Database models
├── config.py                       # Configuration
├── requirements.txt                # Dependencies
├── README.md                       # Project overview
│
├── docs/                          # Documentation
│   ├── QUICK_START.md            # This file
│   ├── DEVELOPMENT_GUIDE.md      # Detailed development guide
│   ├── API_DOCUMENTATION.md      # API reference
│   ├── PRODUCT_BACKLOG.md        # Scrum product backlog
│   ├── SPRINT_PLANNING.md        # Sprint planning
│   └── SCRUM_TEAM.md             # Team roles
│
├── tests/                         # Unit tests
│   ├── __init__.py
│   └── test_models.py
│
├── setup.sh                       # Setup script
├── sample_data.py                 # Sample data generator
└── verify_setup.py                # Verification script
```

## Available API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and endpoints |
| `/api/vehicles` | GET | List all vehicles |
| `/api/drivers` | GET | List all drivers |
| `/api/routes` | GET | List all routes |
| `/api/licenses` | GET | List all licenses |

## Database Models

### Vehicle
Manages transport vehicles (buses, trucks, vans)
- Registration number, type, manufacturer, model
- Capacity, status, timestamps

### Driver
Manages driver information
- Name, license details, contact information
- Hire date, status, timestamps

### Route
Manages transportation routes
- Route number, locations, distance
- Assigned vehicle and driver, status

### License
Tracks licenses and compliance
- License number, type, holder
- Issue/expiry dates, status

## Running Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_models.py
```

## Common Commands

### Database Operations
```bash
# Reset database (WARNING: deletes all data)
python -c "from app import create_app; from models import db; app = create_app(); app.app_context().push(); db.drop_all(); db.create_all()"

# Load sample data
python sample_data.py
```

### Development
```bash
# Activate virtual environment
source venv/bin/activate

# Run application in debug mode
python app.py

# Run tests
pytest tests/

# Verify setup
python verify_setup.py
```

## Scrum Methodology

This project follows Scrum agile methodology:

### Sprint Cycle (2 weeks)
1. **Sprint Planning** - Select user stories and create tasks
2. **Daily Standup** - 15-min sync (9:00 AM)
3. **Development** - Implement features with TDD
4. **Sprint Review** - Demo to stakeholders
5. **Sprint Retrospective** - Team reflection

### Key Documents
- **Product Backlog** - All user stories and features
- **Sprint Planning** - Current sprint goals and tasks
- **Team Roles** - Responsibilities and communication

See `docs/` folder for detailed Scrum documentation.

## Next Steps

### For Developers
1. Review the [Development Guide](docs/DEVELOPMENT_GUIDE.md)
2. Check the [Product Backlog](docs/PRODUCT_BACKLOG.md)
3. Read the [API Documentation](docs/API_DOCUMENTATION.md)
4. Start with Sprint 1 tasks in [Sprint Planning](docs/SPRINT_PLANNING.md)

### For Product Owners
1. Review and prioritize [Product Backlog](docs/PRODUCT_BACKLOG.md)
2. Refine user stories with acceptance criteria
3. Schedule Sprint Planning meeting

### For Scrum Masters
1. Set up project board (Jira/Trello)
2. Schedule Scrum ceremonies
3. Review [Team Roles](docs/SCRUM_TEAM.md)

## Getting Help

### Documentation
- `README.md` - Project overview
- `docs/DEVELOPMENT_GUIDE.md` - Comprehensive development guide
- `docs/API_DOCUMENTATION.md` - API reference

### Troubleshooting
- Run `python verify_setup.py` to check setup
- Ensure virtual environment is activated
- Check that all dependencies are installed

### Resources
- Flask: https://flask.palletsprojects.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- pytest: https://pytest.org/
- Scrum: https://scrumguides.org/

## Support

For issues or questions:
1. Check existing documentation
2. Review error messages carefully
3. Ensure all dependencies are installed
4. Contact the development team

---

**Happy Coding! 🚀**
