"""class smartphone."""


class Smartphone:
    """Base class representing a basic smartphone."""

    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB)"


class AdvancedSmartphone(Smartphone):
    """Subclass that adds extra features."""

    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a {self.camera_megapixels}MP photo!"

    def call(self, number):
        # Polymorphism: override base call method
        return f"{self.brand} {self.model} (video call) to {number}..."


if __name__ == "__main__":
    phone1 = Smartphone("Nokia", "3310", 2)
    phone2 = AdvancedSmartphone("Samsung", "S24 Ultra", 256, 108)

    print(phone1)
    print(phone1.call("+254759606091"))

    print(phone2)
    print(phone2.take_photo())
    print(phone2.call("+254759060168"))