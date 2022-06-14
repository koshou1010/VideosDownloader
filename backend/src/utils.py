import backend.src.extractor.youtube_extractor as youtube_extractor



def extractor_selector(input_url):
    return youtube_extractor.YoutubeExtractor(input_url)
    
def doing_download(choose_extractor):
    choose_extractor.download_entrance()