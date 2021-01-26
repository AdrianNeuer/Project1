import requests
import json
import pandas as pd

id_ = []  # 用户id
name = []  # 用户名字
gender = []  # 性别
location = []  # 所在地
profession = []  # 职业
school = []  # 学校
major = []  # 专业
fans = []  # 粉丝数
focus = []  # 关注数
voteup = []  # 获赞
thanked = []  # 感谢
favorited = []  # 收藏
answer = []  # 回答数
followed_question = []  # 关注问题
company = []  # 公司
job = []  # 工作职位


def get_url(url):  # 获取链接内容
    header_job = {
        "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
    }
    user_url = url
    # proxies = {'http': 'http://192.168.0.101'}    # 免费ip或组内成员ip
    response = requests.get(user_url, headers=header_job)  # , proxies=proxies)
    data = response.content
    data = data.decode('utf-8')
    return data


def get_follower(userID):  # 解析内容，获取关注用户
    lst = []
    url = 'https://www.zhihu.com/api/v4/members/'+userID+'/followees?' \
          'include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%' \
          '2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=20'
    data = get_url(url)
    data = json.loads(data)
    try:
        for user in data['data']:
            lst.append(user['url_token'])
    except Exception:
        pass
    return lst


def next(lst):  # 获取已存列表关注用户
    follower = []
    for user in lst:
        try:
            follower.extend(get_follower(user))
        except Exception:
            pass
    return follower


def get_userInfo(userID):  # 获取用户信息
    url = "https://www.zhihu.com/api/v4/members/" + userID + "?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_bind_phone%2Cis_force_renamed%2Cis_bind_sina%2Cis_privacy_protected%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics"
    data = get_url(url)
    data = json.loads(data)
    if 'url_token' in data:
        id_.append(data['url_token'])  # id
    else:
        id_.append('')
    if 'name' in data:
        name.append(data['name'])  # 名字
    else:
        name.append('')
    if 'gender' in data:
        gender.append(data['gender'])  # 性别
    else:
        gender.append('')
    try:
        if 'name' in data['locations'][0]:
            location.append(data['locations'][0]['name'])  # 居住地
        else:
            location.append('')
    except Exception:
        location.append('')

    if 'business' in data:
        profession.append(data['business']['name'])  # 所在行业
    else:
        profession.append('')
    try:
        if "school" in data['educations'][0]:
            school.append(data['educations'][0]['school']['name'])  # 学校
        else:
            school.append('')
    except Exception:
        school.append('')
    try:
        if 'major' in data['educations'][0]:
            major.append(data['educations'][0]['major']['name'])  # 专业
        else:
            major.append('')
    except Exception:
        major.append('')
    if 'follower_count' in data:
        fans.append(data['follower_count'])  # 粉丝
    else:
        fans.append('')
    if 'following_question_count' in data:
        focus.append(data['following_question_count'])  # 关注
    else:
        focus.append('')
    if 'voteup_count' in data:
        voteup.append(data['voteup_count'])  # 获赞
    else:
        voteup.append('')
    if 'thanked_count' in data:
        thanked.append(data['thanked_count'])  # 感谢
    else:
        thanked.append('')
    if 'favorited_count' in data:
        favorited.append(data['favorited_count'])  # 收藏
    else:
        favorited.append('')
    if 'answer_count' in data:
        answer.append(data['answer_count'])  # 回答数
    else:
        answer.append('')
    if 'following_count' in data:
        followed_question.append(data['following_count'])  # 关注的问题
    else:
        followed_question.append('')
    try:
        if 'company' in data['employments'][0]:
            company.append(data['employments'][0]["company"]['name'])  # 公司
        else:
            company.append('')
    except Exception:
        company.append('')

    try:
        if 'job' in data['employments'][0]:
            job.append(data['employments'][0]["job"]['name'])  # 职位
        else:
            job.append('')
    except Exception:
        job.append('')


def save():  # 转化为DataFrame
    df = {
        'id': id_,
        '名字': name,
        '性别': gender,
        '所在地': profession,
        '学校': school,
        '专业': major,
        '粉丝': fans,
        '关注': focus,
        '获赞': voteup,
        '感谢': thanked,
        '收藏': favorited,
        '回答数': answer,
        '关注的问题': followed_question,
        '公司': company,
        '职位': job
    }
    df = pd.DataFrame(df, index=range(1, 1 + len(id_)))
    return df


def main():  # 主函数
    user_all = []
    with open('data/url.txt', 'r') as f:
        lines = f.readlines()  # 读取所有行
        last_line = lines[-1]  # 取最后一行
    user_id = last_line  # 继续上一次的爬取
    user = get_follower(user_id)
    if user is None:
        print("没有关注的人")
    else:
        user_all = next(user)
    user_all = list(set(user_all))  # 去掉重复的用户重
    with open('data/url.txt', 'a') as f:  # 写入文本文件
        for text in user_all:
            f.write('\n' + text)
    for Id in user_all:
        get_userInfo(Id)


if __name__ == '__main__':
    for i in range(200):
        main()
    df = save()
    df.to_excel('知乎用户.xlsx')
