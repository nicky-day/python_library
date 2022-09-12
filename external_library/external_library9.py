from faker import Faker

fake = Faker()
fake.name()

fake = Faker("ko-KR")
fake.name()
fake.address()

test_data = [(fake.name(), fake.address()) for i in range(30)]
