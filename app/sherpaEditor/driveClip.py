from moviepy.editor import CompositeVideoClip, concatenate_videoclips, concatenate_audioclips, CompositeAudioClip
from moviepy.video.io import html_tools
from app.sherpaEditor import generateEffects, sherpaUtils
import os, gc
from app import app

# TODO: This needs to be changed in the app.config to
#  read to the correct attach directory as outlined in the configuration
attach_dir = os.path.abspath(app.config['DIR_LOCATION'])


def render_video(uid, html_render=False):
    gc.collect()
    """Needs to check for a project_id (user)
    Set html_render to True if you want this function to return html embed code for a preview"""
    # Finished timeline video
    video_list = []

    # Top and Bottom audio timeline
    top_audio = []

    # Define current length of video, in terms of the 'main' timeline
    mainTimeline = 0

    # May be better to read information from this json call, instead of sherpaUtils
    json_file = sherpaUtils.set_proj(uid)

    # Automated all the clips
    for clipName in json_file['CutAwayFootage']:
        # Testing printout
        print(clipName + ":")
        print("mainTimeline: {}".format(mainTimeline))

        # Initialise clip data first
        clipData = sherpaUtils.open_clip_meta_data(data=json_file, clip=clipName)

        clipType = clipData.get('clipType')

        # If its a cutaway, just generate the clip and add a caption if it exists
        if clipType == "CutAway":
            print(clipName + " is a cutaway.")
            clip = generateEffects.generate_clip(clip_data=clipData, user=uid)
            # Insert audio using insert sort
            top_audio.insert(clipData.get('order'), clip.audio)

            # Look for the clip caption data
            captionData = sherpaUtils.open_clip_caption_data(data=json_file, clip=clipName)

            # Append here if it's needed
            if captionData is not 0:
                caption = generateEffects.generate_text_caption(captionData, clipData)
                clip = CompositeVideoClip([clip, caption])

        # Generate image
        elif clipType == "Image":
            print(clipName + " is an image.")
            clip = generateEffects.generate_image_clip(clipData, uid)
            top_audio.insert(clipData.get('order'), clip.audio)

        # If it's a blank
        elif clipType == "Blank":
            try:
                print(clipName + " is a blank.")

                interviewClipCaption = 0

                # get interview footage that should be currently playing, as well as what time it should be playing at
                blankInterviewClip, interviewStartTime = sherpaUtils.current_interview_footage(
                    clip_timeline=mainTimeline,
                    data=json_file
                )

                # Difference between the main timeline and the starting time line for clip
                dif = mainTimeline-interviewStartTime

                print("Interview starts at {}, Blank starts at {}, so difference is {}".format(
                    interviewStartTime,
                    mainTimeline,
                    dif)
                )

                interviewClipMeta = blankInterviewClip['Meta']

                # Create caption and clip data for interview
                try:
                    interviewClipCaption = blankInterviewClip['edit']['Caption']
                # Define it as empty if no clipData found
                except KeyError:
                    interviewClipCaption = 0

                """ 
                Start time is the start time of the Sub Clipped segment of the interview clip video
                Plus the difference between the current time on the top timeline and the starting time for this clip
                Example:
                    Blank starts at 10 seconds, and is 3 seconds long
                    Interview clip starts at 7 seconds, and is 10 seconds long
                    Interview clip should be heard for all 10 seconds from 7-17 on the video
                    But should only be seen from seconds 10-13 on the video
                    Which translates to seconds 3-6 on the clip itself
                    subClipStart is 3, and subClipEnd is 6 in this case
                """
                subClipStart = (interviewClipMeta.get('startTime')) + dif
                subClipEnd = (interviewClipMeta.get('startTime')) + dif + (
                        (clipData.get('endTime')) - (clipData.get('startTime'))
                )
                print("Sub clip starts at {}, ends at {}".format(subClipStart, subClipEnd))

                # Create clip with parameterised start and end times
                clip = generateEffects.generate_clip(
                    clip_data=interviewClipMeta,
                    user=uid,
                    start=subClipStart,
                    end=subClipEnd
                )
            # No clip can be found, generate a blank
            except TypeError:
                print("TypeError - No clip found")
                clip = generateEffects.generate_blank(clipData)
                top_audio.insert(clipData.get('order'), clip.audio)
            # We want this code to run only if we get in the try loop
            # So we use 'finally'
            finally:
                if interviewClipCaption is not 0:
                    caption = generateEffects.generate_text_caption(
                        interviewClipCaption,
                        interviewClipMeta,
                        dur=subClipEnd - subClipStart
                    )
                    clip = CompositeVideoClip([clip, caption])

        # Insert clip into correct position in array
        print("Inserted {} into pos {}.".format(clipData.get('name'), clipData.get('order')-1))

        mainTimeline += clip.duration
        video_list.insert(clipData.get('order')-1, clip)
    
    print(video_list)

    # Create audio from the interview Footage
    bottom_audio = generateEffects.interview_audio_builder(interview_data=json_file['InterviewFootage'], user=uid)

    # Concatenate the clips together
    top_audio = concatenate_audioclips(top_audio)

    try:
        bottom_audio = concatenate_audioclips(bottom_audio)
        # Composite the sound together
        finished_audio = CompositeAudioClip([top_audio, bottom_audio])
    # In case no bottom audio is found
    except ValueError:
        finished_audio = top_audio

    # Concatenate the video files together
    # TODO: Method is currently set at 'compose', which may end up making the whole video look off
    #   Delete or set to 'chain'
    finished_video = concatenate_videoclips(video_list, method="compose")
    finished_video = finished_video.set_audio(finished_audio)
    
    
    # Returns html render of video if true
    if html_render is True:
        print("Creating html preview for project.")
        low_quality = finished_video.resize(0.5)
        preview_runtime = low_quality.duration
        # the +5 is to stop a small issue with regards to previewing a video longer than 60 seconds
        return html_tools.html_embed(
                low_quality,
                maxduration=preview_runtime+5,
                rd_kwargs={
                    'fps': 15,
                    'bitrate': '300k'
                }
            )


    # Otherwise full renders
    else:
        print("Rendering {} clip(s) together, of total length {}.".format(len(video_list), finished_video.duration))
        # Render the finished project out into an mp4
        finished_video.write_videofile(
            os.path.join(
                attach_dir,
                uid,
                sherpaUtils.get_proj_name(data=json_file) + "_edited.mp4"
            )
        )
