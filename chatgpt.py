import requests

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}

# 붐에게
# role 종류 : system, user, assistant, function
# temperature : default 1 (0~2) 높을수록 좀더 다양성 있는 결과 나오나방
sample_data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Translate the following English text to Korean: 'Hello, how are you?'"}],
    "temperature": 0.7
}

keyword = "축구 컷백"

# 제목 쪄오기
prompt_for_title = f"""
I’m writing a blog post based on the keyword “{keyword}”. 
Come up with only one title idea. 
Title should incorporate the exact keyword. 
The title should be no more than 60 characters in total.
Translate in Korean.
"""

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt_for_title}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
response_json = response.json()
title = response_json['choices'][0]['message']['content']
print(title)

# 블로그 글 써주세요
prompt_for_blog_post = f"""
Write a 3000 word blog post titled {title} that uses the exact keyword {keyword} at least once every 1000 words. 
The blog post should include an introduction, main body, and conclusion. The conclusion should invite readers to leave a comment. 
Write in Markdown format.
The main body should be split into at least 4 different subsections.
"""

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt_for_blog_post}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
response_json = response.json()
blog_post = response_json['choices'][0]['message']['content']
print(blog_post)
