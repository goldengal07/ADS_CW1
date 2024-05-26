from property import Property
from comm_property import Comm_Property
from agent import Prop_Agent
from agent_director import Prop_Agency_Director
from commission_slip import Commission_Slip

def main():
    # Create some properties
    property1 = Property("Block 605 Bishan #06-098", 133456, "Freehold", 2004, "Residence", "Bishan", 22000000,0.015)
    property2 = Comm_Property("Building A #09-456 Paya Lebar Square", 654321, "Leasehold", 2015, "Commercial", "Office",
                              "Downtown", 14000000,0.01)
    property3 = Property("61 Choa Chu Kang Loop Northvale Block 71B #01-11", 689673, "Leasehold", 2012, "Apartment", "Choa Chu Kang",
                              14000000, 0.01)
    property4 = Property("2 Tanjong Pagar Plaza", 169119, "Leasehold", 1976, "HDB Flat", "Tanjong Pagar",
                              500000, 0.01)
    property5 = Comm_Property("The Adelphi 1 Coleman Street", 179803, "Leasehold", 2016, "Commercial", "Office","City Hall", 14500000,0.01)
    property6 = Comm_Property("The Central 8 Eu Tong Sen Street", 159818, "Leasehold", 2016, "Commercial", "Office","Raffles PLace", 4860000,0.02)
    property7 = Property("Block 104 HDB Jalan Rajah", 321104, "Leasehold", 1983, "5A HDB Flat", "Toa Payoh",
                              848000, 0.01)
    property8 = Comm_Property("Peninsula Plaza 111 North Bridge Road", 179098, "Leasehold", 2010, "Commercial", "Office","City Hall", 1190000,0.01)
    property9 = Property("15 Beach Road", 190015, "Leasehold", 1974, "4A HDB Flat", "Bugis",
                         725000, 0.01)
    property10 = Comm_Property("148 Cecil Street Singapore", 169545, "Freehold", 2020, "Commercial", "Office",
                              "Raffles Place", 51700000, 0.02)
    property11 = Comm_Property("Orchard Gateway 277 Orchard Road", 238858, "Leasehold", 2018, "Commercial", "Office",
                               "Orchard", 5200000, 0.015)
    property12 = Property("Block 112 HDB Bukit Batok", 650112, "Leasehold", 1990, "4A HDB Flat", "Bukit Batok",
                          900000, 0.012)
    property13 = Comm_Property("Suntec Tower 3 Temasek Boulevard", 638983, "Leasehold", 2015, "Commercial", "Office",
    "Marina Centre", 13000000, 0.01)
    property14 = Property("3 Marine Drive", 440003, "Leasehold", 1978, "HDB Flat", "Marine Parade",
                          550000, 0.011)
    property15 = Comm_Property("One Raffles Place", 248616, "Leasehold", 2017, "Commercial", "Office",
    "Raffles Place", 14800000, 0.011)
    property16 = Comm_Property("Bugis Junction Tower", 188024, "Leasehold", 2016, "Commercial", "Office",
                               "Bugis", 4500000, 0.018)
    property17 = Property("Block 320 HDB Tampines Street 33", 520320, "Leasehold", 1995, "5I HDB Flat", "Tampines",
                          860000, 0.014)
    property18 = Comm_Property("Paya Lebar Square 60 Paya Lebar Road", 409051, "Leasehold", 2014, "Commercial",
                               "Office",
                               "Paya Lebar", 11000000, 0.013)
    property19 = Property("6 Holland Close", 271006, "Leasehold", 1975, "HDB Flat", "Holland",
                          510000, 0.012)
    property20 = Comm_Property("Mapletree Business City 10 Pasir Panjang Road", 117438, "Leasehold", 2013, "Commercial",
                               "Office",
                               "HarbourFront", 9500000, 0.014)
    property21 = Comm_Property("Fusionopolis One-North 1 Fusionopolis Place", 138632, "Leasehold", 2017, "Commercial",
                               "Office",
                               "One-North", 6800000, 0.017)
    property22 = Property("Block 55 HDB Ang Mo Kio Avenue 3", 569933, "Leasehold", 1986, "4A HDB Flat", "Ang Mo Kio",
                          820000, 0.013)
    property23 = Comm_Property("Westgate Tower 1 Gateway Drive", 608531, "Leasehold", 2014, "Commercial", "Office",
                               "Jurong East", 9800000, 0.011)
    property24 = Property("7 Serangoon North Avenue 5", 554910, "Leasehold", 1981, "HDB Flat", "Serangoon",
                          570000, 0.015)
    property25 = Comm_Property("Asia Square Tower 1", 918960, "Leasehold", 2011, "Commercial", "Office",
    "Marina Bay", 15000000, 0.012)
    property26 = Comm_Property("Frasers Tower 182 Cecil Street", 669547, "Leasehold", 2018, "Commercial", "Office",
    "Tanjong Pagar", 4900000, 0.016)
    property27 = Property("Block 325 HDB Clementi Avenue 5", 120325, "Leasehold", 1987, "5I HDB Flat", "Clementi",
                          870000, 0.011)
    property28 = Comm_Property("Guoco Tower 1 Wallich Street", 578881, "Leasehold", 2016, "Commercial", "Office",
    "Tanjong Pagar", 13800000, 0.012)
    property29 = Property("9 Ghim Moh Road", 270009, "Leasehold", 1976, "HDB Flat", "Ghim Moh",
                          530000, 0.012)
    property30 = Comm_Property("Capital Tower 168 Robinson Road", 568912, "Leasehold", 2010, "Commercial", "Office",
    "Downtown Core", 14600000, 0.012)
    property31 = Comm_Property("AXA Tower 8 Shenton Way", 468811, "Leasehold", 2014, "Commercial", "Office",
    "Tanjong Pagar", 6700000, 0.019)
    property32 = Property("Block 111 HDB Yishun Ring Road", 760111, "Leasehold", 1993, "5I HDB Flat", "Yishun",
                          860000, 0.012)
    property33 = Comm_Property("Ocean Financial Centre 10 Collyer Quay", 749315, "Leasehold", 2011, "Commercial", "Office",
    "Raffles Place", 13500000, 0.014)
    property34 = Property("2 Bedok South Avenue 1", 460002, "Leasehold", 1979, "HDB Flat", "Bedok",
                          550000, 0.012)
    property35 = Comm_Property("Samsung Hub 3 Church Street", 449483, "Leasehold", 2013, "Commercial", "Office",
    "Raffles Place", 14000000, 0.012)
    property36 = Comm_Property("One George Street 1 George Street", 249145, "Leasehold", 2014, "Commercial", "Office",
    "Boat Quay", 6900000, 0.02)
    property37 = Property("Block 456 HDB Pasir Ris Drive 4", 510456, "Leasehold", 1997, "5I HDB Flat", "Pasir Ris",
                          880000, 0.014)
    property38 = Comm_Property("UOB Plaza 1 80 Raffles Place", 948624, "Leasehold", 2012, "Commercial", "Office",
    "Raffles Place", 13200000, 0.012)
    property39 = Property("4 Jalan Bukit Merah", 150004, "Leasehold", 1980, "HDB Flat", "Bukit Merah",
                          580000, 0.012)
    property40 = Comm_Property("Marina One East Tower", 578936, "Leasehold", 2017, "Commercial", "Office",
    "Marina Bay", 14500000, 0.012)
    property41 = Comm_Property("PSA Building 460 Alexandra Road", 119963, "Leasehold", 2015, "Commercial", "Office",
                               "Alexandra", 4800000, 0.017)
    property42 = Property("Block 789 HDB Woodlands Avenue 6", 730789, "Leasehold", 1995, "5I HDB Flat", "Woodlands",
                          850000, 0.013)
    property43 = Comm_Property("Raffles City Tower 250 North Bridge Road", 179101, "Leasehold", 2014, "Commercial","Office",
                               "City Hall", 12500000, 0.013)
    property44 = Property("3 Telok Blangah Crescent", 590003, "Leasehold", 1982, "HDB Flat", "Telok Blangah",
    540000, 0.011)
    property45 = Comm_Property("The Gateway East 152 Beach Road", 189721, "Leasehold", 2016, "Commercial", "Office",
                               "Bugis", 14700000, 0.014)
    property46 = Comm_Property("Visioncrest Commercial 103 Penang Road", 238467, "Leasehold", 2017, "Commercial",
                               "Office",
                               "Dhoby Ghaut", 5300000, 0.016)
    property47 = Property("Block 101 HDB Jurong East Street 13", 600101, "Leasehold", 1984, "5A HDB Flat",
                          "Jurong East",
                          880000, 0.012)
    property48 = Comm_Property("HarbourFront Tower One 1 HarbourFront Place", 998633, "Leasehold", 2013, "Commercial", "Office",
    "HarbourFront", 14900000, 0.013)
    property49 = Property("6 Dakota Crescent", 390006, "Leasehold", 1980, "HDB Flat", "Dakota",
                          570000, 0.011)
    property50 = Comm_Property("Mapletree Anson 60 Anson Road", 769914, "Leasehold", 2014, "Commercial", "Office",
    "Tanjong Pagar", 14500000, 0.013)
    property51 = Comm_Property("Republic Plaza 9 Raffles Place", 648619, "Leasehold", 2012, "Commercial", "Office",
    "Raffles Place", 4900000, 0.018)
    property52 = Property("Block 305 HDB Ubi Avenue 1", 400305, "Leasehold", 1986, "4A HDB Flat", "Ubi",
                          830000, 0.013)
    property53 = Comm_Property("One Marina Boulevard", 218989, "Leasehold", 2015, "Commercial", "Office",
    "Marina Bay", 12000000, 0.014)
    property54 = Property("2 Commonwealth Avenue", 140002, "Leasehold", 1977, "HDB Flat", "Commonwealth",
                          510000, 0.011)
    property55 = Comm_Property("OCBC Centre 65 Chulia Street", 259513, "Leasehold", 2014, "Commercial", "Office",
    "Raffles Place", 14200000, 0.013)
    property56 = Comm_Property("City House 36 Robinson Road", 980877, "Leasehold", 2017, "Commercial", "Office",
    "Raffles Place", 4700000, 0.016)
    property57 = Property("Block 201 HDB Hougang Street 21", 530201, "Leasehold", 1993, "5I HDB Flat", "Hougang",
                          810000, 0.012)
    property58 = Comm_Property("Springleaf Tower 3 Anson Road", 379909, "Leasehold", 2014, "Commercial", "Office",
    "Tanjong Pagar", 11800000, 0.012)
    property59 = Property("5 Chai Chee Road", 461005, "Leasehold", 1981, "HDB Flat", "Chai Chee",
                          540000, 0.011)
    property60 = Comm_Property("Twenty Anson 20 Anson Road", 879912, "Leasehold", 2016, "Commercial", "Office",
    "Tanjong Pagar", 14400000, 0.012)
    property61 = Comm_Property("6 Battery Road", 549909, "Leasehold", 2017, "Commercial", "Office",
    "Raffles Place", 4850000, 0.019)
    property62 = Property("Block 121 HDB Bishan Street 12", 570121, "Leasehold", 1987, "4A HDB Flat", "Bishan",
                          830000, 0.012)
    property63 = Comm_Property("Robinson 77 77 Robinson Road", 668896, "Leasehold", 2014, "Commercial", "Office",
    "Tanjong Pagar", 11300000, 0.012)
    property64 = Comm_Property("OUE Downtown 6 Shenton Way", 468809, "Leasehold", 2016, "Commercial", "Office",
    "Downtown Core", 15000000, 0.015)

    # Create directors
    director1 = Prop_Agency_Director("Real Estate Co", "D44556", 2015)
    # Add Director Properties
    director1.add_sold_property(property49)
    director1.add_sold_property(property50)
    director1.add_sold_property(property51)
    director1.add_unsold_property(property52)
    director1.add_unsold_property(property53)
    director1.add_unsold_property(property54)
    director1.add_unsold_property(property55)
    director1.add_unsold_property(property56)

    director2 = Prop_Agency_Director("Property Guru Co", "E77889", 2016)
    director2.add_sold_property(property57)
    director2.add_sold_property(property58)
    director2.add_sold_property(property59)
    director2.add_unsold_property(property60)
    director2.add_unsold_property(property61)
    director2.add_unsold_property(property62)
    director2.add_unsold_property(property63)
    director2.add_unsold_property(property64)

    # Create agents
    agent1 = Prop_Agent("Real Estate Co", "A12345", 2018,director1)
    agent1.add_sold_property(property1)
    agent1.add_sold_property(property2)
    agent1.add_sold_property(property3)
    agent1.add_unsold_property(property4)
    agent1.add_unsold_property(property5)
    agent1.add_unsold_property(property6)
    agent1.add_unsold_property(property7)
    agent1.add_unsold_property(property8)

    # Sell properties
    print("Before Selling")
    agent1.print_unsold_properties()
    agent1.sell_property(property4)
    print("\nAfter Selling")
    agent1.print_unsold_properties()

    agent2 = Prop_Agent("Real Estate Co", "B67890", 2019, director1)
    agent2.add_sold_property(property9)
    agent2.add_sold_property(property10)
    agent2.add_sold_property(property11)
    agent2.add_unsold_property(property12)
    agent2.add_unsold_property(property13)
    agent2.add_unsold_property(property14)
    agent2.add_unsold_property(property15)
    agent2.add_unsold_property(property16)

    agent3 = Prop_Agent("Real Estate Co", "C11223", 2020, director1)
    agent3.add_sold_property(property17)
    agent3.add_sold_property(property18)
    agent3.add_sold_property(property19)
    agent3.add_unsold_property(property20)
    agent3.add_unsold_property(property21)
    agent3.add_unsold_property(property22)
    agent3.add_unsold_property(property23)
    agent3.add_unsold_property(property24)

    agent4 = Prop_Agent("Property Guru Co", "A23456", 2018, director2)
    agent4.add_sold_property(property25)
    agent4.add_sold_property(property26)
    agent4.add_sold_property(property27)
    agent4.add_unsold_property(property28)
    agent4.add_unsold_property(property29)
    agent4.add_unsold_property(property30)
    agent4.add_unsold_property(property31)
    agent4.add_unsold_property(property32)

    agent5 = Prop_Agent("Property Guru Co", "B78901", 2019, director2)
    agent5.add_sold_property(property33)
    agent5.add_sold_property(property34)
    agent5.add_sold_property(property35)
    agent5.add_unsold_property(property36)
    agent5.add_unsold_property(property37)
    agent5.add_unsold_property(property38)
    agent5.add_unsold_property(property39)
    agent5.add_unsold_property(property40)

    agent6 = Prop_Agent("Property Guru Co", "C22334", 2020, director2)
    agent6.add_sold_property(property41)
    agent6.add_sold_property(property42)
    agent6.add_sold_property(property43)
    agent6.add_unsold_property(property44)
    agent6.add_unsold_property(property45)
    agent6.add_unsold_property(property46)
    agent6.add_unsold_property(property47)
    agent6.add_unsold_property(property48)

    # Add agents to director
    director1.add_agent(agent1)
    director1.add_agent(agent2)
    director1.add_agent(agent3)

    director2.add_agent(agent4)
    director2.add_agent(agent5)
    director2.add_agent(agent6)


    # Print commission slips
    Commission_Slip.print_commission_slip(agent1)
    Commission_Slip.print_commission_slip(agent2)
    Commission_Slip.print_commission_slip(agent3)
    Commission_Slip.print_commission_slip(agent4)
    Commission_Slip.print_commission_slip(agent5)
    Commission_Slip.print_commission_slip(agent6)
    Commission_Slip.print_commission_slip(director1)
    Commission_Slip.print_commission_slip(director2)


if __name__ == "__main__":
    main()