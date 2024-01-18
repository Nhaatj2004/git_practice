class Info:
    def __init__(self,name,In,out):
        self.name=name
        self.In=In
        self.out=out
    def __lt__(self, other):
        if(self.In==other.In): return self.out<other.out
        return self.In<other.In
def check(dict):
    for x in dict.keys():
        if(dict[x]==0):
            return True
    return False
def rooms(list):
    visited={}
    for i in range(0,len(list)):
        visited[list[i]]=0
    room=0
    while check(visited):
        room+=1
        obj=Info(None,None,None)
        for i in range(0, len(list)):
            if visited[list[i]]==0:
                obj.name=list[i].name
                obj.In=list[i].In
                obj.out=list[i].out
                visited[list[i]]=1
                break
        print(obj.name,obj.In,obj.out)
        for i in range(0,len(list)):
            if visited[list[i]]==0 and list[i].In>=obj.out:
                obj.name = list[i].name
                obj.In = list[i].In
                obj.out = list[i].out
                visited[list[i]]=1
    print(room)

guest_list=[]
while True:
    print("--------")
    print("MENU:")
    print("1.Add guest")
    print("2.Show list")
    print("3.Calculate minimum room")
    print("4.Exit")
    print("--------",end="\n")
    q=int(input())
    if q==1:
        print("Nhap ten:",end="")
        name=str(input())
        print("Nhap thoi gian check in:", end="")
        In=int(input())
        print("Nhap thoi gian check out:", end="")
        out=int(input())
        p1=Info(name,In,out)
        guest_list.append(p1)
    elif q==2:
        for i in range(0,len(guest_list)):
            print("--------")
            print("Guest name:"+guest_list[i].name)
            print("Check in time: "+str(guest_list[i].In))
            print("Check out time: "+str(guest_list[i].out))
            print("--------", end="\n")
    elif q==4: break
    elif q==3:
        guest_list.sort()
        rooms(guest_list)
