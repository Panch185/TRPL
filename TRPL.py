import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
from tkinter import *
import re
import json
import sys
from io import StringIO
#импорт
root = tk.Tk()
root.destroy()

call_technology = filedialog.askopenfilename(title="Выберите файл")
with open(call_technology) as file:
    data = json.load(file)
a=open(call_technology)
b = a.read()
s = b.count('"start_temp"')
print(s)
h = open(call_technology)
j = h.read()
#бекенд
sorted_ovens = sorted(data['ovens'], key=lambda x: x['start_temp'])
def calculate_oven_time(oven, target_temp):
    time = 0
    current_temp = oven['start_temp']
    for temp in oven['working_temps']:
        if temp > current_temp:
            time += 2
        else:
            time += 2
        current_temp = temp
    if current_temp < target_temp:
        time += 2
    return time
schedule = []
current_time = 0
for oven in sorted_ovens:
    oven_time = calculate_oven_time(oven, 0)
    start_time = max(current_time, oven_time)
    end_time = start_time + oven_time
    schedule.append({
        'oven': oven,
        'start_time': start_time,
        'end_time': start_time + oven_time
    })
    current_time = start_time + oven_time
total_time = schedule[-1]['end_time'] + 2

print(f"Общее время работы печей за день: {total_time}")
for task in schedule:
    print(f"Печь: {task['oven']}")
    print(f"Время старта: {task['start_time']}")
    print(f"Время окончания: {task['end_time']}")
    print()
for task in schedule:
    b = task['oven']
    v = task['start_time']
    n = task['end_time']
#график
fig, ax = plt.subplots()
plt.title('График печей')
ax.set_xlabel('Время')
ax.set_yticklabels([' ', '1 печь', '2 печь', '3 печь', '4 печь', '5 печь', '6 печь', '7 печь'])
ax.grid(True)
data2 = {'Task': ['splav', 'splav2', 'splav3'],
        'Start': [v, v, v],
        'End': [n, n, n ]}

df = pd.DataFrame(data2)


for i, task in df.iterrows():
    ax.barh(1, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 1, task['Task'], ha='center', va='center', color='black')
for i, task in df.iterrows():
    ax.barh(2, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 2, task['Task'], ha='center', va='center', color='black')
for i, task in df.iterrows():
    ax.barh(3, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 3, task['Task'], ha='center', va='center', color='black')
for i, task in df.iterrows():
    ax.barh(4, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 4, task['Task'], ha='center', va='center', color='black')
for i, task in df.iterrows():
    ax.barh(5, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 5, task['Task'], ha='center', va='center', color='black')
for i, task in df.iterrows():
    ax.barh(6, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 6, task['Task'], ha='center', va='center', color='black')
for i, task in df.iterrows():
    ax.barh(7, task['End']-task['Start'], left=task['Start'], height=0.3, align='center', color='b', alpha=0.75)
    ax.text((task['Start']+task['End'])/2, 7, task['Task'], ha='center', va='center', color='black')

plt.show()
root.mainloop()