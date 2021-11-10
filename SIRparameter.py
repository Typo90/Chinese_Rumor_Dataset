import json
import  matplotlib.pyplot as plt
import datetime

start_date_left = '2012-09-11 11:00:00'
start_date_left = datetime.datetime.strptime(start_date_left, "%Y-%m-%d %H:%M:%S")
end_date_right = '2012-09-16 17:00:00'
end_date_right = datetime.datetime.strptime(end_date_right, "%Y-%m-%d %H:%M:%S")
start_date_right = start_date_left+ datetime.timedelta(hours=1)
time_list = [start_date_left]
while (start_date_right < end_date_right):
    time_list.append(start_date_right)
    start_date_left = start_date_right
    start_date_right = start_date_left+ datetime.timedelta(hours=1) 
#print (time_list)

#test
test= '2012-09-11 11:35:48'
test_rumor_date = datetime.datetime.strptime(test, "%Y-%m-%d %H:%M:%S")

print('rumor')
print(test_rumor_date)
print('left')
print(time_list[1])
print (test_rumor_date > time_list[1] and test_rumor_date <= time_list[2])



count_list = [0]*len(time_list)
j = 0
i = 0

with open('0_rumor_origin.json','r',encoding='utf-8') as jsonfile:
    json_string = json.load(jsonfile)
    for comment in json_string:
        for element in comment:
            if element == 'date':
                rumor_date = datetime.datetime.strptime(comment['date'], "%Y-%m-%d %H:%M:%S")
                print(rumor_date)

                while(i < len(time_list)-1):
                    if (rumor_date > time_list[i] and rumor_date <= time_list[i+1]):
                        print('yes')
                        count_list[i] = count_list[i]+1
                    i = i+1
                i = 0
                        


                
                
print (count_list)
print(len(count_list))


x = time_list
y = count_list
plt.plot(x,y)
plt.show()

