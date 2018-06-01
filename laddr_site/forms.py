from django import forms
from .models import LOL_SERVERS, RANKS, ROLES

class ProfileForm(forms.Form):
	summoner_name = forms.CharField(
		label='Summoner name',
		max_length=50
	)
	# server = forms.MultipleChoiceField(
	# 	label="Preferred Server", 
	# 	required = True, 
	# 	widget=forms.CheckboxSelectMultiple, 
	# 	choices=LOL_SERVERS
	# )
	top_champions = forms.CharField(
		label="Top Champs",
		max_length=50
	)
	bio = forms.CharField(
		widget=forms.Textarea,
		label="Who are you"
	)
	rank = forms.ChoiceField(
		label="Rank",
		choices=RANKS
	)
	role = forms.ChoiceField(
		label="Role",
		choices=ROLES
	)
	color = forms.ChoiceField(
		label="Color Preference",
		choices=(
			('#FF0000', "Red"),
			("#00FF00", "Green"),
			('#0000FF', "Blue")
		)
	)