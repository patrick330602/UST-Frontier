#taskTime is the a nested list consisting the start time and end time of each tasks (relative to the start of release time)
#startRelease is the start time of the first possible release
#endRelease is the time that release must be finished

def findRelease(taskTime,startRelease,endRelease):
    relativeTime=taskTime.sort()
    startTime=startRelease
    slotForRelease=[]
    for task in relativeTime:
        if task[0]<=startTime:
            if task[1]>startTime:
                startTime=task[1]
        else:
            slotForRelease.append(task[0]-startTime)
        if task[0]>=endRelease:
            break
    sorting= sorted(slotForRelease)
    return sorting[-1]
