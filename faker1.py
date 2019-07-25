#from faker import Faker
from faker import Factory

fake1 = Factory.create()

for _ in range(5):
    print(fake1.name())
