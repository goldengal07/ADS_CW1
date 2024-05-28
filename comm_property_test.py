from comm_property import Comm_Property
def main():
    # Create an instance of Comm_Property
    comm_property1 = Comm_Property("123 Business Park",987654,"Leasehold",2015,"Commercial","Office","Downtown",15000000, 0.01)

    # Expected output
    expected_output = (
        ">--- PROPERTY INFO ---<\n"
        "Location: 123 Business Park\n"
        "Postal Code: 987654\n"
        "Tenure: Leasehold\n"
        "Year of Completion: 2015\n"
        "Property Type: Commercial\n"
        "Commercial Property Type: Office\n"
        "Area: Downtown\n"
        "Valuation: $15,000,000\n"
        "Commission: $150,000\n"
    )

    expected_result = {
        "address": "123 Business Park",
        "p_code": 987654,
        "tenure": "Leasehold",
        "yoc": 2015,
        "prop_type": "Commercial",
        "comm_property_type": "Office",
        "area": "Downtown",
        "worth": 15000000,
        "Commission": 150000,
    }

    print("Expected Output:\n", expected_output)
    print("Program Output:", comm_property1)

    # Check if the output matches the expected output
    try:
        comm_property1.test(expected_result)
    except ValueError as e:
        print(e)
    # if str(comm_property1) == expected_output:
    #     print("\nTest Passed.")
    # else:
    #     print("\nTest Failed.")


if __name__ == '__main__':
    main()
