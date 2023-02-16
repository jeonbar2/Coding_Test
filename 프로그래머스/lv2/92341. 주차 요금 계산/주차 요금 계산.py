def solution(fees, records):
    import math
    answer = []
    dict_time={}
    #fees=[기본시간 , 기본요금, 단위시간, 단위요금]
    # 기본요금+[(누적시간 - 기본시간 )/단위사간]*단위요금
    for i in records: # dict로 차량번호당 출입시간 저장
        time,number,states = i.split(" ")
        if not number in dict_time.keys():
            dict_time[number]=[time]
        else:
            dict_time[number].append(time)
    
    for i in dict_time: # 출입시간이 짝이 안맞을경우 23:59에 출차한거로 추가
        if (len(dict_time[i]))%2!=0:
            dict_time[i].append("23:59")
    dict_ac_time={}
    for i in dict_time:
        temp=0
       # print(dict_time[i])
        for j in range(0,len(dict_time[i])):
            
            if j%2==0:
                temp -= (60 * int(dict_time[i][j].split(":")[0]))+int(dict_time[i][j].split(":")[1])
            else :
                temp +=(60 * int(dict_time[i][j].split(":")[0]))+int(dict_time[i][j].split(":")[1])
            # print(temp)
        dict_ac_time[i]=temp
    # print(dict_ac_time)
    #fees=[기본시간 , 기본요금, 단위시간, 단위요금]
    # 기본요금+[(누적시간 - 기본시간 )/단위사간]*단위요금
    
    
    dict_ac_time = dict(sorted(dict_ac_time.items()))
    
    for i in dict_ac_time:
        if dict_ac_time[i]-fees[0]>0:
            answer.append(fees[1]+math.ceil((dict_ac_time[i]-fees[0])/fees[2])*fees[3])
        else :
            answer.append(fees[1])
    return answer