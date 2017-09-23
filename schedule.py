
# coding: utf-8

# In[84]:

import datetime
def cal_time(input_string):
    a = input_string.split(";")
    try:
        length = int(a[0])
    except:
        length = -1
    a1 = a[1].split(" ")
    a2 = a[2].split(" ")
    b1 = a1[0].split("-")
    b2 = a1[1].split(":")
    c1 = a2[0].split("-")
    c2 = a2[1].split(":")
    
    if 'Z' in b2[2]:
        second = b2[2].split("Z")[0]
        difference = 0
    elif '+' in b2[2]:
        second = b2[2].split("+")[0]
        difference = int(b2[2].split("+")[1])
        difference = difference//100
    elif '-' in b2[2]:
        second = b2[2].split("-")[0]
        difference = int(b2[2].split("-")[1])
        difference = difference//100
        difference = -difference

    year = int(b1[2])
    month = int(b1[1])
    day = int(b1[0])
    hour = int(b2[0])
    minute = int(b2[1])
    second = int(float(second))
    ms = int((float(second)-int(float(second)))*1000000)
    start_time = datetime.datetime(year,month,day,hour,minute,second,ms)
    year = int(c1[2])
    month = int(c1[1])
    day = int(c1[0])
    hour = int(c2[0])
    minute = int(c2[1])
    second = int(float(second))
    ms = int((float(second)-int(float(second)))*1000000)
    end_time = datetime.datetime(year,month,day,hour,minute,second,ms)
    start_time = start_time - datetime.timedelta(hours = difference)
    end_time = end_time - datetime.timedelta(hours = difference)
    return [length, start_time, end_time]


# In[85]:

def findRelease(task_list, start_release, end_release):
    task_list.sort()
    label = start_release
    slot=[]
    for task in task_list:
        if task[0] > end_release:
            slot.append(end_release-label)
            break
        if task[0] > label:
            slot.append(task[0]-label)
            label = task[1]
        elif task[1] > label:
            label = task[1]
        else:
            label = label
        if label > end_release:
            break
    slot.sort()
    return str(int(slot [len(slot)-1]))


# In[86]:

[length,base_start_time,base_end_time]= cal_time("3;28-05-2017 13:00:00.000+0800;28-05-2017 16:00:00.000+0800")
string = ["London morning trading check;28-05-2017 05:15:00.000Z;28-05-2017 06:15:00.000Z",
         "Tokyo risk testing;28-05-2017 16:15:00.000+0900;28-05-2017 16:45:00.000+0900",
         "New York midnight database check;28-05-2017 03:50:00.000-0400;28-05-2017 03:59:00.000-0400"]
task_list = [[]]*length
for i in range(length):
    task_list[i] = [0,0]
for i in range(length):
    [length,start_time,end_time] = cal_time(string[i])
    task_list[i] = [(start_time-base_start_time).total_seconds(),(end_time-base_start_time).total_seconds()]
print(task_list)
start_release = (base_start_time-base_start_time).total_seconds()
end_release = (base_end_time-base_start_time).total_seconds()
findRelease(task_list,start_release,end_release)


# In[ ]:


