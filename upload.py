import dropbox

ACCESS_TOKEN = "token_here"
dbx = dropbox.Dropbox(ACCESS_TOKEN)
with open("14_10_2017_data.csv", "rb") as f:
	dbx.files_upload(f.read(), '/14_10_2017_data.csv', mute = True)


