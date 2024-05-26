from agent_director import Prop_Agency_Director
class Commission_Slip:
    @staticmethod
    def calculate_commission(property, sharing_rate):
        return property._worth * property._c_rate * sharing_rate


    @staticmethod
    def print_commission_slip(agent):
        total_commission = 0
        print(f"\nCommission Slip for Agent: {agent._aid}")
        for property in agent._sold_properties:
            commission = Commission_Slip.calculate_commission(property, agent._cs_rate)
            total_commission += commission
            print(f"Property: {property._address}, Valuation: ${property._worth: ,.0f},"
                  f"Commission: ${commission:,.0f}")
            print(f"Total Commission Earned: ${total_commission: ,.0f}")

        if isinstance(agent, Prop_Agency_Director):
            total_override_commission = 0
            print("Override Commissions:")
            for sub_agent in agent.agents:
                for property in sub_agent._sold_properties:
                    commission = Commission_Slip.calculate_commission(property, sub_agent._cs_rate)
                    override_commission = commission * agent.over_c_rate
                    total_override_commission += override_commission
                    print(
                        f"Agent: {sub_agent._aid}, Property: {property._address}, Override Commission for Director: ${override_commission: ,.0f}")
            print(f"Total Override Commission Earned by Director: ${total_override_commission: ,.0f}")
            total_commission += total_override_commission
        print(f"Total Income Earned: ${total_commission: ,.0f}")
