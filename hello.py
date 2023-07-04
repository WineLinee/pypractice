
print("你玩jett，开局起了半甲，从B大拉出去直接被左轮贴脸点了一枪头")
real_blood = 8
user_blood = int(input("你还剩多少滴血？请输入"))
while user_blood != real_blood:
    if user_blood < real_blood:
        print("不能就这么点血吧")
    if user_blood > real_blood:
        print("你还想剩这么多血？")
    user_blood = int(input("你还剩多少滴血？请输入"))
if user_blood == real_blood:
    print("还真是")