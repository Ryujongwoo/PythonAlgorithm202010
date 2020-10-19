#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


# 대화 주제 1 ~ 75를 크롤링해서 리스트에 저장시켜 리턴하는 함수
def getSubject():
    subjects = [] # 클롤링한 대화 주제를 저장해서 리턴시킬 빈 리스트를 만든다.
    request = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.findAll('div', {'class': 'tcb-flex-col'})
    for div in divs:
        chapters = div.findAll('a')
        for chapter in chapters:
            subjects.append(chapter.text)
        # ===== for chapter in chapters: 끝
    # ===== for div in divs: 끝
    return subjects


# In[5]:


if __name__ == '__main__':
    subjects = getSubject()
    # print(subjects)
    for i in range(len(subjects)):
        print('{0:2d}. {1}'.format(i + 1, subjects[i]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




