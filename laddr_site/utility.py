from laddr_site.models import *
import random 


def create_solo_match(user):
    count = User.objects.all().count()
    random_index = randint(0, count - 1)
    return User.objects.all()[random_index]


def update_psyche(profile, comp_profile):
    # Updates by simple average
    n = profile.num_profiles_ranked
    if n != PsychePreference.objects.filter(user=profile).len() - 1:
        raise RuntimeError(
            "Number of profiles ranked does not match number of psyche preferences."
        )
    t_pref, j_pref, s_pref = (
        profile.preferred_timmy_rank,
        profile.preferred_johnny_rank,
        profile.preferred_spike_rank,
    )
    t_comp, j_comp, s_comp = (
        comp_profile.timmy_rank,
        comp_profile.johnny_rank,
        comp_profile.spike_rank,
    )
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

def get_player_card(player_id):
    user = User.objects.get(id=player_id)
    profile = Profile.objects.get(user=user)
    player_card_data = {
        'bio': profile.bio,
        'header_color': profile.favorite_color,
        'psyche': profile.get_psyche(),
        'rank': profile.rank,
        'role': profile.role,
        'server': profile.lol_server,
        'summoner_name': profile.summoner_name,
        'top_champions': profile.top_champions,
        'user_name': user.username,
    }
    return player_card_data

def get_team_member_ids(team_id):
    if len(Team.objects.filter(id=team_id)) == 0:
        return []
    team = Team.objects.get(id=team_id)
    member_ids = [x.id for x in team.members.all()]
    return member_ids

def get_team_info(team_id):
    if len(Team.objects.filter(id=team_id)) == 0:
        return {}
    team = Team.objects.get(id=team_id)
    return {
        "name": team.name,
        "date_created": team.date_created,
        # record
        # next match
        # rank
    }

