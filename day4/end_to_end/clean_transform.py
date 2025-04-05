import pandas as pd
import os

RAW_FILE = "end_to_end/books_to_scrape.csv"
CLEAN_FILE = "end_to_end/cleaned_books.csv"

def clean_data():
    if not os.path.exists(RAW_FILE):
        print("❌ Raw data file not found.")
        return

    df = pd.read_csv(RAW_FILE)

    # Clean price: remove any non-digit/decimal characters (like Â£ or £)
    #Trim the first two characterso f price column

    df["Price"] = df["Price"].astype(str)
    df["Price"] = df["Price"].str.replace("Â£", "", regex=False).astype(float)

    # Optional: drop rows with missing titles or ratings (if any)
    df.dropna(subset=["Title", "Rating"], inplace=True)

    # Save cleaned data
    df.to_csv(CLEAN_FILE, index=False)
    print(f"✅ Cleaned data saved to {CLEAN_FILE}")

if __name__ == "__main__":
    clean_data()