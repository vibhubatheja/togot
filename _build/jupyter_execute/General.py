#!/usr/bin/env python
# coding: utf-8

# # New page to be added testing the run process
#  This is a new page I am adding and testing if it runs 
#  
# ```{figure} thumb-1920-598731.jpg
# ---
# height: 200px
# name: PythonBasics4
# ---
# Boruto: Naruto Next Genrations
# ```

# In[1]:


from jupyterquiz import display_quiz
import json
with open("L1Q.json", "r") as file:
    questions=json.load(file)
    
display_quiz(questions)


# In[ ]:





# In[ ]:




