def search(n,check_list,cnt):
    if cnt > n:
        print(check_list)
        return
    search(n,check_list+[cnt],cnt+1)
    search(n,check_list,cnt+1)

search(3,[],1)
