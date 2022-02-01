import cv2
import numpy as np


camera_device_index = 0


def create_video_capture_object(cam_index=0):
	video_stream = cv2.VideoCapture(cam_index)
	return video_stream

def main():
	video_stream = create_video_capture_object(camera_device_index)

	# Runs through the stream frame-by-frame as long as a frame is being returned
	ret = True
	while ret:
		ret, frame = video_stream.read()
		img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	                          # Hue     Sat    Val (Brightness)
	                          # [0-360, 0-255, 0-255]
		hsv_color1 = np.asarray([50   , 50   , 150  ])  # Low Values
		hsv_color2 = np.asarray([130  , 255  , 255  ])  # High Values

		mask = cv2.inRange(img_hsv, hsv_color1, hsv_color2)

		# Displays video streams for both the raw stream and the masked stream
		cv2.imshow('RAW_FRAME', frame)
		cv2.imshow('MASKED_FRAME', mask)

		# Press "q" to stop the camera
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	video_stream.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
