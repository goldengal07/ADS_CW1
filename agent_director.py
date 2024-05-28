from agent import Prop_Agent

class Prop_Agency_Director(Prop_Agent):
    def __init__(self, company, aid, start_year, over_c_rate=0.05, cs_rate=0.75):
        super().__init__(company, aid, start_year)
        self._over_c_rate = over_c_rate
        self._cs_rate = cs_rate
        self._agents = []

    def add_agent(self, agent):
        self._agents.append(agent)

    def get_over_c_rate(self):
        return self._over_c_rate

    def set_over_c_rate(self, over_c_rate):
        self._over_c_rate = over_c_rate

    def get_cs_rate(self):
        return self._cs_rate

    def set_cs_rate(self, cs_rate):
        self._cs_rate = cs_rate

    def get_agents(self):
        return self._agents

    def set_agents(self, agents):
        self._agents = agents

    def __str__(self):
        return (
            f"\n>--- DIRECTOR INFO ---<\n"
            f"Company: {self._company}\n"
            f"ID: {self._aid}\n"
            f"Employment Year: {self._start_year}\n"
            f"Commission Rate: {self._cs_rate}\n"
            f"Overriding Commission Rate: {self._over_c_rate}\n"
            f"Agents: {self._agents}\n"
        )

    def test(self, expect_result):
        if self._company != expect_result["company"]:
            raise ValueError("ERROR: Company not match: ", self._company, expect_result["company"])
        elif self._aid != expect_result["aid"]:
            raise ValueError("ERROR: Agent ID not match: ", self._aid, expect_result["aid"])
        elif self._start_year != expect_result["start_year"]:
            raise ValueError("ERROR: Employment Year not match: ", self._start_year, expect_result["start_year"])
        elif self._cs_rate != expect_result["cs_rate"]:
            raise ValueError("ERROR: Commission Sharing Rate not match: ", self._cs_rate, expect_result["cs_rate"])
        elif self._over_c_rate != expect_result["over_c_rate"]:
            raise ValueError("ERROR: Overriding Commission Rate not match: ", self._over_c_rate, expect_result["over_c_rate"])
        elif self._agents != expect_result["agents"]:
            raise ValueError("ERROR: Agents not match: ", self._agents, expect_result["agents"])
        else:
            print("Test Passed")

