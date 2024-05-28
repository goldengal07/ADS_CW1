from agent_director import Prop_Agency_Director
from agent import Prop_Agent

def main():
    # Create an instance of Prop_Agent
    director1 = Prop_Agency_Director("Property Guru Co", "Director-E77889", 2016, 0.07, 0.8)
    agent1 = Prop_Agent("Real Estate Co", "Agent-12345", 2018)
    agent2 = Prop_Agent("Real Estate Co", "Agent-B67890", 2019)
    agent3 = Prop_Agent("Real Estate Co", "Agent-C11223", 2020)

    # Add agents to director
    director1.add_agent(agent1.get_aid())
    director1.add_agent(agent2.get_aid())
    director1.add_agent(agent3.get_aid())

    # Expected output
    expected_output = (
            f"\n>--- DIRECTOR INFO ---<\n"
            f"Company: Property Guru Co\n"
            f"ID: Director-E77889\n"
            f"Employment Year: 2016\n"
            f"Commission Rate: 0.8\n"
            f"Overriding Commission Rate: 0.07\n"
            f"Agents: ['Agent-12345', 'Agent-B67890', 'Agent-C11223']\n"
    )

    expected_result = {
        "company": director1.get_company(),
        "aid": director1.get_aid(),
        "start_year": director1.get_start_year(),
        "cs_rate": director1.get_cs_rate(),
        "over_c_rate": director1.get_over_c_rate(),
        "agents": director1.get_agents()
    }

    print("Expected Output:", expected_output)
    print("Program Output:", director1)

    # Check if the output matches the expected output
    try:
        director1.test(expected_result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()