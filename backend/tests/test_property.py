import unittest
from domain.property import Property
from domain.property.structures.image import ImageFile
from domain import DomainError


class PropertyTestCase(unittest.TestCase):

    def test_small_name_raises(self):
        prop = Property('small')
        self.assertRaises(DomainError, prop.has_valid_name)

    def test_no_images_raises(self):
        prop = Property("Valid Name For Property")
        self.assertRaises(DomainError, prop.raise_for_invalid_property)

    def test_two_images_or_less_raises(self):
        prop = Property("Valid Name For Property", photos=[
            ImageFile('any', 'image/png', b'/xa0'),
            ImageFile('any2', 'image/png', b'/xa0')
        ])
        self.assertRaises(DomainError, prop.raise_for_invalid_property)

    def test_images_with_same_name_raises(self):
        prop = Property("Valid Name For Property", photos=[
            ImageFile('any', 'image/png', b'/xa0'),
            ImageFile('any', 'image/png', b'/xa0')
        ])
        self.assertRaises(DomainError, prop.raise_for_invalid_property)

    def test_too_many_images_raises(self):
        prop = Property("Valid Name For Property", photos=[
            ImageFile('any', 'image/png', b'/xa0'),
            ImageFile('any2', 'image/png', b'/xa0'),
            ImageFile('any3', 'image/png', b'/xa0'),
            ImageFile('any4', 'image/png', b'/xa0'),
            ImageFile('any5', 'image/png', b'/xa0'),
            ImageFile('any6', 'image/png', b'/xa0')
        ])
        self.assertRaises(DomainError, prop.raise_for_invalid_property)
    
    def test_good_object_not_raises(self):
        prop = Property("Valid Name For Property", photos=[
            ImageFile('any', 'image/png', b'/xa0'),
            ImageFile('any2', 'image/png', b'/xa0'),
            ImageFile('any3', 'image/png', b'/xa0'),
        ])
        self.assertIsNone(prop.raise_for_invalid_property())


if __name__ == '__main__':
    unittest.main()