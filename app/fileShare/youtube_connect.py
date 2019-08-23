import os
from config import Config
import logging

def upload_video(id, title="Default title", description="Default Description", category="22", keywords=["videosherpa"], privacy_status = 0):
    """
    Specify these variables in a form
    """
    
    PRIVACY_OPTIONS = ("public", "private", "unlisted")
    
    file_location = os.path.join(Config.BASE_DIR, Config.VIDS_LOCATION, id, id+"_edited.mp4")
    video_title = title
    video_description = description
    video_category = category
    video_keywords = keywords
    video_privacy = PRIVACY_OPTIONS[privacy_status]

    youtube_auth_token = open(os.path.join(Config.BASE_DIR, Config.VIDS_LOCATION, id, id+"_youtube_auth.log"), "a+")


    run = "python "\
    "app/fileShare/upload_video.py "\
    '--file="{}" '\
    '--title="{}" '\
    '--description="{}" '\
    '--category="{}" '\
    '--keywords="{}" '\
    '--privacyStatus="{}" '\
    '--writeFile="{}" '\
    "--noauth_local_webserver".format(
            file_location,
            video_title,
            video_description,
            video_category,
            video_keywords,
            video_privacy,
            youtube_auth_token
        )

    logging.debug(run)
    print(run)

    os.system(run)

    return "Uploading video to YouTube..."

upload_video("1149")