import os
from dotenv import load_dotenv


def main():
   test_thing = os.getenv('TEST')
   print(test_thing)

if __name__ == "__main__":
   load_dotenv()  # Loads the .env file
   main()