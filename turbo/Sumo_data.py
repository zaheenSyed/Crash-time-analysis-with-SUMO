# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 04:32:02 2019

@author: rezac
"""

import os
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

import glob

import os,sys

import pandas as pd

from operator import itemgetter
#combining Insync files



#in_path = r"C:\Research\NSF_Population_behaviour\Social Media\IRMA\IRMA_Data\UserBasedCollection\Back_Track" 
in_path=r"C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run" 
                  



############################################################################################

#Reading Field Data

infile=r'Field_data_clean2.csv'

df=pd.read_csv(infile)

df_field=df.filter(['interval_id','interval_begin','speed','flow'])


#df_field=df_field.sort_values(['interval_id'])
#
df_field=df_field[(df_field['interval_begin']>=1800) & (df_field['interval_begin']<5400)]
df_field=df_field.reset_index(drop=True)

#df_field.to_csv(r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run\Field_data_filter.csv')

#Reading Simulation Data

infile_loop=r"loop.csv"

df_loop=pd.read_csv(infile_loop, sep=";",usecols=['interval_id','interval_begin','interval_flow','interval_speed'])

df_loop=df_loop.sort_values(['interval_id'])

loop_id=pd.unique(df_loop['interval_id'])

loop_det=[]

df_sort=pd.DataFrame()

for i in range (len(df_loop)):
    interval_id=df_loop['interval_id'][i].split('_')
    loop_no=interval_id[0]
    lane_no=interval_id[1]
    #print(loop_no)
    loop_det.append([loop_no,lane_no])
    #lane_no.append(int(lane_no))

det=pd.DataFrame(loop_det,columns=['loop_det','lane_no'])   
df_loop['loop_det']=det['loop_det']
df_loop['lane_no']=det['lane_no']
df_loop=df_loop.sort_values(['loop_det','interval_begin'])

flow=df_loop.filter(['interval_begin','loop_det','interval_flow'])

grp_flow=flow.groupby(['interval_begin','loop_det']).sum()
#df_loop=df_loop.sort_values(['interval_begin'])
grp_flow=grp_flow.reset_index()
grp_flow=grp_flow.sort_values(['loop_det'])
  
speed=df_loop.filter(['interval_begin','loop_det','interval_speed'])

grp_speed=speed.groupby(['interval_begin','loop_det']).mean()
#df_loop=df_loop.sort_values(['interval_begin'])
grp_speed=grp_speed.reset_index()

grp_speed=grp_speed.sort_values(['loop_det','interval_begin'])

df_sim=pd.merge(grp_flow, grp_speed, on=['loop_det','interval_begin'])
df_sim=df_sim.sort_values(['loop_det','interval_begin'])


#df_field=df_field.set_index(['interval_begin'],drop=True)
df_sim=df_sim[(df_sim['interval_begin']>=1800) & (df_sim['interval_begin']<5400)]

df_sim=df_sim.reset_index(drop=True)

#df_sim.to_csv(r"C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run\sim_data.csv")



df_sim['interval_aspiredFlow']=df_field['flow']
df_sim['interval_aspiredSpeed']=df_field['speed']

df_sim['interval_aspiredSpeed']=df_sim['interval_aspiredSpeed'].replace(to_replace=0, method='ffill')
df_sim['interval_speed']=df_sim['interval_speed'].replace(to_replace=-1, method='ffill')


df_filter=df_sim

#df_filter=df_sim[(df_sim['interval_begin']>=1800) & (df_sim['interval_begin']<5400)]
#df_filter=df_sim
#df_filter=df_filter[(df_filter['loop_det']!='loop3')]
#df_filter=df_filter[(df_filter['loop_det']!='loop6')]
#df_filter=df_filter[(df_filter['loop_det']!='loop7')]
#df_filter=df_filter[(df_filter['loop_det']!='loop8')]
#GEH score calculation

#df_filter=df_filter.sort_values(['interval_id'])

#df_filter=df_filter.reset_index(drop=True)

df_filter['GEH']=np.sqrt(2*(df_filter['interval_aspiredFlow']-df_filter['interval_flow'])**2/(df_filter['interval_aspiredFlow']+df_filter['interval_flow']))
df_filter['GEH']=df_filter['GEH'].fillna(0)

count=df_filter[df_filter['GEH']<5]

percentage_passing=(len(count)*100)/len(df_filter)

print("GEH :", percentage_passing)

#absolute speed check



df_filter['abs_speed_diff']=np.abs(df_filter['interval_aspiredSpeed']-df_filter['interval_speed'])

df_filter['abs_speed_diff']=df_filter['abs_speed_diff'].fillna(0)

count=df_filter[df_filter['abs_speed_diff']<5]

percentage_passing=(len(count)*100)/len(df_filter)

print("abs_speed_diff :", percentage_passing)

det=df_filter['loop_det'].unique()

count=[]

for i in det:
    count_geh=len(df_filter[(df_filter['loop_det']==i) & (df_filter['GEH']<5)])
    count_speed=len(df_filter[(df_filter['loop_det']==i) & (df_filter['abs_speed_diff']<5)])
    count.append([i, count_geh,count_speed])

print(count)

#df_filter.to_csv(r"C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run\calibration_data.csv")


'''



infile=r"C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\Based Model\Data_analysis\Best_Result\calibration_data_final_result.csv"

df=pd.read_csv(infile)







calib=df['loop_det'].unique()

RMSPE_flow_list=[]
RMSPE_speed_list=[]



for i in calib:
    
    df1=df[df['loop_det']==i]
    #df1['interval_begin']=df1['interval_begin']/60
    #df1=df1[(df1['interval_begin']>=30) & (df1['interval_begin']<=90)]
    #df1['interval_speed']=pd.to_numeric(df1['interval_speed'])
    
    
    fig1,ax1 = plt.subplots(figsize=(10,6))
    ax1.plot(df1['interval_begin'], df1['interval_aspiredFlow'],label='actual_data')
    ax1.plot(df1['interval_begin'],df1['interval_flow'],label='simlated_data')
    #ax1.set_xlimit(18,)
    ax1.set_xlabel('Time Interval in Minutes',size=18)
    ax1.set_ylabel('Flow in vph',size=18)
    ax1.set_title('Flow Variation',size=20)
    plt.legend()
    plt.tight_layout()
    plt.show()
    fig1.savefig(r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Data Analysis/'+str(i)+'flow_plot.png',dpi=500)
    
    RMSPE_flow = np.sqrt(np.mean(np.square(((df1['interval_flow'] - df1['interval_aspiredFlow']) / df1['interval_aspiredFlow'])), axis=0))
    RMSE_flow=np.sqrt( mean_squared_error(df1['interval_flow'],df1['interval_aspiredFlow']))
    RMSPE_flow_list.append([i, RMSPE_flow, RMSE_flow])
    
    fig2,ax2 = plt.subplots(figsize=(10,6))
    ax2.plot(df1['interval_begin'], df1['interval_aspiredSpeed'],label='actual_data')
    ax2.plot(df1['interval_begin'],df1['interval_speed'],label='simulated_data')
    ax2.set_xlabel('Time Interval in Minutes',size=18)
    ax2.set_ylabel('Speed in m/s',size=18)
    ax2.set_title('Speed Variation',size=20)
    plt.legend()
    plt.tight_layout()
    fig2.savefig(r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Data Analysis/'+str(i)+'speed_plot.png',dpi=500)
    
    RMSPE_speed= np.sqrt(np.mean(np.square(((df1['interval_speed'] - df1['interval_aspiredSpeed']) / df1['interval_aspiredSpeed'])), axis=0))
    print("RMSPE_speed:", RMSPE_speed)
    RMSE_speed=np.sqrt( mean_squared_error(df1['interval_speed'],df1['interval_aspiredSpeed']))
    RMSPE_speed_list.append([i, RMSPE_speed, RMSE_speed])
    










file = open(r"C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Data Analysis\error_1.txt","w") 

file.write("RMSPE_flow_list:",) 

file.write(str(RMSPE_flow_list)) 

file.write("\n RMSPE_speed_list:") 

file.write(str(RMSPE_speed_list)) 
file.write(str(RMSPE_speed_list)) 


file.write("\n No of Accident:") 

file.write(str(n)) 

file.close()

df.to_csv(r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Data Analysis\Initial_data.csv')





infile_tt=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\traveltime.csv'

#infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'


df_tt=pd.read_csv(infile_tt, sep=';')
df_tt['edge_traveltime']=df_tt['edge_traveltime']/60
df_tt['interval_begin']=df_tt['interval_begin']/60

time_interval=df_tt['interval_begin'].unique()

edge_list=["1to2","2to3","34","4to5","5to6","R4_R5","7to8","8to9","9to10","10to11","11to12","R6_R7"]

travel_time=pd.DataFrame(np.transpose([time_interval]),columns=['time_interval'])
travel_time['total']=0.0

for j in edge_list:
    tt=df_tt[(df_tt['edge_id']==j)]
    tt=tt.reset_index()
    print(tt['edge_traveltime'])
    travel_time[str(j)]=tt['edge_traveltime']
    travel_time['total']= travel_time['total']+travel_time[str(j)]

    


 
fig3,ax3 = plt.subplots(figsize=(10,6))
ax3.plot(travel_time['time_interval'], travel_time['total'],'*-',color='c')
ax3.set_xlabel('Time Interval in Minutes',size=18)
ax3.set_ylabel('Travel Time in Minutes',size=18)
ax3.set_title('Travel Time Variation',size=20)
#plt.legend()
plt.tight_layout()
fig3.savefig(r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Data Analysis\traveltime_plot.png',dpi=500)





#df1=df1[(df1['conflict_begin']>1800) & (df1['conflict_begin']<5400) ]



import numpy as np
import matplotlib.pyplot as plt
'''

ssm=[]
total_TT=[]

os.chdir(r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run')

for i in range(20):
    os.system("sumo.exe "+ "I75_FInal.sumocfg")

    input_files1 = r"ssm_v0.xml" 
    input_files2 = r"traveltime.xml" 
    input_files3 =  r"loop.xml" 
    
    
    
    cmd1 = "python xml2csv.py " + input_files1
    
    os.system(cmd1)
    
    
    cmd2 = "python xml2csv.py " + input_files2
    
    os.system(cmd2)
    
    
    
    cmd3 = "python xml2csv.py " + input_files3
    
    os.system(cmd3)








    infile=r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run\ssm_v0.csv'
    
    #infile=r'ssm_v0_TTC.csv'
    
    
    #infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'
    
    
    df1=pd.read_csv(infile, sep=';',)
    
    df1=df1[(df1['conflict_begin']>=1800.0) & (df1['conflict_begin']<5400.0 )]
    
    #df1(['minTTC_value','maxDRAC_value']).dropna(how='any')
    
    
    df1=df1.fillna(-1)
    
    
    df_ttc=df1[(df1['minTTC_value']>=0) & (df1['minTTC_value']<=1.5)]
    
    #df_ttc=df1[df1['minTTC_value']>=0]
    
    
    #df_ttc=df1.copy()
    print(len(df_ttc))
    
    
    '''
    
    # the histogram of the data
    
    fig, ax4=plt.subplots(figsize=(6,4))
    
    n, bins, patches = ax4.hist(df_ttc['minTTC_value'],40,density=False, facecolor='y', alpha=0.75)
    
    
    #ax4.hist(df_ttc['minTTC_value'])
    ax4.set_xlabel('Time to Collision',size='14')
    ax4.set_ylabel('Frequency',size='14')
    ax4.set_title('Distribution for TTC Value',size='14')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #ax4.axis([0.62,3.1,0,250])
    ax4.grid(True)
    plt.tight_layout()
    #plt.show()
    
    #fig.savefig(r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\Based Model\Data_analysis\TTC_plot_25.png',dpi=500)
    
    #n, bins, patches = ax4.hist(df1['minTTC_value'],10,density=False, facecolor='y', alpha=0.75)
    
    #df_drac=df1[(df1['maxDRAC_value']<7) & (df1['maxDRAC_value']>=1)]
    
    
    df_drac=df1[(df1['maxDRAC_value']>=3.30)]

    fig5, ax5=plt.subplots(figsize=(6,4))
    #ax5.hist(df_drac['maxDRAC_value'])
    
    n, bins, patches = ax5.hist(df_drac['maxDRAC_value'],40,density=False, facecolor='y', alpha=0.75)
    
    ax5.set_xlabel('Maximum DRAC Value',size='14')
    ax5.set_ylabel('Frequency',size='14')
    ax5.set_title('Distribution for Maximum DRAC Value',size='14')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #ax5.axis([0.5,3.0,0,90])
    ax5.grid(True)
    plt.tight_layout()
    #plt.show()
    
    #fig5.savefig(r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\Based Model\Data_analysis\DRAC_plot_25.png',dpi=500)
    
    '''
    
    
    df_drac=df1[(df1['maxDRAC_value']>=3.30)]
    
    print(len(df_drac))
    
    print(len(df_ttc)+len(df_drac))
    
    ssm.append(len(df_ttc)+len(df_drac))
    
    print(len(df1))


    infile_tt=r'traveltime.csv'
    
    #infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'
    
    
    df_tt=pd.read_csv(infile_tt, sep=';')
    df_tt['edge_traveltime']=df_tt['edge_traveltime']/60
    df_tt['interval_begin']=df_tt['interval_begin']/60
    
    time_interval=df_tt['interval_begin'].unique()
    
    edge_list=["1to2","2to3","3to4","4to5","5to6","R4_R5","7to8","8to9","9to10","10to11","11to12","R6_R7"]
    
    travel_time=pd.DataFrame(np.transpose([time_interval]),columns=['time_interval'])
    travel_time['total']=0.0
    
    for j in edge_list:
        tt=df_tt[(df_tt['edge_id']==j)]
        tt=tt.reset_index()
        #print(tt['edge_traveltime'])
        travel_time[str(j)]=tt['edge_traveltime']
        travel_time['total']= travel_time['total']+travel_time[str(j)]
        total_TT.append(travel_time['total'].values)
    
    
    
    
print(np.mean(ssm))
  
    
print(np.std(ssm))
    
print(np.mean(total_TT))
    
print(np.std(total_TT))
    
