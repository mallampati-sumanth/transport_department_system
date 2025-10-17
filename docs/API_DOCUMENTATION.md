# API Documentation - Transport Department System

## Base URL
```
http://localhost:5000
```

## Endpoints

### 1. Get API Information
Get information about the API and available endpoints.

**Endpoint:** `GET /`

**Response:**
```json
{
  "message": "Transport Department System API",
  "version": "1.0.0",
  "endpoints": {
    "vehicles": "/api/vehicles",
    "drivers": "/api/drivers",
    "routes": "/api/routes",
    "licenses": "/api/licenses"
  }
}
```

### 2. List All Vehicles
Retrieve a list of all vehicles in the system.

**Endpoint:** `GET /api/vehicles`

**Response:**
```json
[
  {
    "id": 1,
    "registration_number": "ABC-1234",
    "vehicle_type": "Bus",
    "manufacturer": "Toyota",
    "model": "Coaster",
    "status": "active"
  }
]
```

**Vehicle Statuses:**
- `active` - Vehicle is operational
- `maintenance` - Vehicle is under maintenance
- `retired` - Vehicle is no longer in service

### 3. List All Drivers
Retrieve a list of all drivers in the system.

**Endpoint:** `GET /api/drivers`

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "license_number": "DL-123456",
    "license_type": "B",
    "status": "active"
  }
]
```

**Driver Statuses:**
- `active` - Driver is currently employed
- `on_leave` - Driver is on leave
- `retired` - Driver is no longer employed

### 4. List All Routes
Retrieve a list of all routes in the system.

**Endpoint:** `GET /api/routes`

**Response:**
```json
[
  {
    "id": 1,
    "route_number": "R-001",
    "start_location": "City Center",
    "end_location": "Airport",
    "distance_km": 25.5,
    "status": "active"
  }
]
```

**Route Statuses:**
- `active` - Route is currently operational
- `inactive` - Route is temporarily not in use
- `suspended` - Route has been suspended

### 5. List All Licenses
Retrieve a list of all licenses in the system.

**Endpoint:** `GET /api/licenses`

**Response:**
```json
[
  {
    "id": 1,
    "license_number": "LIC-2024-001",
    "license_type": "Operating Permit",
    "holder_name": "Transport Department",
    "status": "valid"
  }
]
```

**License Statuses:**
- `valid` - License is currently valid
- `expired` - License has expired
- `suspended` - License has been suspended
- `revoked` - License has been revoked

## Database Models

### Vehicle Model
```python
{
  "id": Integer (Primary Key),
  "registration_number": String(20) (Unique, Required),
  "vehicle_type": String(50) (Required),
  "manufacturer": String(50),
  "model": String(50),
  "year": Integer,
  "capacity": Integer,
  "status": String(20),
  "created_at": DateTime,
  "updated_at": DateTime
}
```

### Driver Model
```python
{
  "id": Integer (Primary Key),
  "name": String(100) (Required),
  "license_number": String(20) (Unique, Required),
  "license_type": String(10) (Required),
  "phone": String(20),
  "email": String(100),
  "address": String(200),
  "hire_date": Date,
  "status": String(20),
  "created_at": DateTime,
  "updated_at": DateTime
}
```

### Route Model
```python
{
  "id": Integer (Primary Key),
  "route_number": String(20) (Unique, Required),
  "start_location": String(100) (Required),
  "end_location": String(100) (Required),
  "distance_km": Float,
  "estimated_duration_minutes": Integer,
  "vehicle_id": Integer (Foreign Key),
  "driver_id": Integer (Foreign Key),
  "status": String(20),
  "created_at": DateTime,
  "updated_at": DateTime
}
```

### License Model
```python
{
  "id": Integer (Primary Key),
  "license_number": String(20) (Unique, Required),
  "license_type": String(50) (Required),
  "holder_name": String(100) (Required),
  "issue_date": Date (Required),
  "expiry_date": Date (Required),
  "status": String(20),
  "created_at": DateTime,
  "updated_at": DateTime
}
```

## Error Handling

All endpoints return appropriate HTTP status codes:
- `200 OK` - Request successful
- `400 Bad Request` - Invalid request parameters
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Future Enhancements

The following endpoints are planned for future sprints:
- `POST /api/vehicles` - Create a new vehicle
- `PUT /api/vehicles/{id}` - Update vehicle information
- `DELETE /api/vehicles/{id}` - Delete a vehicle
- Similar CRUD operations for drivers, routes, and licenses
- Authentication and authorization
- Advanced filtering and search
- Pagination support
