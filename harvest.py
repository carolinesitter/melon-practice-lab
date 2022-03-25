############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):

        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    melon_musk = MelonType(
        "musk", 
        "1998", 
        "green",
        "True", 
        "True", 
        "Muskmelon")
    melon_musk.add_pairing("mint")
    
    melon_casaba = MelonType(
        "cas", 
        "2003", 
        "orange", 
        "False",
        "False", 
        "Casaba")
    melon_casaba.add_pairing("strawberries")
    melon_casaba.add_pairing("mint")

    melon_cren = MelonType(
        "cren",
        "1996",
        "green",
        "False",
        "False",
        "Crenshaw"
    )
    melon_cren.add_pairing("prosciutto")

    melon_yellow_w = MelonType(
        "yw", 
        "2013", 
        "yellow", 
        "False", 
        "True", 
        "Yellow Watermelon")
    melon_yellow_w.add_pairing("ice cream")


    all_melon_types.extend([melon_musk, melon_casaba,
     melon_cren, melon_yellow_w])


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # we only need to loop through melon types
    for melon in melon_types:            
        print(f"{melon.name} pairs with ")

        # loop through the list to grab each pairing item 
        for pair in melon.pairings:
            print(f"- {pair}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons_dictionary = {}
    for melon in melon_types:
        melons_dictionary[melon.code] = melon

    for key, value in melons_dictionary.items():
        print(f"{key} : {value}")
    
    return melons_dictionary

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest

    def __init__(self, melon_type, shape_rating,
     color_rating, harvest_field, harvester):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvester = harvester

    def is_sellable(self, sellable):
        
        if self.shape_rating < 5 and self.color_rating > 5 and self.harvest_field != 3:

             sellability = "This melon can be sold!"

        else:

            sellability = "Oh no! This melon cannot be sold!"
            
        return sellability



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

    melon_list = []

    melon_1 = Melon("yw", 8, 7, 2, "Sheila")
    melon_2 = Melon("yw", 3, 4, 2, "Sheila")
    melon_3 = Melon("yw", 9, 8, 2, "Sheila")
    melon_4 = Melon("cas", 10, 6, 35, "Sheila")
    melon_5 = Melon("cren", 8, 9, 35, "Micheal")
    melon_6 = Melon("cren", 8, 2, 35, "Micheal")
    melon_7 = Melon("cren", 2, 3, 4, "Micheal")
    melon_8 = Melon("musk", 6, 7, 4, "Micheal")
    melon_9 = Melon("yw", 7, 10, 3, "Sheila")

    melon_list.extend([melon_1, melon_2, melon_3, melon_4,
     melon_5, melon_6, melon_7, melon_8, melon_9])

    return melon_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
