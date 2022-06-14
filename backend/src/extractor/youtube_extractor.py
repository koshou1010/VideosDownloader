from pytube import YouTube

class YoutubeExtractor:
    def __init__(self, input_url):
        self.input_url = input_url
    
    def progress(self, chunk, file_handle, bytes_remaining):
        content_size = self.target_mp4.filesize
        size = content_size - bytes_remaining
        print('\r' + '[Download progress]:[%s%s]%.2f%%;'%('█' * int(size*20/content_size), ' '*(20-int(size*20/content_size)), float(size/content_size*100)), end='')

    def download_entrance(self):
        yt = YouTube(self.input_url, on_progress_callback=self.progress)
        prog_mp4 = yt.streams.filter(progressive=True, file_extension='mp4')
        self.target_mp4 = prog_mp4.order_by('resolution').desc().first()
        video_file = self.target_mp4.download()