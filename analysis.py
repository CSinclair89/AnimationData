#!/usr/bin/env python
# coding: utf-8

# In[57]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline, BSpline


# In[58]:


pd = pd.read_csv("data/hours.csv")
pd


# In[59]:


pd_subset = pd.isnull().sum()
pd_subset


# In[60]:


intro_total = pd["intro"].sum()
est_intro_previous = 10
intro_total = intro_total + est_intro_previous
intro_total


# In[61]:


verse1_total = pd["verse1"].sum()
verse1_total


# In[62]:


solo1_total = pd["solo1"].sum()
solo1_total


# In[63]:


solo2_total = pd["solo2"].sum()
solo2_total


# In[64]:


est_solo_previous = 200


# In[65]:


solo_total = solo1_total + solo2_total + est_solo_previous
solo_total


# In[66]:


verse2_total = pd["verse2"].sum()
est_verse2_previous = 14
verse2_total = verse2_total + est_verse2_previous
verse2_total


# In[67]:


outro_total = pd["outro"].sum()
outro_total


# In[68]:


compositing_total = pd["compositing"].sum()
compositing_total


# In[69]:


sunday_subset = pd[pd["day"] == "sunday"]
print(sunday_subset.count())

sunday_subset_intro_total = sunday_subset["intro"].sum()
sunday_subset_verse1_total = sunday_subset["verse1"].sum()
sunday_subset_solo1_total = sunday_subset["solo1"].sum()
sunday_subset_solo2_total = sunday_subset["solo2"].sum()
sunday_subset_verse2_total = sunday_subset["verse2"].sum()
sunday_subset_outro_total = sunday_subset["outro"].sum()
sunday_subset_compositing_total = sunday_subset["compositing"].sum()

sunday_total = sunday_subset_intro_total + sunday_subset_verse1_total + sunday_subset_solo1_total + sunday_subset_solo2_total + sunday_subset_verse2_total + sunday_subset_outro_total + sunday_subset_compositing_total
sunday_mean = round((sunday_total / 38), 2)


# In[70]:


monday_subset = pd[pd["day"] == "monday"]
print(monday_subset.count())

monday_subset_intro_total = monday_subset["intro"].sum()
monday_subset_verse1_total = monday_subset["verse1"].sum()
monday_subset_solo1_total = monday_subset["solo1"].sum()
monday_subset_solo2_total = monday_subset["solo2"].sum()
monday_subset_verse2_total = monday_subset["verse2"].sum()
monday_subset_outro_total = monday_subset["outro"].sum()
monday_subset_compositing_total = monday_subset["compositing"].sum()

monday_total = monday_subset_intro_total + monday_subset_verse1_total + monday_subset_solo1_total + monday_subset_solo2_total + monday_subset_verse2_total + monday_subset_outro_total + monday_subset_compositing_total
monday_mean = round((monday_total / 38), 2)


# In[71]:


tuesday_subset = pd[pd["day"] == "tuesday"]
print(tuesday_subset.count())

tuesday_subset_intro_total = tuesday_subset["intro"].sum()
tuesday_subset_verse1_total = tuesday_subset["verse1"].sum()
tuesday_subset_solo1_total = tuesday_subset["solo1"].sum()
tuesday_subset_solo2_total = tuesday_subset["solo2"].sum()
tuesday_subset_verse2_total = tuesday_subset["verse2"].sum()
tuesday_subset_outro_total = tuesday_subset["outro"].sum()
tuesday_subset_compositing_total = tuesday_subset["compositing"].sum()

tuesday_total = tuesday_subset_intro_total + tuesday_subset_verse1_total + tuesday_subset_solo1_total + tuesday_subset_solo2_total + tuesday_subset_verse2_total + tuesday_subset_outro_total + tuesday_subset_compositing_total
tuesday_mean = round((tuesday_total / 38), 2)


# In[72]:


wednesday_subset = pd[pd["day"] == "wednesday"]
print(wednesday_subset.count())

wednesday_subset_intro_total = wednesday_subset["intro"].sum()
wednesday_subset_verse1_total = wednesday_subset["verse1"].sum()
wednesday_subset_solo1_total = wednesday_subset["solo1"].sum()
wednesday_subset_solo2_total = wednesday_subset["solo2"].sum()
wednesday_subset_verse2_total = wednesday_subset["verse2"].sum()
wednesday_subset_outro_total = wednesday_subset["outro"].sum()
wednesday_subset_compositing_total = wednesday_subset["compositing"].sum()

wednesday_total = wednesday_subset_intro_total + wednesday_subset_verse1_total + wednesday_subset_solo1_total + wednesday_subset_solo2_total + wednesday_subset_verse2_total + wednesday_subset_outro_total + wednesday_subset_compositing_total
wednesday_mean = round((wednesday_total / 38), 2)


# In[73]:


thursday_subset = pd[pd["day"] == "thursday"]
print(thursday_subset.count())

thursday_subset_intro_total = thursday_subset["intro"].sum()
thursday_subset_verse1_total = thursday_subset["verse1"].sum()
thursday_subset_solo1_total = thursday_subset["solo1"].sum()
thursday_subset_solo2_total = thursday_subset["solo2"].sum()
thursday_subset_verse2_total = thursday_subset["verse2"].sum()
thursday_subset_outro_total = thursday_subset["outro"].sum()
thursday_subset_compositing_total = thursday_subset["compositing"].sum()

thursday_total = thursday_subset_intro_total + thursday_subset_verse1_total + thursday_subset_solo1_total + thursday_subset_solo2_total + thursday_subset_verse2_total + thursday_subset_outro_total + thursday_subset_compositing_total
thursday_mean = round((thursday_total / 37), 2)


# In[74]:


friday_subset = pd[pd["day"] == "friday"]
print(friday_subset.count())

friday_subset_intro_total = friday_subset["intro"].sum()
friday_subset_verse1_total = friday_subset["verse1"].sum()
friday_subset_solo1_total = friday_subset["solo1"].sum()
friday_subset_solo2_total = friday_subset["solo2"].sum()
friday_subset_verse2_total = friday_subset["verse2"].sum()
friday_subset_outro_total = friday_subset["outro"].sum()
friday_subset_compositing_total = friday_subset["compositing"].sum()

friday_total = friday_subset_intro_total + friday_subset_verse1_total + friday_subset_solo1_total + friday_subset_solo2_total + friday_subset_verse2_total + friday_subset_outro_total + friday_subset_compositing_total
friday_mean = round((friday_total / 37), 2)


# In[75]:


saturday_subset = pd[pd["day"] == "saturday"]
print(saturday_subset.count())

saturday_subset_intro_total = saturday_subset["intro"].sum()
saturday_subset_verse1_total = saturday_subset["verse1"].sum()
saturday_subset_solo1_total = saturday_subset["solo1"].sum()
saturday_subset_solo2_total = saturday_subset["solo2"].sum()
saturday_subset_verse2_total = saturday_subset["verse2"].sum()
saturday_subset_outro_total = saturday_subset["outro"].sum()
saturday_subset_compositing_total = saturday_subset["compositing"].sum()

saturday_total = saturday_subset_intro_total + saturday_subset_verse1_total + saturday_subset_solo1_total + saturday_subset_solo2_total + saturday_subset_verse2_total + saturday_subset_outro_total + saturday_subset_compositing_total
saturday_mean = round((saturday_total / 38), 2)


# In[76]:


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


# In[77]:


pd_line = pd
pd_line["total"] = pd_line["intro"] + pd_line["verse1"] + pd_line["solo1"] + pd_line["solo2"] + pd_line["verse2"] + pd_line["outro"]


# In[78]:


df_weektotal = pd_line

for week in pd_line:
    pd_week["week total"] = pd_week["total"].groupby(pd_week["week"]).sum()
    
df_weektotal = df_weektotal["week total"].dropna()
df_weektotal


# In[79]:


total_x = list(range(1, 40))
total_y = []

for i in df_weektotal:
    total_y.append(i)
    
arr_total_x = np.array(total_x)
arr_total_y = np.array(total_y)

total_xnew = np.linspace(arr_total_x.min(), arr_total_x.max(), 200) 

spl = make_interp_spline(arr_total_x, arr_total_y, k=3)
total_y_smooth = spl(total_xnew)

font = {
    "size": 8
}

plt.text(1.8, 32, " Classes", fontdict = font)
plt.axvspan(0, 6, color='gray', alpha=0.5)

plt.text(14.9, 32, "Vacation", fontdict = font)
plt.axvspan(13.5, 18.5, color='gray', alpha=0.5)

plt.text(31.5, 32, "Classes", fontdict = font)
plt.axvspan(25, 40, color='gray', alpha=0.5)

plt.ylabel("Hours Worked")
plt.xlabel("Week # (April-December)")
plt.title("Total Overall Hours Worked Per Week")

plt.plot(total_xnew, total_y_smooth)
plt.figure(figsize=(40, 10))


# In[107]:


# Weekly Totals for Each Section

pd_line
pd_line["intro week total"] = pd_line["intro"]
pd_line["verse1 week total"] = pd_line["verse1"]
pd_line["solo total"] = pd_line["solo1"] + pd_line["solo2"]
pd_line["verse2 week total"] = pd_line["verse2"]
pd_line["outro week total"] = pd_line["outro"]
pd_line["compositing week total"] = pd_line["compositing"]
pd_line

df_weektotal = pd_line

for week in df_weektotal:
    df_weektotal["intro week total"] = df_weektotal["intro"].groupby(df_weektotal["week"]).sum()
    df_weektotal["verse1 week total"] = df_weektotal["verse1"].groupby(df_weektotal["week"]).sum()
    df_weektotal["solo week total"] = df_weektotal["solo total"].groupby(df_weektotal["week"]).sum()
    df_weektotal["verse2 week total"] = df_weektotal["verse2"].groupby(df_weektotal["week"]).sum()
    df_weektotal["outro week total"] = df_weektotal["outro"].groupby(df_weektotal["week"]).sum()
    df_weektotal["compositing week total"] = df_weektotal["compositing"].groupby(df_weektotal["week"]).sum()
    
df_weektotal = df_weektotal.dropna()

intro_x = list(range(1, 40))
intro_y = []
verse1_x = list(range(1, 40))
verse1_y = []
solo_x = list(range(1, 40))
solo_y = []
verse2_x = list(range(1, 40))
verse2_y = []
outro_x = list(range(1, 40))
outro_y = []
compositing_x = list(range(1, 40))
compositing_y = []

for i in df_weektotal["intro week total"]:
    intro_y.append(i)
    
for i in df_weektotal["verse1 week total"]:
    verse1_y.append(i)
    
for i in df_weektotal["solo week total"]:
    solo_y.append(i)
    
for i in df_weektotal["verse2 week total"]:
    verse2_y.append(i)
    
for i in df_weektotal["outro week total"]:
    outro_y.append(i)
    
for i in df_weektotal["compositing week total"]:
    compositing_y.append(i)
    
print(intro_y)
    
arr_intro_x = np.array(intro_x)
arr_intro_y = np.array(intro_y)
arr_verse1_x = np.array(verse1_x)
arr_verse1_y = np.array(verse1_y)
arr_solo_x = np.array(solo_x)
arr_solo_y = np.array(solo_y)
arr_verse2_x = np.array(verse2_x)
arr_verse2_y = np.array(verse2_y)
arr_outro_x = np.array(outro_x)
arr_outro_y = np.array(outro_y)
arr_compositing_x = np.array(compositing_x)
arr_compositing_y = np.array(compositing_y)

intro_xnew = np.linspace(arr_intro_x.min(), arr_intro_x.max(), 200) 
spl = make_interp_spline(arr_intro_x, arr_intro_y, k=2)
intro_y_smooth = spl(intro_xnew)

verse1_xnew = np.linspace(arr_verse1_x.min(), arr_verse1_x.max(), 200) 
spl = make_interp_spline(arr_verse1_x, arr_verse1_y, k=2)
verse1_y_smooth = spl(verse1_xnew)

solo_xnew = np.linspace(arr_solo_x.min(), arr_solo_x.max(), 200) 
spl = make_interp_spline(arr_solo_x, arr_solo_y, k=2)
solo_y_smooth = spl(solo_xnew)

verse2_xnew = np.linspace(arr_verse2_x.min(), arr_verse2_x.max(), 200) 
spl = make_interp_spline(arr_verse2_x, arr_verse2_y, k=2)
verse2_y_smooth = spl(verse2_xnew)

outro_xnew = np.linspace(arr_outro_x.min(), arr_outro_x.max(), 200) 
spl = make_interp_spline(arr_outro_x, arr_outro_y, k=2)
outro_y_smooth = spl(outro_xnew)

compositing_xnew = np.linspace(arr_compositing_x.min(), arr_compositing_x.max(), 200) 
spl = make_interp_spline(arr_compositing_x, arr_compositing_y, k=2)
compositing_y_smooth = spl(compositing_xnew)


# In[110]:


# Plotting Sections Over Year

plt.text(1.8, 32, " Classes", fontdict = font)
plt.axvspan(0, 6, color='gray', alpha=0.5)

plt.text(14.9, 32, "Vacation", fontdict = font)
plt.axvspan(13.5, 18.5, color='gray', alpha=0.5)

plt.text(31.5, 32, "Classes", fontdict = font)
plt.axvspan(25, 40, color='gray', alpha=0.5)

plt.ylabel("Hours Worked")
plt.xlabel("Week # (April-December)")
plt.title("Total Overall Hours Worked Per Week")

plt.plot(intro_xnew, intro_y_smooth, label = "Intro")
plt.plot(verse1_xnew, verse1_y_smooth, label = "Verse 1")
plt.plot(solo_xnew, solo_y_smooth, label = "Gtr Solo")
plt.plot(verse2_xnew, verse2_y_smooth, label = "Verse 2")
plt.plot(outro_xnew, outro_y_smooth, label = "Outro")
plt.plot(compositing_xnew, compositing_y_smooth, label = "Compositing")
plt.legend(bbox_to_anchor=(1.02, 0.35), loc='upper left', borderaxespad=0)
plt.figure(figsize=(40, 10))
plt.show()


# In[73]:


sections = [intro_total, verse1_total, solo_total, verse2_total, outro_total, compositing_total]
labels = ["Intro - 47 hours", "Verse 1 - 340 hours", "Gtr Solo - 313 hours", "Verse 2 - 162 hours", "Outro - 24 hours", "Compositing - 14 hours"]

fig, ax = plt.subplots(figsize=(7, 5))

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%"

wedges, texts, autotexts = ax.pie(sections, autopct = lambda pct: func(pct, sections), textprops = dict(color = "w"))
ax.legend(wedges, labels, title = "Section", loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1))
plt.setp(autotexts, size = 10, weight = "bold")
ax.set_title("Breakdown of Hours Per Song Section")

plt.show()


# In[ ]:




