# Gas Utility Service  

The **Gas Utility Service** project is a Django-based web application designed to streamline service request management for gas utilities. This project demonstrates a scalable architecture, clean code practices, and practical implementation of Django’s capabilities for handling requests efficiently.  

## Features  
- **User Management**:  
  - Superuser setup for administrative tasks.  
  - Secure user authentication and authorization.  

- **Service Requests**:  
  - User-friendly interface to submit service requests.  
  - Dynamic request management for efficient handling.  

- **Database Management**:  
  - Migration files included for seamless database setup.  
  - Relational database support for scalability and reliability.  

- **Customizable**:  
  - Modular design allows easy integration of additional features.  
  - Fully configurable for deployment on AWS.  

## Requirements  
- Python 3.8+  
- Django 4.0+  
- MySQL (or your preferred relational database)  

## Setup  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/Githubarunkumar847/gas-utility-service.git  
   cd gas-utility-service  
   ```  

2. Create a virtual environment and install dependencies:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # (For Windows: venv\Scripts\activate)  
   pip install -r requirements.txt  
   ```  

3. Configure the database in `settings.py`.  

4. Apply database migrations:  
   ```bash  
   python manage.py migrate  
   ```  

5. Create a superuser for accessing the admin panel:  
   ```bash  
   python manage.py createsuperuser  
   ```  

6. Start the development server:  
   ```bash  
   python manage.py runserver  
   ```  

   By default, the application will run on [http://127.0.0.1:8000](http://127.0.0.1:8000).  

## Usage  
- Access the admin panel at `/admin` with the superuser credentials.  
- Submit service requests through the `/home` endpoint.  
- Manage and review service requests using the admin interface.  

## Deployment  
The project is fully prepared for deployment on **AWS**. You can deploy using services like **Elastic Beanstalk** or **EC2**. Detailed instructions will be added in future updates.  

## Contributing  
Contributions are welcome! If you’d like to enhance the project or report any issues, feel free to open an issue or submit a pull request.  

## License  
This project is licensed under the MIT License.