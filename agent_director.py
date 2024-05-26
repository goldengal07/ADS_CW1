from agent import Prop_Agent

class Prop_Agency_Director(Prop_Agent):
    def __init__(self, company, aid, start_year, over_c_rate=0.05, cs_rate=0.75):
        super().__init__(company, aid, start_year, cs_rate)
        self.over_c_rate = over_c_rate
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def get_over_c_rate(self):
        return self.over_c_rate

    def set_over_c_rate(self, over_c_rate):
        self.over_c_rate = over_c_rate

    def get_agents(self):
        return self.agents

    def set_agents(self, agents):
        self.agents = agents


