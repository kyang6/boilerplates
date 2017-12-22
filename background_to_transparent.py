'''
Script to make background transparent
Basics:
	- Pass in an image and a threshold. This is a value between 0-255 
		that specifies the cutoff for color which will be turned transparent.
		Default channel is white, to switch to black channel set --channel flag to 'b'

How to Use:
	- install dependencies (cv2, argparse, os, pillow)
	- call script: 'python3 background_to_transparent.py 
		--image [FILENAME] 
		--threshold [THRESHOLD]
		--channel [CHANNEL]'
	- for help: 'python background_to_transparent.py --help' 
'''
import cv2
import argparse
import os 


'''
private function _create_args()
-------------------------------
Creates an argeparse object for CLI for threshold_image() function

Input:
	Void

Return:
	args object with required arguments for threshold_image() function

'''
def _create_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--image", help="filename of the image that will be edited", type=str)
	parser.add_argument("--threshold", help="threshold for black cut off: range(0,255)", type=int)
	parser.add_argument("--channel", help="threshold corresponds to black(b) or white(w) channel", type=str)

	args = parser.parse_args()
	return args


'''
public function threshold_image(image_name, dir_path, channel, threshold)
----------------------------------------------------------------
Segments thresholded pixels in an image to transparent

Input:
	Pass in the path to an image, what channel to threshold, and a 
	threshold value. Writes a final image called edited_[INPUT IMAGE NAME].png
	that is the source image but the pixels that are choosen by the thresholded are transparent.

Return:
	Void 
'''
def threshold_image(filename, channel, threshold):
	image_name = os.path.basename(args.image) 		# Name of the image
	dir_path = os.path.dirname(args.image) 			# Path to the file
	
	print("Name of Image: {0}".format(image_name))
	print("Path to Image: {0}".format(dir_path))

	src = cv2.imread('/'.join((dir_path,image_name)), 1)
	tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	if channel == "b":
		_,alpha = cv2.threshold(tmp,threshold,255,cv2.THRESH_BINARY)
	else:
		_,alpha = cv2.threshold(tmp,threshold,255,cv2.THRESH_BINARY_INV)
	
	b, g, r = cv2.split(src)
	rgba = [b,g,r, alpha]
	dst = cv2.merge(rgba,4)

	# Save image to same directory as source image
	final_path = '/'.join((dir_path,"edited_{0}.png".format(image_name.split(".")[0])))
	print("Edited Image Path: {0}".format(final_path))
	cv2.imwrite(final_path, dst)

if __name__ == '__main__':
	args = _create_args()
	threshold_image(args.image, args.channel, args.threshold)




