import motor.motor_asyncio

MONGODB_URL = 'mongodb://root:rootpassword@localhost:8000'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database 
database = client.python_db