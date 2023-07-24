# Program Title: Project 1: Lists and Data Files
# Program Description: This program is for calculate new insurance policy infomration.
# Written By: Mohamed Maghrebi
# Written on: July 22, 2023

# Imports/
import datetime



# define functions

def CalMonthlyPayments(TotalCost):
    TotalCost += Pro_Fee
    MonthlyPayments = TotalCost / 8

    return MonthlyPayments


# Open the defaults file and read the values into variables

f = open('OSICDef.dat', 'r')
Pol_Num = int(f.readline())
Bas_Pre = float(f.readline())
Dis_Add_Car = float(f.readline())
Cos_Ex_Lia= float(f.readline())
Cos_Gla_Cov = float(f.readline())
Cos_Loa_Car = float(f.readline())
HST_RATE = float(f.readline())
Pro_Fee = float(f.readline())
f.close()

# Main Program
while True:
    CusFirstName = input("Enter the customer first name (END to quit): ").title()
    if CusFirstName == "End":
        break

    CusLastName = input("Enter the customer's last name: ").title()
    CusStAdd = input("Enter customer's street address: ").title()
    CusCity = input("Enter the city: ").title()

    valid_provinces = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QB", "SK", "YT"]

    while True:
        CusProv = input("Enter the province(XX): ").upper()
        if CusProv not in valid_provinces:
            print("Error - Province is invalid.")
        else:
            break

    Postal = input("Enter the postal code (L0L0L0): ").upper()

    CusPhoneNum = input("Enter the phone number (999999999): ")

    NumCars = int(input("Enter number of cars being insured: "))
    OptLiability = input("Enter Y or N for extra liability up to $1,000,000: ").upper()
    GlassCoverage = input("Enter Y or N for glass coverage: ").upper()
    OptLoaner = input("Enter Y or N for loaner car: ").upper()

    valid_payments = ["Monthly", "Full"]

    while True:
        PaymentMethod = input("Enter payment method(Full or Monthly): ").title()
        if PaymentMethod not in valid_payments:
            print("Error - Payment method is invalid.")
        else:
            break
    print()
# Calculations


    if NumCars == 1:
        Premium = Bas_Pre
    else:
        AddtCarPremium = (NumCars - 1) * Bas_Pre
        AddtCarDiscount = AddtCarPremium - (AddtCarPremium * Dis_Add_Car)
        Premium = Bas_Pre + AddtCarDiscount
        AddtCarDiscountDsp = "${:,.2f}".format(AddtCarDiscount)

    if OptLiability == "Y":
        OptLiabilityCost = Cos_Ex_Lia * NumCars
    else:
        OptLiabilityCost = 0
    if GlassCoverage == "Y":
        GlassCoverageCost = Cos_Gla_Cov * NumCars
    else:
        GlassCoverageCost = 0
    if OptLoaner == "Y":
        OptLoanerCost = Cos_Loa_Car * NumCars
    else:
        OptLoanerCost = 0

    TotalExtra = OptLoanerCost + OptLiabilityCost + GlassCoverageCost

    Subtotal = Premium + TotalExtra

    HSTAmount = Subtotal * HST_RATE

    TotalCost = Subtotal + HSTAmount

    MonthlyPayments = CalMonthlyPayments(TotalCost)


# Get invoice date and next payment dates
    InvoiceDate = datetime.date.today()
    NextPaymentDate = InvoiceDate.replace(day=1, month=InvoiceDate.month + 1)

# formatting
    PremiumDsp = "${:,.2f}".format(Premium)
    OptLiabilityCostDsp = "${:,.2f}".format(OptLiabilityCost)
    GlassCoverageCostDsp = "${:,.2f}".format(GlassCoverageCost)
    OptLoanerCostDsp = "${:,.2f}".format(OptLoanerCost)
    SubtotalDsp = "{:,.2f}".format(Subtotal)
    HSTAmountDsp = "${:,.2f}".format(HSTAmount)
    TotalExtraDsp = "${:,.2f}".format(TotalExtra)
    TotalCostDsp = "${:,.2f}".format(TotalCost)
    MonthlyPaymentsDsp = "${:,.2f}".format(MonthlyPayments)



#User outputs

    print("One Stop Insurance Company")
    print("\n===== Receipt =====")
    print(f"Date: {InvoiceDate}")
    print(f"Policy Number: {int(Pol_Num)}")
    print(f"Customer Name: {CusFirstName} {CusLastName}")
    print(f"Address: {CusStAdd}")
    print(f"City: {CusCity}")
    print(f"Province: {CusProv}")
    print(f"Postal Code: {Postal}")
    print(f"Phone Number: {CusPhoneNum}")
    print(f"Number of Cars Insured: {NumCars}")
    print(f"Extra Liability Coverage: {'Yes' if OptLiability == 'Y' else 'No'}")
    print(f"Glass Coverage: {'Yes' if GlassCoverage == 'Y' else 'No'}")
    print(f"Loaner Car Coverage: {'Yes' if OptLoaner == 'Y' else 'No'}")
    print(f"Total Extra Charges: {TotalExtraDsp}")
    print(f"Total Premium: {PremiumDsp}")
    print(f"HST (15%): {HSTAmountDsp}")
    print(f"Processing Fee: ${Pro_Fee:.2f}")
    print(f"Total Cost: {TotalCostDsp}")
    print(f"Payment Method: {PaymentMethod}")
    if PaymentMethod == "Monthly":
        print(f"Monthly Payment Amount: {MonthlyPaymentsDsp}")
        print(f"Next Payment Date: {NextPaymentDate}\n")




   # Write the values to a file for future reference.
    f = open("Policies.dat", "a")
    f.write(f"{Pol_Num}, ")
    f.write(f"{InvoiceDate}, ")
    f.write(f"{CusFirstName}, ")
    f.write(f"{CusLastName}, ")
    f.write(f"{CusStAdd}, ")
    f.write(f"{CusCity}, ")
    f.write(f"{CusProv}, ")
    f.write(f"{Postal}, ")
    f.write(f"{CusPhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{OptLiability}, ")
    f.write(f"{GlassCoverage}, ")
    f.write(f"{OptLoaner}, ")
    f.write(f"{PaymentMethod}, ")
    f.write(f"{TotalCost}\n")
    f.close()
    print()
    print("Policy information processed and saved...")

# Update any default values based on the processing requirements
    Pol_Num += 1

# Housekeeping
    f = open('OSICDef.dat', 'w')
    f.write(f"{Pol_Num}\n")
    f.write(f"{Bas_Pre}\n")
    f.write(f"{Dis_Add_Car}\n")
    f.write(f"{Cos_Ex_Lia}\n")
    f.write(f"{Cos_Gla_Cov}\n")
    f.write(f"{Cos_Loa_Car}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{Pro_Fee}\n")
    f.close()
    print()
