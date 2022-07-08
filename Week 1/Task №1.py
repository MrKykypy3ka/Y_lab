def domain_name(url):
    temp = url.replace('https://', '').replace('http://', '').replace('www.', '')
    return temp[:temp.index('.')]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
