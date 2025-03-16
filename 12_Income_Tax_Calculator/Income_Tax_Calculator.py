import customtkinter as ctk

class TaxCalculator:

    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        #initialize window
        self.padding: dict = {"padx": 20, "pady": 10}

        #Income Label and entry
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        #Tax Rate Label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text="Tax Percent:")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        #Calculated Tax Label and Result
        self.result_label = ctk.CTkLabel(self.window, text="Total Tax:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0,'0')
        self.result_entry.grid(row=2,column=1, **self.padding)

        #calculate button
        self.calculate_button = ctk.CTkButton(self.window, text="Calculate", command=self.calculate_tax)
        self.calculate_button.grid(row=3,column=1, **self.padding)


    def update_results(self, text: str):
        self.result_entry.delete(0,ctk.END)
        self.result_entry.insert(0,text)


    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            tax = income * (tax_rate / 100)
            print(f"tax=${tax}")
            self.update_results(f"${tax:,.2f}")

        except ValueError:
            self.update_results("Invalid Input")

    def run(self):
        self.window.mainloop()



def main() -> None:
    tax = TaxCalculator()
    tax.run()

if __name__ == "__main__":
    main()