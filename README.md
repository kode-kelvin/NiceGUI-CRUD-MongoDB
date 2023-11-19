# NiceGUI-CRUD-MongoDB

# NiceGUI CRUD Application with MongoDB

## Introduction

Welcome to the NiceGUI CRUD application using MongoDB. This project is built on the Python NiceGUI framework, which integrates VueJS, Quasar, and FastAPI. The goal of this application is to provide a simple yet powerful example of a CRUD (Create, Read, Update, Delete) functionality using NiceGUI and MongoDB.

## Getting Started

To begin working with this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kode-kelvin/NiceGUI-CRUD-MongoDB.git
   cd NiceGUI-CRUD-MongoDB
   ```

2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB:**
   - Create a MongoDB account.
   - Create a cluster and database. Make note of the connection URI.

## Configuration

Before running the application, make sure to set up the MongoDB connection in the `.env` file. Open the file and update the `MONGODB_URI` variable with your MongoDB connection URI.
# .env 

SECRET_KEY=yourSecretKey
DB_PASSWORD=yourMongodbPassword
DB_USER_NAME=yourDbName


## Running the Application

Once you've cloned the project, installed the requirements, and configured the MongoDB connection, you can run the application using the following command:

```bash
python app.py
```

This will start the FastAPI server and make the application accessible at [http://localhost:8000](http://localhost:8000).

## Usage

Visit the application in your web browser and interact with the CRUD functionality provided. You can perform the following operations:

- **Create:** Add new items to the database.
- **Read:** View the list of items in the database.
- **Update:** Modify existing items in the database.
- **Delete:** Remove items from the database.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NiceGUI: [NiceGUI GitHub Repository](https://github.com/kode-kelvin/NiceGUI)
- MongoDB: [MongoDB](https://www.mongodb.com/)

Enjoy using the NiceGUI CRUD application with MongoDB! If you have any questions or issues, please feel free to open an [issue](https://github.com/kode-kelvin/NiceGUI-CRUD-MongoDB/issues).
