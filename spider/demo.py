import requests

'''
    json:结构化数据  字典类似
    html:非结构化数据
'''
url = 'https://www.kanman.com/api/getchapterinfov2?product_id=1&productname=kmh&platformname=pc&comic_id=108515&chapter_newid=di1hua-1611285550012&isWebp=1&quality=middle'


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'cookie': 'user=%7B%22type%22%3A%22device%22%2C%22Cgold%22%3A0%2C%22coins%22%3A0%2C%22Ulevel%22%3A1%7D; UM_distinctid=18220b7fddfa7-02aa393ed5a53b-26021a51-384000-18220b7fde0af6; CNZZDATA1255417151=1562005100-1658403658-%7C1658403658; CNZZDATA1261814609=1158867612-1658406105-%7C1658406105; kmh-habit=%7B%22mode%22%3A%22scroll%22%7D',
           'referer': 'https://www.kanman.com/108515/di1hua-1611285550012.html'
           }
response = requests.get(url)
data = response.json()
img_list = data['data']['current_chapter']['chapter_img_list']
name = data['data']['current_chapter']['chapter_name']
print(name)
num = 1
for i in img_list:
    res = requests.get(i, headers=headers)
    with open('dufei/'+str(name)+str(num)+'.jpg', 'wb') as f:
        f.write(res.content)
    num += 1


