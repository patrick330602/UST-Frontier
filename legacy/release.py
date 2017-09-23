def findRelease(taskTime,startRelease,endRelease):
    relativeTime=taskTime.sort()
    startTime=startRelease
    slotForRelease=[]
    for task in relativeTime:
        if task[0]<=startTime:
            if task[1]>startTime:
                startTime=task[1]
            else:
        else:
            slotForRelease.append(task[0]-startTime)
        if task[0]>=endRelease:
            break
    sorting= sorted(slotForRelease)
    return sorting[-1]
