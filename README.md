
# ParkWise Backend

The backend for ParkWise, a parking management system, built with Django and Django REST Framework.

## Features
- Manage parking areas and parking spots.
- Calculate available parking spaces and occupancy rates dynamically.
- Provide RESTful APIs for parking management.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/razmazlih/ParkWise-backend.git
    cd ParkWise-backend
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create migrations:
    ```bash
    python manage.py makemigrations
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```

The backend will be available at `http://localhost:8000`.

## API Endpoints
### Parking Areas
- **GET** `/api/parking-areas/` - List all parking areas.
- **POST** `/api/parking-areas/` - Create a new parking area.
- **GET** `/api/parking-areas/{id}/` - Retrieve a specific parking area.
- **PUT** `/api/parking-areas/{id}/` - Update a specific parking area.
- **DELETE** `/api/parking-areas/{id}/` - Delete a specific parking area.

### Parking Spots
- **GET** `/api/parking-spots/` - List all parking spots.
- **POST** `/api/parking-spots/` - Create a new parking spot.
- **GET** `/api/parking-spots/{id}/` - Retrieve a specific parking spot.
- **PUT** `/api/parking-spots/{id}/` - Update a specific parking spot.
- **DELETE** `/api/parking-spots/{id}/` - Delete a specific parking spot.
- **GET** `/api/parking-spots/by-area/{area_id}/` - Retrieve parking spots by area.

## File Structure
```
backend/
├── parking/
│   ├── models.py       # Database models for ParkingArea and ParkingSpot
│   ├── serializers.py  # API serializers for ParkingArea and ParkingSpot
│   ├── views.py        # API viewsets for ParkingArea and ParkingSpot
│   ├── urls.py         # URL routing for the parking app
│   └── ...
├── manage.py
├── settings.py
└── ...
```

## Dynamic Features
1. **Availability Calculation**:
   - `ParkingArea` model automatically updates the count of available parking spots and accessible spots.

2. **Validation**:
   - Validates parking spot positions with a custom format (`e.g., A1, B10`).

3. **Occupancy Rate**:
   - Calculates the percentage of occupied spots for each parking area.

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License.

---

### Future Enhancements
- Add real-time notifications for spot availability.
- Implement authentication and permissions.
- Integrate geolocation services to map parking areas.
