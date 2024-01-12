
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

pd = pd.read_csv("data/hours.csv")

pd_line = pd
pd_line["total"] = pd_line["intro"] + pd_line["verse1"] + pd_line["solo1"] + pd_line["solo2"] + pd_line["verse2"] + pd_line["outro"]

pd_week = pd_line
pd_week

df_weektotal = pd_week

for week in pd_week:
    pd_week["week total"] = pd_week["total"].groupby(pd_week["week"]).sum()
    
df_weektotal = df_weektotal["week total"].dropna()
df_weektotal

x = list(range(1, 40))
y = []

for i in df_weektotal:
    y.append(i)
    
arr_x = np.array(x)
arr_y = np.array(y)

xnew = np.linspace(arr_x.min(), arr_x.max(), 200) 

spl = make_interp_spline(arr_x, arr_y, k=3)
y_smooth = spl(xnew)

font = {
    "size": 10
}

# Weekly Totals for Intro Section

pd_line_intro = pd_line
pd_line_intro["intro week total"] = pd_line["intro"]
pd_line_intro

df_intro_weektotal = pd_line_intro

for week in df_intro_weektotal:
    df_intro_weektotal["intro week total"] = df_intro_weektotal["intro"].groupby(df_intro_weektotal["week"]).sum()
    
df_intro_weektotal = df_intro_weektotal["intro week total"].dropna()
df_intro_weektotal

intro_x = list(range(1, 40))
intro_y = []

for i in df_intro_weektotal:
    intro_y.append(i)
    
arr_intro_x = np.array(intro_x)
arr_intro_y = np.array(intro_y)

intro_xnew = np.linspace(arr_intro_x.min(), arr_intro_x.max(), 200) 

spl = make_interp_spline(arr_intro_x, arr_intro_y, k=2)
intro_y_smooth = spl(intro_xnew)

# Weekly Totals for Verse 1 Section

pd_line_verse1 = pd_line
pd_line_verse1["verse1 week total"] = pd_line["verse1"]
pd_line_verse1

df_verse1_weektotal = pd_line_verse1

for week in df_verse1_weektotal:
    df_verse1_weektotal["verse1 week total"] = df_verse1_weektotal["verse1"].groupby(df_verse1_weektotal["week"]).sum()
    
df_verse1_weektotal = df_verse1_weektotal["verse1 week total"].dropna()
df_verse1_weektotal

verse1_x = list(range(1, 40))
verse1_y = []

for i in df_verse1_weektotal:
    verse1_y.append(i)
    
arr_verse1_x = np.array(verse1_x)
arr_verse1_y = np.array(verse1_y)

verse1_xnew = np.linspace(arr_verse1_x.min(), arr_verse1_x.max(), 200) 

spl = make_interp_spline(arr_verse1_x, arr_verse1_y, k=2)
verse1_y_smooth = spl(verse1_xnew)

# Weekly Totals for Guitar Solo

pd_line_solo = pd_line
pd_line_solo["solo total"] = pd_line["solo1"] + pd_line["solo2"]
pd_line_solo

df_solo_weektotal = pd_line_solo

for week in df_solo_weektotal:
    df_solo_weektotal["solo week total"] = df_solo_weektotal["solo total"].groupby(df_solo_weektotal["week"]).sum()
    
df_solo_weektotal = df_solo_weektotal["solo week total"].dropna()
df_solo_weektotal

solo_x = list(range(1, 40))
solo_y = []

for i in df_solo_weektotal:
    solo_y.append(i)
    
arr_solo_x = np.array(solo_x)
arr_solo_y = np.array(solo_y)

solo_xnew = np.linspace(arr_solo_x.min(), arr_solo_x.max(), 200) 

spl = make_interp_spline(arr_solo_x, arr_solo_y, k=2)
solo_y_smooth = spl(solo_xnew)

# Weekly Totals for Verse 2 Section

pd_line_verse2 = pd_line
pd_line_verse2["verse2 week total"] = pd_line["verse2"]
pd_line_verse2

df_verse2_weektotal = pd_line_verse2

for week in df_verse2_weektotal:
    df_verse2_weektotal["verse2 week total"] = df_verse2_weektotal["verse2"].groupby(df_verse2_weektotal["week"]).sum()
    
df_verse2_weektotal = df_verse2_weektotal["verse2 week total"].dropna()
df_verse2_weektotal

verse2_x = list(range(1, 40))
verse2_y = []

for i in df_verse2_weektotal:
    verse2_y.append(i)
    
arr_verse2_x = np.array(verse2_x)
arr_verse2_y = np.array(verse2_y)

verse2_xnew = np.linspace(arr_verse2_x.min(), arr_verse2_x.max(), 200) 

spl = make_interp_spline(arr_verse2_x, arr_verse2_y, k=2)
verse2_y_smooth = spl(verse2_xnew)


# Weekly Totals for Outro Section

pd_line_outro = pd_line
pd_line_outro["outro week total"] = pd_line["outro"]
pd_line_outro

df_outro_weektotal = pd_line_outro

for week in df_outro_weektotal:
    df_outro_weektotal["outro week total"] = df_outro_weektotal["outro"].groupby(df_outro_weektotal["week"]).sum()
    
df_outro_weektotal = df_outro_weektotal["outro week total"].dropna()
df_outro_weektotal

outro_x = list(range(1, 40))
outro_y = []

for i in df_outro_weektotal:
    outro_y.append(i)
    
arr_outro_x = np.array(outro_x)
arr_outro_y = np.array(outro_y)

print(arr_outro_x)
print(arr_outro_y)

outro_xnew = np.linspace(arr_outro_x.min(), arr_outro_x.max(), 200) 

spl = make_interp_spline(arr_outro_x, arr_outro_y, k=2)
outro_y_smooth = spl(outro_xnew)


# Weekly Totals for Compositing Section

pd_line_compositing = pd_line
pd_line_compositing["compositing week total"] = pd_line["compositing"]
pd_line_compositing

df_compositing_weektotal = pd_line_compositing

for week in df_compositing_weektotal:
    df_compositing_weektotal["compositing week total"] = df_compositing_weektotal["compositing"].groupby(df_compositing_weektotal["week"]).sum()
    
df_compositing_weektotal = df_compositing_weektotal["compositing week total"].dropna()
df_compositing_weektotal

compositing_x = list(range(1, 40))
compositing_y = []

for i in df_compositing_weektotal:
    compositing_y.append(i)
    
arr_compositing_x = np.array(compositing_x)
arr_compositing_y = np.array(compositing_y)

compositing_xnew = np.linspace(arr_compositing_x.min(), arr_compositing_x.max(), 200) 

spl = make_interp_spline(arr_compositing_x, arr_compositing_y, k=2)
compositing_y_smooth = spl(compositing_xnew)

# Plotting Sections Over Year

plt.text(1.8, 32, " Classes", fontdict = font)
plt.axvspan(0, 6, color='gray', alpha=0.5)

plt.text(14.9, 32, "Vacation", fontdict = font)
plt.axvspan(13.5, 18.5, color='gray', alpha=0.5)

plt.text(31.5, 32, "Classes", fontdict = font)
plt.axvspan(25, 40, color='gray', alpha=0.5)

plt.ylabel("Hours Worked")
plt.xlabel("Week # (April-December)")
plt.title("Specific Section Hours Worked Per Week")

plt.plot(intro_xnew, intro_y_smooth, label = "Intro")
plt.plot(verse1_xnew, verse1_y_smooth, label = "Verse 1")
plt.plot(solo_xnew, solo_y_smooth, label = "Gtr Solo")
plt.plot(verse2_xnew, verse2_y_smooth, label = "Verse 2")
plt.plot(outro_xnew, outro_y_smooth, label = "Outro")
plt.plot(compositing_xnew, compositing_y_smooth, label = "Compositing")
plt.legend(bbox_to_anchor=(1.02, 0.35), loc='upper left', borderaxespad=0)
plt.figure(figsize=(40, 10))
plt.show()