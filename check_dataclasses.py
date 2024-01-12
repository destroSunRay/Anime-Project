from dataclasses import dataclass, asdict

@dataclass
class Item:
    name: str
    price: float
    sku: str

    def discount(self) -> float:
        return price*0.8

camera = Item(name='DSLR', price=299.99, sku='CAM123')
camera2 = Item(name='DSLR', price=399.99, sku='CAM123')

print(asdict(camera))

a={'a':1,'b':{'c':1}}
b={'b':{'c':2,'d':2},'c':1}

a.update(b)
a.update(asdict(camera))
print(a)
