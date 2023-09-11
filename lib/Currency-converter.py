import requests

# Exchange rates (as of a specific date)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 110.01,
    # Add more currencies and their exchange rates as needed
}

def fetch_exchange_rates():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data["rates"]
    except Exception as e:
        print(f"Error fetching exchange rates: {str(e)}")
        return None

def update_exchange_rates():
    global exchange_rates
    new_rates = fetch_exchange_rates()
    if new_rates:
        exchange_rates = new_rates
        print("Exchange rates updated successfully.")

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    if from_currency in exchange_rates and to_currency in exchange_rates:
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Invalid currency codes."

if __name__ == "__main__":
    try:
        while True:
            print("\nOptions:")
            print("1. Convert currency")
            print("2. Update exchange rates")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter the amount: "))
                from_currency = input("Enter the currency you are converting from (e.g., USD): ").upper()
                to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()

                result = convert_currency(amount, from_currency, to_currency)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
            elif choice == "2":
                update_exchange_rates()
            elif choice == "3":
                print("Exiting the currency converter.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
