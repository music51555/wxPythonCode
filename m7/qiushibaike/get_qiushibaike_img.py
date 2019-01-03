import requests

pic_url = 'https://www.qiushibaike.com/pic/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

pci_text = requests.get(url = pic_url, headers = headers).text
