"""Amphibian.

AmphibianData class and associated methods. Used to represent the amphibian
data from the dataset/database to insert into the create pdf process.

"""


class AmphibianData:
    """AmphibianData.

    Class Representing the data scraped from the data source with additional
    helper methods

    Args:
        amp_info: list passed to init

    """

    def __init__(self, amp_info: list) -> None:
        """Init method for Amphibian Data.

        Instantiates AmphibianData class.

        Args:
            amp_info: amphibian info list

        """
        self.position = amp_info[0]
        self.order = amp_info[1]
        self.family = amp_info[2]
        self.genus = amp_info[3]
        self.species = amp_info[4]
        self.SVLMx = self.get_SVLMx(amp_info)
        self.longevity = amp_info[8]
        self.nesting_site = amp_info[9]
        self.clutch = self.get_clutch(amp_info)
        self.parity_mode = amp_info[13]
        self.egg_diameter = amp_info[14]
        self.activity = amp_info[15]
        self.micro_habitat = amp_info[16]
        self.geographic_region = self.get_geographic_regions(amp_info)
        self.IUCN = amp_info[18]
        self.pop_trend = amp_info[19]
        self.range_size = amp_info[20]
        self.elevation = self.get_elevation(amp_info)
        self.image_url_male = ""
        self.image_url_female = ""

        # fecundity, egg hatching, age maturity, metamorphosis are missing

    def get_geographic_regions(self, amp_info: list) -> str:
        geo = amp_info[17]
        geo = geo.split(",")
        geo_n = []
        for g in geo:
            a = g.replace(" Nocountry", "")
            a = a.replace("Noregion", "")
            geo_n.append(a)
        geo_set = {x for x in geo_n}
        geo_l = [*geo_set]
        return "/".join(geo_l)

    def get_SVLMx(self, amp_info: list) -> str:
        """Get SVLMx."""
        SVLMx = f"Male: {amp_info[5]}"
        SVLMx += f"{' ' * (10 - len('male: ' + str(amp_info[5])))}| "
        SVLMx += (
            f"Female: {amp_info[6]}{' ' * (10 - len('Female: ' + str(amp_info[6])))}|"
        )
        SVLMx += f" Average: {amp_info[7]}"

        return SVLMx

    def get_clutch(self, amp_info: list) -> str:
        """Get Clutch."""
        clutch = f"Min: {amp_info[10]}{' ' * (10 - len('min: ' + str(amp_info[10])))}| "
        clutch += (
            f"Max: {amp_info[11]}{' ' * (10 - len('max: ' + str(amp_info[11])))}| "
        )
        clutch += f"Average: {amp_info[12]}"

        return clutch

    def get_elevation(self, amp_info: list) -> str:
        """Get Elevation."""
        elevation = (
            f"Min: {amp_info[21]}{' ' * (10 - len('min: ' + str(amp_info[21])))}| "
        )
        elevation += (
            f"Max: {amp_info[22]}{' ' * (10 - len('max: ' + str(amp_info[22])))}| "
        )
        elevation += f"Average: {amp_info[23]}"

        return elevation

    def get_full_name(self) -> str:
        """Get full name.

        Returns the string of the combination of the Amphibian Object's order
        family genus and species

        Return:
            full_name(str)

        """
        return f"{self.order} {self.family} {self.genus} {self.species}"

    def get_short_name(self) -> str:
        """Get short name.

        Returns the string of the combination of the Amphibian Object's genus and
        species

        Return:
            short_name(str)

        """
        return f"{self.genus} {self.species}"

    def get_image_url(self) -> str:
        """Get image url.

        Returns the string of the image url

        Currently unimplemented
        """
        return ""

    def has_image_url(self) -> bool:
        """Check if class has image url.

        Returns boolean value based on the contents of the image_url_male
        and image_url_female properties

        Return:
            bool
        """
        return self.image_url_male != "" and self.image_url_female != ""
