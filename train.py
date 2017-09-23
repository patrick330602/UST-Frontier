import collections
import queue

def train(data):
    node={}
    edge=collections.defaultdict(list)
    edgeFarther={}
    havevisit={}
    for station in data['stations']:
        node[station['name']] = {'p': station['passengers'], 'cnt': station['passengers']}
        havevisit[station['name']] = False
        for con in station.connections:
            v = con.station
            edge[station].append({'next': v, 'line': con.line})

    q=queue.Queue()
    q.put(data['destination'])
    while not q.empty():
        u=q.get()
        for e in edge[u]:
            v=e['next']
            if not havevisit[v]:
                havevisit[v]=True
                q.put(v)
                edgeFarther[u].put(v)

    def dfs(u):
        for e in edgeFarther[u]:
            v=e.next
            dfs(v)
            cnt[u]=cnt[u]+cnt[v]

    dfs(data['destination'])

    line='bug'
    totalNumOfPassengers=0
    reachingVia='bug'

    for e in edge[data['destination']]:
        v=e['next']
        if cnt[v]>totalNumOfPassengers:
            totalNumOfPassengers=cnt[v]
            line=e['line']
            reachingVia=e['name']

    return line, totalNumOfPassengers, reachingVia
