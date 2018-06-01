from laddr_site.models import *
from django.utils.timezone import now


def create_test_users(n):
	"""
	Creates test user objects for fixtures
	Returns 1 on error 0 on success
	"""
	for i in range(n * 5):
		uname = "Test_User_{0}".format(i)
		if len(User.objects.filter(username=uname)) > 0:
			User.objects.get(username=uname).delete()
		user = User.objects.create(username=uname)
		profile = Profile.objects.create(user=user,
										 summoner_name=uname,
										 is_real=False)
		Membership.objects.create(user=user,
								  team=Team.objects.get(name="Test_Team_{0}".format(int(i/5))),
								  date_joined=now())

def create_test_teams(n):
	for i in range(n):
		tname = "Test_Team_{0}".format(i)
		if len(Team.objects.filter(name=tname)) > 0:
			Team.objects.get(name=tname).delete()
		team = Team.objects.create(name=tname,
								   date_created=now(),
								   is_real=False)

def make_fixture_objects(n):
	create_test_teams(n)
	create_test_users(n)
