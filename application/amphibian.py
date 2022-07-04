
class AmphibianData:
    """

    Class Representing the data scraped from the data source with additional helper methods


    """

    def __init__(self, amp_info: list) -> None:
        self.position = amp_info[0]
        self.order = amp_info[1]
        self.family = amp_info[2]
        self.genus = amp_info[3]
        self.species = amp_info[4]
        self.body_size_male = amp_info[5]
        self.body_size_female = amp_info[6]
        self.nesting_site = amp_info[7]
        self.fecundity = amp_info[8]
        self.age_maturity = amp_info[9]
        self.egg_hatching = amp_info[10]
        self.metamorphosis = amp_info[11]
        self.parity_mode = amp_info[12]
        self.egg_diameter = amp_info[13]
        self.activity = amp_info[14]
        self.micro_habitat = amp_info[15]
        self.geography = amp_info[16]
        self.image_url_male = ""
        self.image_url_female = ""

    def get_full_name(self) -> str:
        return f"{self.order} {self.family} {self.genus} {self.species}"

    def get_short_name(self) -> str:
        return f"{self.genus} {self.species}"

    def get_image_url(self) -> str:
        return ""

    def has_image_url(self):
        return self.image_url_male != "" and self.image_url_female != ""