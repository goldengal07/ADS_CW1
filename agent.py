

class Prop_Agent:
    def __init__(self, company, aid, start_year, cs_rate=0.7):
        self._unsold_properties = []
        self._sold_properties = []
        self._cs_rate = cs_rate      # Commission Sharing Rate
        self._company = company
        self._aid = aid              # Agent Registration Number
        self._start_year = start_year

    def add_unsold_property(self, property):
        self._unsold_properties.append(property)

    def add_sold_property(self, property):
        self._sold_properties.append(property)

    def sell_property(self, property):
        if property in self._unsold_properties:
            self._unsold_properties.remove(property)
            self._sold_properties.append(property)
            print(f"\n[SUCCESS] {self._aid} sold {property.get_address()}")
        else:
            print("Property not found in unsold properties list.")

    def print_unsold_properties(self):
        print(f"Unsold Properties for Agent {self._aid}:")
        for property in self._unsold_properties:
            print(f"- {property.get_address()}")

    def get_company(self):
        return self._company

    def set_company(self, company):
        self._company = company

    def get_sold_properties(self):
        return self._sold_properties

    def get_unsold_properties(self):
        return self._unsold_properties

    def get_aid(self):
        return self._aid

    def set_aid(self, aid):
        self._aid = aid

    def get_start_year(self):
        return self._start_year

    def set_start_year(self, start_year):
        self._start_year = start_year

    def get_cs_rate(self):
        return self._cs_rate

    def set_cs_rate(self, cs_rate):
        self._cs_rate = cs_rate

    def __str__(self):
        return (
            f"\n>--- AGENT INFO ---<\n"
            f"Company: {self._company}\n"
            f"ID: {self._aid}\n"
            f"Employment Year: {self._start_year}\n"
            f"Commission Rate: {self._cs_rate}\n"
            f"Sold Properties: {self._sold_properties}\n"
            f"Unsold Properties: {self._unsold_properties}\n"
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
        elif self._sold_properties != expect_result["sold"]:
            raise ValueError("ERROR: Sold Properties not match: ", self._sold_properties, expect_result["sold"])
        elif self._unsold_properties != expect_result["unsold"]:
            raise ValueError("ERROR: Unsold Properties not match: ", self._unsold_properties, expect_result["unsold"])
        else:
            print("Test Passed")
