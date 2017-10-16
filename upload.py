import dropbox

ACCESS_TOKEN = "f1WY0hSJNtAAAAAAAAAACJ799dpcm-jYszAJ1P57b926YS4JyrQqfB58cVTZR1YQ"
dbx = dropbox.Dropbox(ACCESS_TOKEN)
dbx.files_upload("amazon.in adidas shoes date as on 14/10/2017",'/14_10_2017_data.csv')


