import subprocess

def remove_image_metadata(image_path, output_path):

    exiftool_path = "C:\\exiftool\\exiftool.exe"
    # Remove metadata using exiftool
    subprocess.run([exiftool_path, '-all=', '-overwrite_original', '-out', output_path, image_path])

def remove_video_metadata(video_path, output_path):
    subprocess.run(['ffmpeg', '-i', video_path, '-map_metadata', '-1', '-c', 'copy', output_path])

# Example usage
image_input_path = 'Pic 5.jpg'
image_output_path = 'output_image.jpg'
remove_image_metadata(image_input_path, image_output_path)

video_input_path = 'Example_video.mp4'
video_output_path = 'output_video.mp4'
remove_video_metadata(video_input_path, video_output_path)
