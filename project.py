from faker import Faker

fake = Faker()
fake_names = []
for i in range(500):
    fake_names.append(fake.name())

print('hello')