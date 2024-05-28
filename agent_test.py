from agent import Prop_Agent
from property import Property

def main():
    # Create an instance of Prop_Agent
    agent1 = Prop_Agent("Property Guru Co", "A55667",2009)
    agent2 = Prop_Agent("SG HDB Flat Sale", "B88900",2007)

    property1 = Property("Block 605 Bishan #06-098",570107,"Freehold",2004,"Housing","Bishan",8000000)
    property2 = Property("Block 443 Sin Ming Avenue #01-439", 570443, "Leasehold", 2006, "Housing", "Bishan", 850000)

    # Add properties to Agent
    agent1.add_sold_property(property1.get_address())
    agent1.add_unsold_property(property2.get_address())
    #sell =

    # Expected output
    expected_output = (
            f"\n>--- AGENT INFO ---<\n"
            f"Company: Property Guru Co\n"
            f"ID: A55667\n"
            f"Employment Year: 2009\n"
            f"Commission Rate: 0.7\n"
            f"Sold Properties: ['Block 605 Bishan #06-098']\n"
            f"Unsold Properties: ['Block 443 Sin Ming Avenue #01-439']\n"
    )

    # Results
    expected_result = {
        "company": agent1.get_company(),
        "aid": agent1.get_aid(),
        "start_year": agent1.get_start_year(),
        "cs_rate": agent1.get_cs_rate(),
        "sold": [property1.get_address()],
        "unsold": [property2.get_address()]
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