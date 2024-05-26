from agent import Prop_Agent

def main():
    # Create an instance of Prop_Agent
    agent1 = Prop_Agent("Property Guru Co", "A55667",2009)

    # Expected output
    expected_output = (
            f"\n>--- AGENT INFO ---<\n"
            f"Company: Property Guru Co\n"
            f"ID: A55667\n"
            f"Employment Year: 2009\n"
            f"Commission Rate: 0.7\n"
    )

    expected_result = {
        "company": "Property Guru Co",
        "aid": "A55667",
        "start_year": 2009,
        "cs_rate": 0.7
    }

    print("Expected Output:", expected_output)
    print("Program Output:", agent1)

    # Check if the output matches the expected output
    try:
        agent1.test(expected_result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()