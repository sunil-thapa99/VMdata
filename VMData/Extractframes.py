import cv2
import os

from .MediaInfo import MediaInfo

class Extractframes(MediaInfo):
    def __init__(self, video_file):
        """
            Generic media property extraction class for extracting video
            properties in python.
    
            Attributes:
                video_file (str) representing the the path of video
        """
        MediaInfo.__init__(self, video_file)
        

    def __check_rotation(self,):
        """
            Function to check the rotation value of video.

            Args:
                None
            Return:
                rotateCode (int)
        """
        meta_dict = self.getVideoDetail()
        rotateCode = None
        
        try:
            rotation_val = meta_dict['TAG']['rotate']
            if int(rotation_val) == 90:
                rotateCode = cv2.ROTATE_90_CLOCKWISE
            elif int(rotation_val) == 180:
                rotateCode = cv2.ROTATE_180
            elif int(rotation_val) == 270:
                rotateCode = cv2.ROTATE_90_COUNTERCLOCKWISE
        except:
            print(f'No rotation data found on media {self.video_path}')
            pass
        return rotateCode

    def __correct_rotation(self, frame, rotateCode):
        """
            Rotates the given frame.

            Args: 
                frame (numpy.ndarray) represents n-dimensional matrix of image
                rotateCode (int) represents clockwise/anti-clockwise direction

            Return:
                New rotated frame
        """
        return cv2.rotate(frame, rotateCode)

    def extract_frames(self, frame_path='', index=0):
        """
            Extract frames from video while looking into video rotation degree. 
            Mostly, the aspect ration between different devices doesn't matches.
            To resolve such issue, the __check_rotation examines the I/O input property 
            of video and according to the rotation degree, the __correct_rotation rotates
            the frame before saving the frame.

            Args:
                frame_path (str) represents file path to save extracted image
                index (int) represent starting index number for frame to be saved

            Return:
                None
        """
        try:
            cam = cv2.VideoCapture(self.video_path)
        except:
            print(f'No video source found.')
            pass
        rotateCode = self.__check_rotation()

        while True:
            ret, frame = cam.read()

            if ret:
                if rotateCode is not None:
                    frame = self.__correct_rotation(frame, rotateCode)
                index += 1
                cv2.imwrite(os.path.join(frame_path, str(index) + ".jpg"), frame)
            else:
                break

