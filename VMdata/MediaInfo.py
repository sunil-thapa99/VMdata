import subprocess

class MediaInfo:
    def __init__(self, video_file=None):
        """ Generic media property extraction class for extracting video
            properties in python.
	
		    Attributes:
                video_file (str) representing the the path of video
		"""
        self.__video_file = video_file

    @property
    def video_path(self):
        """
            Args:
                None
            Returns: 
                path of video (str)
        """
        return self.__video_file

    @video_path.setter
    def video_path(self, video_file):
        """
            Args: 
                video_file (str) representing the the path of video
            Returns:
                None
        """
        self.__video_file = video_file

    def getVideoDetail(self):
        """
            Function to extract media info from video file. This function uses 
            I/O streams to connect to video's input/ouput pipes using subprocess

            Args:
                None
            Returns:
                key_value_pair (dict) representing metadata of video file
        """
        cmd = ["ffprobe -show_streams {}".format(self.__video_file)]

        process = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)

        output, _ = process.communicate()
        decoded_val = output.decode('UTF-8')
        key_value_pair = {'DISPOSITION': {}, 'TAG': {}}
        tokens = decoded_val.split("\n")
        for t in tokens:
            if len(t) != 0:
                result = t.split("=")
                if len(result) == 2:
                    key = result[0]
                    value = result[1]
                    if 'DISPOSITION' in key or 'TAG' in key:
                        new_key = result[0].split(':')

                        key_value_pair[new_key[0]].update({new_key[1]: value})
                    else:
                        key_value_pair.update({key:value})
        return key_value_pair
