import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

print(os.getenv("BEARER_TOKEN"))