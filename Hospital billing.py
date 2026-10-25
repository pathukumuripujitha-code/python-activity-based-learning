
# Hospital Billing and Patient Classification

patients = [
    ("P101", "Ravi", 500, 1200, 3000, "Senior"),
    ("P102", "Sita", 500, 800, 1500, "General"),
    ("P103", "Raju", 400, 600, 1000, "Student")
]

senior_discount = 15
student_discount = 10
max_bill = 100000
payment_limit = 5000

for patient in patients:
    pid, name, consultation, diagnostic, treatment, category = patient

    print("\nPatient ID:", pid)
    print("Patient Name:", name)

    if min(consultation, diagnostic, treatment) < 0:
        print("Invalid bill: Charges cannot be negative.")
        continue

    total = consultation + diagnostic + treatment

    if total > max_bill:
        print("Invalid bill: Amount exceeds billing limit.")
        continue

    if category == "Senior":
        discount = total * senior_discount / 100
    elif category == "Student":
        discount = total * student_discount / 100
    else:
        discount = 0

    final_bill = total - discount

    print("Consultation Charge:", consultation)
    print("Diagnostic Charge:", diagnostic)
    print("Treatment Charge:", treatment)
    print("Total Before Discount:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)

    if final_bill <= 0:
        print("Invalid payment amount.")
    elif final_bill <= payment_limit:
        print("Patient Classification: Low Payment")
    else:
        print("Patient Classification: High Payment")

    payment = min(final_bill, payment_limit)

    if payment <= final_bill:
        balance = final_bill - payment
        print("Payment Made:", payment)
        print("Remaining Balance:", balance)
