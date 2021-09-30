
import os
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

import glob

import os,sys

import pandas as pd

from operator import itemgetter


ssm=[]
total_TT=[]

os.chdir(r'D:\Github\Crash time analysis with SUMO\Data_run1_11sep21')

for i in range(2):
    #os.system("sumo.exe "+ "I75_FInal.sumocfg")

    input_files1 = r"ssm_v0.xml" 
    input_files2 = r"traveltime.xml" 
    input_files3 =  r"loop.xml" 
    
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
    
    
    df_ttc=df1[(df1['minTTC_value']>=0) & (df1['minTTC_value']<=1.5)]
    
    #df_ttc=df1[df1['minTTC_value']>=0]
    
    
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
    plt.show()
    
    #fig5.savefig(r'C:\Research\TRB Paper ACC impact during hurricane evacuation\SUMO\Based Model\Data_analysis\DRAC_plot_25.png',dpi=500)
    
    
    
    
    df_drac=df1[(df1['maxDRAC_value']>=3.30)]
    
    print('the length of drac: ',len(df_drac))
    
    print(''total length',len(df_ttc)+len(df_drac))
    
    ssm.append(len(df_ttc)+len(df_drac))
    
    print(len(df1))


    infile_tt=r'traveltime.csv'
    
    # infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'
    
    
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
        # print(tt['edge_traveltime'])
        travel_time[str(j)]=tt['edge_traveltime']
        travel_time['total']= travel_time['total']+travel_time[str(j)]
        total_TT.append(travel_time['total'].values)
    

    
    
print(np.mean(ssm))
  
    
print(np.std(ssm))
    
print(np.mean(total_TT))
    
print(np.std(total_TT))
    
