import requests
import time
import csv
f=open('mooc.csv','a',encoding='utf-8-sig',newline='')
writer=csv.writer(f)
writer.writerow(['User name','Comment content','"Score"','Number of likes','Release time'])
cookies = {
    'NTESSTUDYSI': '775c8621ab08439484a38ee772d9c3d9',
    'EDUWEBDEVICE': '1348aec1122d451c874f439ddf8a9658',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'origin': 'https://www.icourse163.org',
    'priority': 'u=1, i',
    'referer': 'https://www.icourse163.org/course/ZJU-1003377027',
    'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'NTESSTUDYSI=775c8621ab08439484a38ee772d9c3d9; EDUWEBDEVICE=1348aec1122d451c874f439ddf8a9658',
}

params = {
    'csrfKey': '775c8621ab08439484a38ee772d9c3d9',
}
for x in range(1,60):
    data = {
        'courseId': '1003377027',
        'pageIndex': x,
        'pageSize': '20',
        'orderBy': '3',
    }

    response = requests.post('https://www.icourse163.org/web/j/mocCourseV2RpcBean.getCourseEvaluatePaginationByCourseIdOrTermId.rpc', params=params, cookies=cookies, headers=headers, data=data).json()
    lists=response['result']['list']
    for i in lists:
        name=i['userNickName']
        content=i['content']
        mark=i['mark']
        like=i['agreeCount']
        times=i['gmtModified']
        timestamp = int(times) / 1000
        local_time = time.localtime(timestamp)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
        print(name,content,mark,like,formatted_time)
        writer.writerow([name,content,mark,like,formatted_time])

