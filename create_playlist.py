#Step 1: Log into Youtube
#Step 2: Grab our Liked Videos
#Step 3: Create a New Playlist
#Step 4: Search for the new Song
#Step 5: Add this song into the new Spotify Playlist
import json
import requests
#from secrets import spotify_user_id, spotify_token
import secrets

class createPlaylist:
	def __init__(self):
		self.user_id = secrets.spotify_user_id

	def get_youtube_client(self):
		pass

	def get_liked_videos(self):
		pass

	def create_playlist(self):
		request_body = json.dumps(
		  {"name": "New Playlist Test",
		  "description": "New playlist Test description",
		  "public": True}
		  )

		query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
		response = requests.post(query, 
			data=request_body,
			headers={"Content-Type": "application/json",
					"Authorization": "Bearer {}".format(secrets.spotify_token)
					}
			)
		response_json = response.json()
		return response
		#return response_json

		#return playlist id
		return response_json["id"]

	#Search for the Song
	def get_spotify_url(self, track, artist):
		pass

	def add_song_to_playlist(self):
		pass

test = createPlaylist()
print(test.create_playlist())