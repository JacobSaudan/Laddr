import random
from laddr_site.models import *


def create_solo_match(user):
	count = User.objects.all().count()
	random_index = randint(0, count - 1)
	return User.objects.all()[random_index]

def update_psyche(profile, comp_profile):
	# Updates by simple average
	n = profile.num_profiles_ranked
	if (n != PsychePreference.objects.filter(user=profile).len() - 1):
		raise RuntimeError('Number of profiles ranked does not match number of psyche preferences.')
	t_pref, j_pref, s_pref = profile.preferred_timmy_rank, profile.preferred_johnny_rank, profile.preferred_spike_rank
	t_comp, j_comp, s_comp = comp_profile.timmy_rank, comp_profile.johnny_rank, comp_profile.spike_rank
	t_pref = update_average(t_pref, n, t_comp)
	j_pref = update_average(j_pref, n, j_comp)
	s_comp = update_average(s_pref, n, s_comp)
	profile.preferred_timmy_rank = t_pref
	profile.preferred_johnny_rank = j_pref
	profile.preferred_spike_rank = s_pref
	profile.num_profiles_ranked = n + 1
	profile.save()


def update_average(prev_avg, prev_n, new_value):
	if prev_avg == None:
		return new_value
	return ((prev_avg * prev_n) + new_value) / (prev_n + 1)
