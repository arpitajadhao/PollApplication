# PollApplication
This is a Django-based web application that allows users to participate in polls by voting on various questions. It features a user registration system with authentication, ensuring that only registered users can vote and view poll results.The application is designed with a modern and responsive UI using Bootstrap, providing a seamless user experience.
**Features**
Key Features:

- User registration and authentication
- Secure voting system with one vote per user per poll
- Dynamic display of poll results
- Responsive design for better usability
- User can vote only once for a poll
  

## 🛠️ Tech Stack  
- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** Default SQLite (can be configured to use other databases)

- ## ⚙️ Installation and Setup  
Follow these steps to install and set up the project on your local machine.  

### 1. **Clone the Repository**  
1. First, clone the repository to your local machine using the following command:  
```bash
git clone https://github.com/arpitajadhao/PollApplication.git
2. Create & Activate a Virtual Environment python -m venv venv source venv/bin/activate On Windows: venv\Scripts\activate
3. Install Dependencies pip install -r requirements.txt
4. Apply Migrations python manage.py migrate
5. Create Superuser (For Admin Panel Access) python manage.py createsuperuser
6. Run the Server python manage.py runserver Access the app at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.

🔐 User Registration & Authentication
The app allows users to register and log in using Django's authentication system.
Only authenticated users can vote in polls and view results.
After registering, users are automatically logged in and redirected to the polls index page.

🎨 UI Design
The application uses Bootstrap for a modern and responsive user interface.
Clean and intuitive design for better usability and accessibility.

📜 License
This project is licensed under the MIT License.


