#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


pd = pd.read_csv("hours.csv")
pd


# In[3]:


pd_subset = pd.isnull().sum()
pd_subset


# In[4]:


intro_total = pd["intro"].sum()
intro_total


# In[5]:


verse1_total = pd["verse1"].sum()
verse1_total


# In[6]:


solo1_total = pd["solo1"].sum()
solo1_total


# In[7]:


solo2_total = pd["solo2"].sum()
solo2_total


# In[8]:


solo_total = solo1_total + solo2_total
solo_total


# In[9]:


verse2_total = pd["verse2"].sum()
verse2_total


# In[10]:


outro_total = pd["outro"].sum()
outro_total


# In[11]:


compositing_total = pd["compositing"].sum()
compositing_total


# In[12]:


sunday_subset = pd[pd["day"] == "sunday"]
print(sunday_subset.count())

sunday_subset_intro_total = sunday_subset["intro"].sum()
sunday_subset_verse1_total = sunday_subset["verse1"].sum()
sunday_subset_solo1_total = sunday_subset["solo1"].sum()
sunday_subset_solo2_total = sunday_subset["solo2"].sum()
sunday_subset_verse2_total = sunday_subset["verse2"].sum()
sunday_subset_outro_total = sunday_subset["outro"].sum()

sunday_total = sunday_subset_intro_total + sunday_subset_verse1_total + sunday_subset_solo1_total + sunday_subset_solo2_total + sunday_subset_verse2_total + sunday_subset_outro_total
sunday_mean = round((sunday_total / 38), 2)


# In[13]:


monday_subset = pd[pd["day"] == "monday"]
print(monday_subset.count())

monday_subset_intro_total = monday_subset["intro"].sum()
monday_subset_verse1_total = monday_subset["verse1"].sum()
monday_subset_solo1_total = monday_subset["solo1"].sum()
monday_subset_solo2_total = monday_subset["solo2"].sum()
monday_subset_verse2_total = monday_subset["verse2"].sum()
monday_subset_outro_total = monday_subset["outro"].sum()

monday_total = monday_subset_intro_total + monday_subset_verse1_total + monday_subset_solo1_total + monday_subset_solo2_total + monday_subset_verse2_total + monday_subset_outro_total
monday_mean = round((monday_total / 38), 2)


# In[14]:


tuesday_subset = pd[pd["day"] == "tuesday"]
print(tuesday_subset.count())

tuesday_subset_intro_total = tuesday_subset["intro"].sum()
tuesday_subset_verse1_total = tuesday_subset["verse1"].sum()
tuesday_subset_solo1_total = tuesday_subset["solo1"].sum()
tuesday_subset_solo2_total = tuesday_subset["solo2"].sum()
tuesday_subset_verse2_total = tuesday_subset["verse2"].sum()
tuesday_subset_outro_total = tuesday_subset["outro"].sum()

tuesday_total = tuesday_subset_intro_total + tuesday_subset_verse1_total + tuesday_subset_solo1_total + tuesday_subset_solo2_total + tuesday_subset_verse2_total + tuesday_subset_outro_total
tuesday_mean = round((tuesday_total / 38), 2)


# In[15]:


wednesday_subset = pd[pd["day"] == "wednesday"]
print(wednesday_subset.count())

wednesday_subset_intro_total = wednesday_subset["intro"].sum()
wednesday_subset_verse1_total = wednesday_subset["verse1"].sum()
wednesday_subset_solo1_total = wednesday_subset["solo1"].sum()
wednesday_subset_solo2_total = wednesday_subset["solo2"].sum()
wednesday_subset_verse2_total = wednesday_subset["verse2"].sum()
wednesday_subset_outro_total = wednesday_subset["outro"].sum()

wednesday_total = wednesday_subset_intro_total + wednesday_subset_verse1_total + wednesday_subset_solo1_total + wednesday_subset_solo2_total + wednesday_subset_verse2_total + wednesday_subset_outro_total
wednesday_mean = round((wednesday_total / 38), 2)


# In[16]:


thursday_subset = pd[pd["day"] == "thursday"]
print(thursday_subset.count())

thursday_subset_intro_total = thursday_subset["intro"].sum()
thursday_subset_verse1_total = thursday_subset["verse1"].sum()
thursday_subset_solo1_total = thursday_subset["solo1"].sum()
thursday_subset_solo2_total = thursday_subset["solo2"].sum()
thursday_subset_verse2_total = thursday_subset["verse2"].sum()
thursday_subset_outro_total = thursday_subset["outro"].sum()

thursday_total = thursday_subset_intro_total + thursday_subset_verse1_total + thursday_subset_solo1_total + thursday_subset_solo2_total + thursday_subset_verse2_total + thursday_subset_outro_total
thursday_mean = round((thursday_total / 37), 2)


# In[17]:


friday_subset = pd[pd["day"] == "friday"]
print(friday_subset.count())

friday_subset_intro_total = friday_subset["intro"].sum()
friday_subset_verse1_total = friday_subset["verse1"].sum()
friday_subset_solo1_total = friday_subset["solo1"].sum()
friday_subset_solo2_total = friday_subset["solo2"].sum()
friday_subset_verse2_total = friday_subset["verse2"].sum()
friday_subset_outro_total = friday_subset["outro"].sum()

friday_total = friday_subset_intro_total + friday_subset_verse1_total + friday_subset_solo1_total + friday_subset_solo2_total + friday_subset_verse2_total + friday_subset_outro_total
friday_mean = round((friday_total / 37), 2)


# In[18]:


saturday_subset = pd[pd["day"] == "saturday"]
print(saturday_subset.count())

saturday_subset_intro_total = saturday_subset["intro"].sum()
saturday_subset_verse1_total = saturday_subset["verse1"].sum()
saturday_subset_solo1_total = saturday_subset["solo1"].sum()
saturday_subset_solo2_total = saturday_subset["solo2"].sum()
saturday_subset_verse2_total = saturday_subset["verse2"].sum()
saturday_subset_outro_total = saturday_subset["outro"].sum()

saturday_total = saturday_subset_intro_total + saturday_subset_verse1_total + saturday_subset_solo1_total + saturday_subset_solo2_total + saturday_subset_verse2_total + saturday_subset_outro_total
saturday_mean = round((saturday_total / 38), 2)


# In[19]:


day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
mean = [sunday_mean, monday_mean, tuesday_mean, wednesday_mean, thursday_mean, friday_mean, saturday_mean]

fig, ax = plt.subplots()
bars = ax.barh(day, mean)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
y_pos = np.arange(len(days))
hours = (sunday_mean, monday_mean, tuesday_mean, wednesday_mean, thursday_mean, friday_mean, saturday_mean)

ax.barh(y_pos, hours, align = "center", color="#6757FA")
ax.bar_label(bars, label_type="center", color="w")
ax.set_yticks(y_pos, labels = days)
ax.invert_yaxis()
ax.set_xlabel("Hours")
ax.set_title("Average Hours Worked Per Day")
plt.show()


# In[20]:


pd_line = pd
pd_line["total"] = pd_line["intro"] + pd_line["verse1"] + pd_line["solo1"] + pd_line["solo2"] + pd_line["verse2"] + pd_line["outro"]

pd_week = pd_line
pd_week


# In[21]:


df_weektotal = pd_week

for week in pd_week:
    pd_week["week total"] = pd_week["total"].groupby(pd_week["week"]).sum()
    
df_weektotal = df_weektotal["week total"].dropna()
df_weektotal


# In[22]:


plt.plot(df_weektotal)
plt.ylabel("Hours Worked")
plt.xlabel("Week # (April-December)")
plt.figure(figsize=(500,10))
plt.show()


# In[44]:


sections = [intro_total, verse1_total, solo1_total, solo2_total, verse2_total, outro_total]
labels = ["Intro", "Verse 1", "Gtr Solo 1", "Gtr Solo 2", "Verse 2", "Outro"]

fig, ax = plt.subplots(figsize=(7, 5))

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} hours)"

wedges, texts, autotexts = ax.pie(sections, autopct = lambda pct: func(pct, sections), textprops = dict(color = "w"))
ax.legend(wedges, labels, title = "Section", loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1))
plt.setp(autotexts, size = 8, weight = "bold")
ax.set_title("Breakdown of Hours Per Song Section")

plt.show()


# In[ ]:




