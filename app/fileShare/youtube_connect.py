import os
from app import app

def upload_video(id, title="Default title", description="Default Description", category="22", keywords=["videosherpa"], privacy_status = 0):
    """
    Specify these variables in a form
    """
    
    PRIVACY_OPTIONS = ("public", "private", "unlisted")
    
    file_location = os.path.join(app.config['BASE_DIR'], app.config['BASE_DIR'], id+"_edited.mp4")
    video_title = title
    video_description = description
    video_category = category
    video_keywords = keywords
    video_privacy = PRIVACY_OPTIONS[privacy_status]

    os.system('python \
        N:/restful-sherpa-alt/app/fileShare/upload_video.py \
        --file="{}" \
        --title="{}" \
        --description="{}" \
        --category="{}" \
        --keywords="{}" \
        --privacyStatus="{}" \
        --noauth_local_webserver'.format(
            file_location,
            video_title,
            video_description,
            video_category,
            video_keywords,
            video_privacy
        )
    )

    return "test"

