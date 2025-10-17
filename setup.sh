#!/bin/bash
# Setup script for Transport Department System

echo "Transport Department System - Setup"
echo "===================================="

# Check Python version
echo "Checking Python version..."
python --version

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create database tables
echo "Creating database tables..."
python -c "from app import create_app; from models import db; app = create_app('development'); app.app_context().push(); db.create_all(); print('Database tables created successfully!')"

# Optional: Load sample data
read -p "Do you want to load sample data? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Loading sample data..."
    python sample_data.py
fi

echo ""
echo "Setup complete!"
echo "==============="
echo "To run the application:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run the application: python app.py"
echo "  3. Open browser to: http://localhost:5000"
echo ""
echo "To run tests:"
echo "  pytest tests/"
