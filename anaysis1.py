
import os
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

import glob

import os,sys

import pandas as pd

from operator import itemgetter


ssm=[] # list surrogate safety measure  
total_TT=[] # empty list to find the total Travel time

os.chdir(r'D:\Github\Crash time analysis with SUMO')

for i in range(2):
    os.system("sumo.exe "+ "I75_121_Final.sumocfg")

    input_files1 = r"ssm_v0.xml"  # from rou add xml
    input_files2 = r"traveltime.xml" #from data add xml
    input_files3 =  r"loop.xml"  # from loop add
    
    try:
    
        cmd1 = "python xml2csv.py " + input_files1
        
        os.system(cmd1)
        
        
        cmd2 = "python xml2csv.py " + input_files2
        
        os.system(cmd2)
        
        
        
        cmd3 = "python xml2csv.py " + input_files3
        
        os.system(cmd3)

    except:
        print("file made")





    #infile=r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\ACC_added_with_base model\Simulation\25_ACC\Simulation_run\ssm_v0.csv'
    
    infile=r'ssm_v0.csv'
    
    
    #infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'
    
    
    df1=pd.read_csv(infile, sep=';',)
    
    df1=df1[(df1['conflict_begin']>=1800.0) & (df1['conflict_begin']<5400.0 )]
    
    #df1(['minTTC_value','maxDRAC_value']).dropna(how='any')
    
    
    df1=df1.fillna(-1)
    
    
    #df_ttc=df1[(df1['minTTC_value']>=0) & (df1['minTTC_value']<=1.5)]
    
    df_ttc=df1[df1['minTTC_value']>=0]
    
    
    #df_ttc=df1.copy()
    print('the length of ttc data:',len(df_ttc))
    
    

    
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
    plt.show()
    
    fig.savefig(r'D:\Github\Crash time analysis with SUMO\TTC_plot_25.png',dpi=500)
    
    #n, bins, patches = ax4.hist(df1['minTTC_value'],10,density=False, facecolor='y', alpha=0.75)
    
    #df_drac=df1[(df1['maxDRAC_value']<7) & (df1['maxDRAC_value']>=1)]
    
    # the limit should be 3.5
    df_drac=df1[(df1['maxDRAC_value']>=0)]

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
    plt.show()
    
    fig5.savefig(r'D:\Github\Crash time analysis with SUMO\DRAC_plot_25.png',dpi=500)
    
    
    
    
    df_drac=df1[(df1['maxDRAC_value']>=3.30)]
    
    print('the length of drac: ',len(df_drac))
    
    print(''total length',len(df_ttc)+len(df_drac))
    
    ssm.append(len(df_ttc)+len(df_drac))
    
    print(len(df1))


    infile_tt=r'traveltimezz.csv'
    
    # infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'
    
    
    df_tt=pd.read_csv(infile_tt, sep=';')
    df_tt['traveltime']=df_tt['edge_traveltime']/60
    df_tt['begin']=df_tt['interval_begin']/60
    
    time_interval=df_tt['begin'].unique()
    
    edge_list=['L23_L2','L2_L1','L3_L23','L4_L3','L4_LS4','L5_L4','L6_L5','LS3_L3','LS4_LS41s','R1_R2','R2_R3','R3_R4','R4_R5','R4_RS4','R5_R6','R6_R7','R7_R8','RS5_R5']

    

    travel_time=pd.DataFrame(np.transpose([time_interval]),columns=['time_interval'])
    travel_time['total']=0.0
    
    for j in edge_list:
        tt=df_tt[(df_tt['edge_id']==j)]
        tt=tt.reset_index()
        # print(tt['edge_traveltime'])
        travel_time[str(j)]=tt['edge_traveltime']
        travel_time['total']= travel_time['total']+travel_time[str(j)]
        total_TT.append(travel_time['total'].values)
    

    
    
print(np.mean(ssm))
  
    
print(np.std(ssm))
    
print(np.mean(total_TT))
    
print(np.std(total_TT))
    
