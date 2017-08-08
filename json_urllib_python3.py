#using python3 for json

# coding: utf-8

# In[1]:


import json


# In[6]:


import urllib.request
from urllib.parse import urlencode


# In[3]:


addr = input("Enter address:")


# In[4]:


url_prefix = "https://maps.googleapis.com/maps/api/geocode/json?"


# In[7]:


url = url_prefix + urllib.parse.urlencode({"sensor":'false',"address":addr })


# In[8]:


print(url)


# In[9]:


data = json.loads(urllib.request.urlopen(url).read())


# In[12]:


print (data["results"][0]["geometry"]["location"]["lat"])


# In[14]:


print (data["results"][0]["formatted_address"])


# In[ ]:




