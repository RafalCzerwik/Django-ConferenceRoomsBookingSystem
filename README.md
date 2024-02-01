# Django Conference Rooms Booking System

## Introduction
#### This Django project is a simple conference room booking system that allows users to manage conference rooms, make reservations, and view room details.

## Installation
1. ### Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

2. ### Create a virtual environment:
```bash
- python -m venv venv
```
3. ### Activate the virtual environment:

- #### On Windows:
```bash
.\venv\Scripts\activate
```
- #### On macOS/Linux:
```bash
source venv/bin/activate
```
4. ### Install dependencies:
```bash
- pip install -r requirements.txt
```
5. ### Apply database migrations:
```bash
- python manage.py migrate
```
6. ### Run the development server:
```bash
- python manage.py runserver
```
7. ### Access the application in your web browser at http://127.0.0.1:8000/

## Usage
### Adding a New Room
- Access the "Add New Room" page at http://127.0.0.1:8000/room/new/
- Fill in the required information and click "Submit" to add a new conference room.

### Viewing Room List
- Navigate to the "Room List" page at http://127.0.0.1:8000/
- Browse the list of available conference rooms with their details.

### Modifying a Room
- Click on a room in the "Room List" to go to the details page.
- From the details page, click on the "Modify" button to update the room information.

### Deleting a Room
- Click on a room in the "Room List" to go to the details page.
- From the details page, click on the "Delete" button to remove the room.

### Reserving a Room
- Click on a room in the "Room List" to go to the details page.
- From the details page, click on the "Reserve" button to make a reservation.

### Searching for Rooms
- Use the "Search" functionality at http://127.0.0.1:8000/search/ to filter rooms based on name, capacity, and projector availability.

## Contributing
Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests.

## License
This project is not licensed.