from agent_director import Prop_Agency_Director
from agent import Prop_Agent
class Commission_Slip:
    @staticmethod
    def calculate_agent_commission(property, agent_rate):
        return property.get_worth() * property.get_c_rate() * agent_rate

    @staticmethod
    def calculate_property_commission(property):
        return property.get_worth() * property.get_c_rate()

    @staticmethod
    def print_commission_slip(agent):
        if isinstance(agent, Prop_Agent):
            total_commission = 0
            print(f"\nCommission Slip -> {agent.get_aid()}\nProperties Sold:")

            for index, property in enumerate(agent.get_sold_properties(), start=1):
                commission = Commission_Slip.calculate_agent_commission(property, agent.get_cs_rate())
                prop_commission = Commission_Slip.calculate_property_commission(property)
                total_commission += commission
                print(f"{index}. Property: {property.get_address()}, Valuation: ${property.get_worth()}, Property Rate: {property.get_c_rate()}, Agent Rate: {agent.get_cs_rate()}, Property Commission: ${prop_commission:.0f}, Shared Commission: ${commission:,.0f}")
            print(f"Total Commission Earned: ${total_commission:,.0f}")

        if isinstance(agent, Prop_Agency_Director):
            total_override_commission = 0
            print("Overriding Commissions:")
            for sub_agent in agent.get_agents():
                for property in sub_agent.get_sold_properties():
                    commission = Commission_Slip.calculate_agent_commission(property, sub_agent.get_cs_rate())
                    prop_commission = Commission_Slip.calculate_property_commission(property)
                    override_commission = commission * agent.get_over_c_rate()
                    total_override_commission += override_commission

                    print(
                        f"- Agent ID: {sub_agent.get_aid()}, Property: {property.get_address()}, Valuation: ${property.get_worth():.0f}, Property Rate: {property.get_c_rate()}, Property Commission: ${prop_commission:.0f}\n    Agent Rate: {sub_agent.get_cs_rate()}, Overriding Commission Rate: {agent.get_over_c_rate()}, Overriding Commission: ${override_commission:.0f}")
            print(f"Total Overriding Commission Earned: ${total_override_commission:,.0f}")
            total_commission += total_override_commission
        print(f"Total Income Earned: ${total_commission:,.0f}")
