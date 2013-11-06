import os
import urllib

def get_existing_pages():
    pages = []
    for root, dirs, filenames in os.walk('static'):
        for f in filenames:
            pages.append({urllib.unquote_plus(f[:-4]): f[:-4]})
    return sorted(pages, key=lambda k: k)