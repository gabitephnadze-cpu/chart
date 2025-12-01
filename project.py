from faker import Faker

fake = Faker()
fake_names = []
for i in range(1000):
    fake_names.append(fake.name())
