from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    def __init__(self, designation, name, diameter, hazardous):
        self.designation = designation
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous

        # an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        return f"{self.designation} ({self.name})"

    def __str__(self):
        article = "is" if self.hazardous else "is not"
        return f"A NearEarthObject {self.fullname} has a diameter of {str(self.diameter)} km and {article} potentially {self.hazardous}"

    def __repr__(self):
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    def __init__(self, time, distance, velocity, designation):
        self.time = cd_to_datetime(time)
        self._designation = designation
        self.distance = distance
        self.velocity = velocity
        self.neo = None

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def __str__(self):
        return f"At {time_str}, '{neo.fullname}' approaches Earth at a distance of {distance:.2f} au and a velocity of {velocity:.2f} km/s."

    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
