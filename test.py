from vehicle import Vehicle, Car, Plane, Boat
import test
from smartphone import Smartphone, AdvancedSmartphone


def test_smartphone_str():
    phone = Smartphone("Nokia", "3310", 2)
    assert str(phone) == "Nokia 3310 (2GB)"


def test_smartphone_call():
    phone = Smartphone("Nokia", "3310", 2)
    assert "is calling" in phone.call("+254782852499")


def test_advanced_smartphone_inherits_smartphone():
    phone = AdvancedSmartphone("Samsung", "S24 Ultra", 256, 108)
    assert isinstance(phone, Smartphone)
    assert isinstance(phone, AdvancedSmartphone)


def test_advanced_smartphone_take_photo():
    phone = AdvancedSmartphone("Samsung", "S24 Ultra", 256, 108)
    assert "Taking a 108MP photo!" == phone.take_photo()


def test_advanced_smartphone_overrides_call():
    phone = AdvancedSmartphone("Samsung", "S24 Ultra", 256, 108)
    assert "(video call)" in phone.call("+254719852400")


def test_vehicle_move():
    v = Vehicle()
    assert v.move() == "Vehicle is moving..."


def test_car_move():
    c = Car()
    assert c.move() == "🚗 Driving on the road"


def test_plane_move():
    p = Plane()
    assert p.move() == "✈️ Flying in the sky"


def test_boat_move():
    b = Boat()
    assert b.move() == "🚤 Sailing on the water"


def test_polymorphism():
    vehicles = [Car(), Plane(), Boat()]
    moves = [v.move() for v in vehicles]
    assert "🚗 Driving on the road" in moves
    assert "✈️ Flying in the sky" in moves
    assert "🚤 Sailing on the water" in moves