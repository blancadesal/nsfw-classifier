import os
import argparse
import cv2


def extract_frames(source_file, target_dir, msec_time_interval):
  """Function to extract frames from input video file
  and save them as separate frames in an output directory.

  Args:
    source_file: Input video file.
    target_dir: Target directory to save the frames.
    msec_time_interval: Frame sampling interval in msec

  Returns:
    None
  """

  try:
    os.mkdir(target_dir)
  except:
    pass

  cap = cv2.VideoCapture(source_file)
  count = 0
  print('Extracting frames...')

  while(cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_MSEC, (count * msec_time_interval))
    success, frame = cap.read()
    if not success:
      break
    frame_name = f'frame{count}.jpg'
    cv2.imwrite(os.path.join(target_dir, frame_name), frame)    
    count += 1

  print(f'Extracted {count - 1} frames')
  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", help="path to video")
    parser.add_argument("target_dir", help="path to target directory")
    parser.add_argument("msec_time_interval", help="sampling time interval in msec", type=int)
    args = parser.parse_args()
    # print(args)
    extract_frames(args.source_file, args.target_dir, args.msec_time_interval)