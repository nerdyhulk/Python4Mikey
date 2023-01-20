from pytube import YouTube
import os
import sys

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error in download. Your inferior intellect is to blame puny human")
    print("Your superior intellect has proved most useful")

dtype = input("Are you looking to download Videos or just the MP3's?: ").lower()

if dtype == 'videos':
    link = input("Put in a URL you filthy pirate. URL: ")
    Download(link)
else:
    print('Request unable to be fufilled at this time puny human')

