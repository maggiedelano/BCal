# TO DO:
# Look for data points since the script was last run (so time of last run must be recorded)
# For each new datapoint, write the pomodoro comment to a new google calendar event
# If possible, check and make sure the event doesn't already exist
# Calendar event length = POMODORO_LENGTH * value of datapoint
# Calendar event time = timestamp of datapoint - event length
# Calendar event name = Pomodoro comment (if it exists), else "Pomodoro"

import requests

auth_token = 'YOUR_AUTH_TOKEN_HERE'
defaultGoal = 'pomodoros'

def getUserURLResponse(authToken, diffSince):
	"""Get a response from user url using authToken."""
	params = {'auth_token': authToken, 'diff_since': diffSince}

	response = requests.get('https://www.beeminder.com/api/v1/users/me.json', params = params)

	print(response.json())

getUserURLResponse(auth_token, 1437246999)

