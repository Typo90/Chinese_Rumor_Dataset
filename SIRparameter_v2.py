import json
import  matplotlib.pyplot as plt
import datetime
from scipy.integrate import odeint
import numpy as np


start_date_left = '2012-09-11 11:00:00'
start_date_left = datetime.datetime.strptime(start_date_left, "%Y-%m-%d %H:%M:%S")
end_date_right = '2012-09-13 09:00:00'
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


# describe the model
def deriv(y, t, N, S2I, S2R, I2R, Iforget, k=10):
    S, I, R = y
    dSdt = -(S2I + S2R) * S * I
    dIdt = S2I * S * I - I2R * I * (I + R) - Iforget * I
    dRdt = S2R * S * I + I2R * I * (I + R) + Iforget * I
    dSdt, dIdt, dRdt = k*dSdt/N, k*dIdt/N, k*dRdt/N
    return dSdt, dIdt, dRdt

#N = 10000
N = 39
I0 = 1
R0 = 0
S0 = N - I0 - R0
#S2I = 0.2
#I2R = 0.1 0.8
#S2R =
#Iforget = 0.3
S2I = 0.99
S2R = 0.01
I2R = 0.147
Iforget = 0
k = 10
t = np.linspace(0, 46, 100) # Grid of time points (in days)
y0 = S0, I0, R0 # Initial conditions vector

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, S2I, S2R, I2R, Iforget, k))
#print (ret.T)
S, I, R = ret.T

def plotsir(t, S, I, R):
    f, ax = plt.subplots(1,1,figsize=(10,4))
    ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
    #ax.plot(t, I, 'y', alpha=0.7, linewidth=2, label='Infected')
    #ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
    ax.plot(count_list,  color='gray', marker='o',alpha=0.7, linewidth=2, label='real_data:Susceptible')
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('No. of users')

    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)

    #x = time_list
    #y = count_list
    #plt.plot(x,y)
    
    plt.show();

plotsir(t, S, I, R)
