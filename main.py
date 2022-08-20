from dotenv import load_dotenv

from TDConnection import TDConnector

def main():
   ticker_symbols = ['aapl', 'tsla']
   Td_Connection = TDConnector(ticker_symbols=ticker_symbols)
   print(Td_Connection.return_stuff())

if __name__ == "__main__":
   load_dotenv()  # Loads the .env file
   main()