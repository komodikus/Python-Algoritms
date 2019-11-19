from collections import OrderedDict


class BC(tuple):
    def __new__(cls, *args):
        if len(args) > len(cls.__dict__["fields"]):
            raise AttributeError
        for attr, arg in zip(cls.__dict__["fields"], args):
            setattr(cls, str(attr), arg)
        return super().__new__(cls, args)

    def __repr__(self):
        return "{}({})".format(self._name, self.fields)

    def __setattr__(self, key, value):
        raise AttributeError

    def asdict(self):
        return OrderedDict(zip(self.fields, self))


class namedtuple:

    def __new__(cls, name, fields):
        return type(name, (BC,), {"fields": fields, "_name": name})


My_Car = namedtuple('Car', ['speed', 'year', 'color'])
car_ex = My_Car('144 km/h', '1994', 'yellow')

print('#' * 80)

print(car_ex)
print(car_ex.fields)
# print(car_ex._name)
print(car_ex.speed)
print(car_ex.year)
print(car_ex.asdict())

print('#' * 80)
try:
    car_ex.speed = 1
    print(car_ex.speed)
except:
    print('ASJDJASJDAJSDJ')
