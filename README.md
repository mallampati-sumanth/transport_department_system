# Transport Department System

A comprehensive system for managing transport department operations using Scrum methodology.

## Overview

The Transport Department System is designed to manage vehicles, drivers, routes, and licenses for a transportation organization. The system follows Scrum agile methodology for project management and development.

## Features

- **Vehicle Management**: Track and manage vehicle inventory, maintenance schedules, and status
- **Driver Management**: Maintain driver records, licenses, and assignments
- **Route Management**: Create and manage transportation routes with schedules
- **License & Compliance**: Track licenses, permits, and ensure regulatory compliance
- **Reporting & Analytics**: Generate reports and monitor key performance indicators

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLAlchemy (SQLite for development, can be configured for PostgreSQL/MySQL)
- **Testing**: pytest
- **Project Management**: Scrum methodology

## Project Structure

```
transport_department_system/
├── app.py                 # Main application file
├── config.py             # Configuration settings
├── models.py             # Database models
├── requirements.txt      # Python dependencies
├── tests/               # Unit tests
│   └── test_models.py
├── docs/                # Scrum documentation
│   ├── PRODUCT_BACKLOG.md
│   ├── SPRINT_PLANNING.md
│   └── SCRUM_TEAM.md
└── README.md
```

## Quick Start

### Automated Setup
```bash
git clone https://github.com/mallampati-sumanth/transport_department_system.git
cd transport_department_system
./setup.sh
```

### Manual Setup

1. Clone the repository:
```bash
git clone https://github.com/mallampati-sumanth/transport_department_system.git
cd transport_department_system
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize database:
```bash
python init_db.py
```

For detailed setup instructions, see [Quick Start Guide](docs/QUICK_START.md).

## Running the Application

### Development Mode
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Running Tests
```bash
pytest tests/
```

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /api/vehicles` - List all vehicles
- `GET /api/drivers` - List all drivers
- `GET /api/routes` - List all routes
- `GET /api/licenses` - List all licenses

## Documentation

### Getting Started
- **[Quick Start Guide](docs/QUICK_START.md)** - Get up and running in 5 minutes
- **[Development Guide](docs/DEVELOPMENT_GUIDE.md)** - Comprehensive development guide
- **[API Documentation](docs/API_DOCUMENTATION.md)** - Complete API reference

### Scrum Methodology
The project follows Scrum methodology with the following artifacts:
- **[Product Backlog](docs/PRODUCT_BACKLOG.md)** - User stories and epics
- **[Sprint Planning](docs/SPRINT_PLANNING.md)** - Sprint goals and tasks
- **[Team Roles](docs/SCRUM_TEAM.md)** - Roles and responsibilities

## Development Workflow

1. **Sprint Planning**: Team selects user stories from Product Backlog
2. **Daily Standup**: 15-minute daily sync at 9:00 AM
3. **Development**: Implement features with TDD approach
4. **Sprint Review**: Demonstrate completed work to stakeholders
5. **Sprint Retrospective**: Team reflection and continuous improvement

## Contributing

1. Create a feature branch from main
2. Implement changes with unit tests
3. Ensure all tests pass
4. Submit pull request for code review
5. Merge after approval

## Verification

To verify that the system is set up correctly:
```bash
python verify_setup.py
```

This will check that all required files are present and have valid syntax.

## Contributing

We welcome contributions! Please follow these steps:

1. Review the [Development Guide](docs/DEVELOPMENT_GUIDE.md)
2. Check the [Product Backlog](docs/PRODUCT_BACKLOG.md) for available tasks
3. Create a feature branch
4. Make your changes with tests
5. Submit a pull request

See our Definition of Done in the [Product Backlog](docs/PRODUCT_BACKLOG.md).

## License

This project is developed for educational purposes as part of a Scrum-based software development initiative.

## Acknowledgments

This Transport Department System demonstrates:
- Clean Python architecture with Flask
- Database design with SQLAlchemy
- RESTful API design
- Scrum agile methodology
- Test-driven development with pytest
