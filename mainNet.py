import pandas as pd

def get_open_price(ticker, date):
    # Construct file name based on ticker
    filename = f"{ticker}.csv"

    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(filename)

        # Convert the "Date" column to datetime for easier manipulation
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

        # Filter by the specified date
        filtered_df = df[df['Date'].dt.strftime('%Y-%m-%d') == date]

        if not filtered_df.empty:
            open_price = filtered_df['Open'].values[0]
            return f"The open price for {ticker} on {date} is ${open_price}"
        else:
            return f"No data available for {ticker} on {date}"
    except FileNotFoundError:
        return f"{ticker.upper()} not loaded or file not found."

def main():
    ticker = input("Enter the cryptocurrency ticker (e.g., AVAX): ").strip().upper()
    date = input("Enter the date for the price (format: YYYY-MM-DD): ").strip()

    result = get_open_price(ticker, date)
    print(result)

if __name__ == "__main__":
    main()
