import csv


class ExchangeRates:
    """Class to load exchange rate data from a CSV file and perform conversions."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.usd_cad_rate = self._read_latest_usd_cad_rate()

    def _read_latest_usd_cad_rate(self) -> float:
        """Reads the CSV file and retrieves the latest USD/CAD rate from the last row."""
        latest_rate = None

        with open(self.filepath, mode="r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Store the value from column 'FXAUSDCAD'
                if "FXAUSDCAD" in row and row["FXAUSDCAD"]:
                    latest_rate = float(row["FXAUSDCAD"])

        if latest_rate is None:
            raise ValueError("USD/CAD exchange rate ('FXAUSDCAD') not found in the file.")

        return latest_rate

    def convert(self, amount: float, from_curr: str, to_curr: str) -> float:
        """Converts an amount between USD and CAD using the latest exchange rate.

        Exchange rate is expressed as CAD per 1 USD (1 USD = rate CAD).
        """
        from_curr = from_curr.upper()
        to_curr = to_curr.upper()

        if from_curr == to_curr:
            return amount
        elif from_curr == "USD" and to_curr == "CAD":
            return amount * self.usd_cad_rate
        elif from_curr == "CAD" and to_curr == "USD":
            return amount / self.usd_cad_rate
        else:
            raise ValueError("Supported currencies are 'USD' and 'CAD' only.")


def main():
    # File name as downloaded from Canvas
    filename = "BankOfCanadaExchangeRate.2026.csv"

    try:
        # Instantiate the ExchangeRates class
        rates = ExchangeRates(filename)
        print(f"Loaded latest USD/CAD Exchange Rate: {rates.usd_cad_rate}\n")

        # Prompt user for inputs
        amount = float(input("Enter amount to convert: "))
        from_currency = input("Enter 'from' currency (USD or CAD): ").strip().upper()
        to_currency = input("Enter 'to' currency (USD or CAD): ").strip().upper()

        # Perform conversion
        converted_amount = rates.convert(amount, from_currency, to_currency)

        print(
            f"\nResult: {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
        )

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'. Make sure it is in the same folder as this script.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()