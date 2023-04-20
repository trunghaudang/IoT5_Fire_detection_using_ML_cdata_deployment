from icrawler.builtin import GoogleImageCrawler

keywords = [''] #key word list to query images


google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': "C:/Users/84386/OneDrive/Desktop/nonname"}) #dir to store images
filters = dict(
    size='large',
    date=((2000, 1, 1), (2023, 4, 17)))
for keyword in keywords:
    google_crawler.crawl(keyword=keyword, filters=filters, max_num=100)