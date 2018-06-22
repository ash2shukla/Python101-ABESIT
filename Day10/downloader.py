import urllib.request


def download(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

if __name__ == "__main__":
    download("http://ovh.net/files/1Mb.dat", "downloaded_file.dat")