from faker import Faker
from datetime import date
from random import randint
from djbooks.models import Publisher, Author, Book

fake = Faker('de_DE')

for _ in range(15):
    name = fake.company()
    address = fake.street_address()
    city = fake.city()
    country = fake.country()
    website = 'www.' + fake.domain_name()
    p = Publisher(name = fake.company(), address = fake.street_address(), city = fake.city(), country = fake.country(), website = 'www.' + fake.domain_name())

'''
    b = Book(title=fake.text(max_nb_chars=25), authors=Author.objects.get(id=randint(1,10)), publisher=Publisher.objects.get(id=randint(1,5)), date=fake.date_this_century())
    name
    address 
    city 
    country 
    website 
for i in range(25):
    b = Book(title=fake.text(max_nb_chars=25), publisher=Publisher.objects.get(id=randint(1,5)), publication_date=fake.date_this_century())
    b.save()
    a = Author.objects.get(id=randint(1,10))
    a.book_set.set([b])

'''