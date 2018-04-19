import random
from laddr_site.models import *


def create_solo_match(user):
	count = User.objects.all().count()
	random_index = randint(0, count - 1)
	return User.objects.all()[random_index]
