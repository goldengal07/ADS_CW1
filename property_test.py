from property import Property


def main():
    # Create an instance of Property
    property1 = Property(
        "Block 605 Bishan #06-098",
        570107,
        "Freehold",
        2004,
        "Housing",
        "Bishan",
        8000000
    )

    # Expected output
    expected_output = (
        ">--- PROPERTY INFO ---<\n"
        "Location: Block 605 Bishan #06-098\n"
        "Postal Code: 570107\n"
        "Tenure: Freehold\n"
        "Year of Completion: 2004\n"
        "Property Type: Housing\n"
        "Area: Bishan\n"
        "Valuation: $8,000,000\n"
        "Commission: $80,000\n"
    )

    expected_result = {
        "address": "Block 605 Bishan #06-098",
        "p_code": 570107,
        "tenure": "Freehold",
        "yoc": 2004,
        "prop_type": "Housing",
        "area": "Bishan",
        "worth": 8000000,
        "Commission": 80000
    }

    print("Expected Output:\n", expected_output)
    print("Program Output:", property1)

    # result = property1.test(expected_result)
    # if result.success == True:
    #     print("passed")
    # else:
    #     print("failed", result.error)

    # Check if the output matches the expected output
    try:
        property1.test(expected_result)
    except ValueError as e:
        print(e)
    # if expected_output == str(property1):
    #     print("Test Passed!")
    # else:
    #     print("Test Failed.")


if __name__ == '__main__':
    main()