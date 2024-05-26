from property import Property

class Comm_Property(Property):
    def __init__(self, address, p_code, tenure, yoc, prop_type, comm_property_type, area, worth, c_rate):
        super().__init__(address, p_code, tenure, yoc, prop_type, area, worth, c_rate)
        self._comm_property_type = comm_property_type

    def get_comm_property_type(self):
        return self._comm_property_type

    def set_comm_property_type(self, comm_prop_type):
        self._comm_property_type = comm_prop_type

    def __str__(self):
        return (
            f"\n>--- PROPERTY INFO ---<\n"
            f"Location: {self._address}\n"
            f"Postal Code: {self._p_code}\n"
            f"Tenure: {self._tenure}\n"
            f"Year of Completion: {self._yoc}\n"
            f"Property Type: {self._prop_type}\n"
            f"Commercial Property Type: {self._comm_property_type}\n"
            f"Area: {self._area}\n"
            f"Valuation: ${self._worth:,.0f}\n"
            f"Commission: ${self._worth * self._c_rate:,.0f}\n"
            )

    def test(self, expect_result):
        if self._address != expect_result["address"]:
            raise ValueError("ERROR: Address not match: ", self._address, expect_result["address"])
        elif self._p_code != expect_result["p_code"]:
            raise ValueError("ERROR: Postal Code not match: ", self._p_code, expect_result["p_code"])
        elif self._tenure != expect_result["tenure"]:
            raise ValueError("ERROR: Tenure not match: ", self._tenure, expect_result["tenure"])
        elif self._yoc != expect_result["yoc"]:
            raise ValueError("ERROR: Year of Completion not match: ", self._yoc, expect_result["yoc"])
        elif self._prop_type != expect_result["prop_type"]:
            raise ValueError("ERROR: Property Type not match: ", self._prop_type, expect_result["prop_type"])
        elif self._comm_property_type != expect_result["comm_property_type"]:
            raise ValueError("ERROR: Commercial Property Type not match: ", self._comm_property_type, expect_result["comm_property_type"])
        elif self._area != expect_result["area"]:
            raise ValueError("ERROR: Area not match: ", self._area, expect_result["area"])
        elif self._worth != expect_result["worth"]:
            raise ValueError("ERROR: Valuation not match: ", self._worth, expect_result["worth"])
        else:
            print("Test Passed")