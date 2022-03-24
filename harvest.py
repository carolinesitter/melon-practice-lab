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
        "seedless", 
        "bestseller", 
        "Muskmelon")
    melon_musk.add_pairing("mint")
    
    melon_casaba = MelonType(
        "cas", 
        "2003", 
        "orange", 
        "has seeds",
        "None", 
        "Casaba")
    melon_casaba.add_pairing("strawberries")
    melon_casaba.add_pairing("mint")

    melon_cren = MelonType(
        "cren",
        "1996",
        "green",
        "has seeds",
        "None",
        "Crenshaw"
    )
    melon_cren.add_pairing("prosciutto")

    melon_yellow_w = MelonType(
        "yw", 
        "2013", 
        "yellow", 
        "has seeds", 
        "bestseller", 
        "Yellow Watermelon")
    melon_yellow_w.add_pairing("ice cream")


    all_melon_types.extend([melon_musk, melon_casaba, melon_cren, melon_yellow_w])


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # we only need to loop through melon types
    for item in melon_types:            
        print(f"{item.name} pairs with ")

        # loop through the list to grab each pairing item 
        for pair in item.pairings:
            print(f"- {pair}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
