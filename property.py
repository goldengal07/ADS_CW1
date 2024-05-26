
class Property:
    def __init__(self, address, p_code, tenure, yoc, prop_type, area, worth, c_rate=0.01):
        self._address = address
        self._p_code = p_code   # Postal Code
        self._tenure = tenure
        self._yoc = yoc         # Year of Completion
        self._prop_type = prop_type
        self._area = area
        self._c_rate = c_rate    # Default to 1%
        self._worth = worth     # Valuation

    # Accessor and Modifier for each protected attribute
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_p_code(self):
        return self._p_code

    def set_p_code(self, p_code):
        self._p_code = p_code

    def get_tenure(self):
        return self._tenure

    def set_tenure(self, tenure):
        self._tenure = tenure

    def get_yoc(self):
        return self._yoc

    def set_yoc(self, yoc):
        self._yoc = yoc

    def get_prop_type(self):
        return self._prop_type

    def set_prop_type(self, prop_type):
        self._prop_type = prop_type

    def get_area(self):
        return self._area

    def set_area(self, area):
        self._area = area

    def get_worth(self):
        return self._worth

    def set_worth(self, worth):
        self._worth = worth

    def get_c_rate(self):
        return self._c_rate

    def set_c_rate(self, c_rate):
        self._c_rate = c_rate

    def __str__(self):
        return (
            f"\n>--- PROPERTY INFO ---<\n"
            f"Location: {self._address}\n"
            f"Postal Code: {self._p_code}\n"
            f"Tenure: {self._tenure}\n"
            f"Year of Completion: {self._yoc}\n"
            f"Property Type: {self._prop_type}\n"
            f"Area: {self._area}\n"
            f"Valuation: ${self._worth:,.0f}\n"
            f"Commission: ${self._worth * self._c_rate:,.0f}\n"
            )

    # ERROR CHECKING AND ERROR LOG
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
        elif self._area != expect_result["area"]:
            raise ValueError("ERROR: Area not match: ", self._area, expect_result["area"])
        elif self._worth != expect_result["worth"]:
            raise ValueError("ERROR: Valuation not match: ", self._worth, expect_result["worth"])
        else:
            print("Test Passed")