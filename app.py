import cv2
import os

def split_video_to_frames(video_path, num_frames):
    # Open video file
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = max(1, frame_count // num_frames)

    # Create output directory for frames
    output_dir = "frames_output"
    os.makedirs(output_dir, exist_ok=True)

    frame_num = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_num % step == 0:
            cv2.imwrite(f"{output_dir}/frame_{saved_count}.jpg", frame)
            saved_count += 1
            if saved_count >= num_frames:
                break

        frame_num += 1

    cap.release()
    print(f"Saved {saved_count} frames in {output_dir}")

# Example usage
video_path = input("Enter path to video: ")
num_frames = int(input("Enter number of frames to extract: "))
split_video_to_frames(video_path, num_frames)
