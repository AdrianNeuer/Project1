import json
import pandas as pd

id_ = []  # 用户id
name = []  # 用户名字
gender = []
location = []
profession = []
school = []
major = []
fans = []
focus = []
voteup = []
thanked = []
favorited = []
answer = []
followed_question = []
company = []
job = []
with open('items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        if 'url_token' in item:
            id_.append(item['url_token'])  # id
        else:
            id_.append('')
        if 'name' in item:
            name.append(item['name'])  # 名字
        else:
            name.append('')
        if 'gender' in item:
            gender.append(item['gender'])  # 性别
        else:
            gender.append('')
        try:
            if 'name' in item['locations'][0]:
                location.append(item['locations'][0]['name'])  # 居住地
            else:
                location.append('')
        except Exception:
            location.append('')

        if 'business' in item:
            profession.append(item['business']['name'])  # 所在行业
        else:
            profession.append('')
        try:
            if "school" in item['educations'][0]:
                school.append(item['educations'][0]['school']['name'])  # 学校
            else:
                school.append('')
        except Exception:
            school.append('')
        try:
            if 'major' in item['educations'][0]:
                major.append(item['educations'][0]['major']['name'])  # 专业
            else:
                major.append('')
        except Exception:
            major.append('')
        if 'follower_count' in item:
            fans.append(item['follower_count'])  # 粉丝
        else:
            fans.append('')
        if 'following_count' in item:
            focus.append(item['following_count'])  # 关注
        else:
            focus.append('')
        if 'voteup_count' in item:
            voteup.append(item['voteup_count'])  # 获赞
        else:
            voteup.append('')
        if 'thanked_count' in item:
            thanked.append(item['thanked_count'])  # 感谢
        else:
            thanked.append('')
        if 'favorited_count' in item:
            favorited.append(item['favorited_count'])  # 收藏
        else:
            favorited.append('')
        if 'answer_count' in item:
            answer.append(item['answer_count'])  # 回答数
        else:
            answer.append('')
        if 'following_count' in item:
            followed_question.append(item['following_count'])  # 关注的问题
        else:
            followed_question.append('')
        try:
            if 'company' in item['employments'][0]:
                company.append(item['employments'][0]["company"]['name'])  # 公司
            else:
                company.append('')
        except Exception:
            company.append('')

        try:
            if 'job' in item['employments'][0]:
                job.append(item['employments'][0]["job"]['name'])  # 职位
            else:
                job.append('')
        except Exception:
            job.append('')
df = {
    'id': id_,
    '名字': name,
    '性别': gender,
    '所在地': location,
    '所在行业': profession,
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
df.to_excel('知乎用户.xlsx')
