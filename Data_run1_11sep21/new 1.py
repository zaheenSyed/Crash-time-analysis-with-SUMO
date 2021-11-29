infile_tt=r'traveltimezz.csv'
    
    # infile=r'C:\Graduate Courses\Spring 2019\CGN 6938\Final Project\Final Model\sumofull.csv'
    
    
    df_tt=pd.read_csv(infile_tt, sep=';')
    df_tt['traveltime']=df_tt['traveltime']/60
    df_tt['begin']=df_tt['begin']/60
    
    time_interval=df_tt['begin'].unique()
    
    edge_list=['L23_L2','L2_L1','L3_L23','L4_L3','L4_LS4','L5_L4','L6_L5','LS3_L3','LS4_LS41s','R1_R2','R2_R3','R3_R4','R4_R5','R4_RS4','R5_R6','R6_R7','R7_R8','RS5_R5']
    
    travel_time=pd.DataFrame(np.transpose([time_interval]),columns=['time_interval'])
    travel_time['total']=0.0
    
    for j in edge_list:
        tt=df_tt[(df_tt['id2']==j)]
        tt=tt.reset_index()
        print(tt['traveltime'])
        travel_time[str(j)]=tt['traveltime']
        travel_time['total']= travel_time['total']+travel_time[str(j)]
        total_TT.append(travel_time['total'].values)
    
 
    


    
    
print(np.mean(ssm))
  
    
print(np.std(ssm))
    
print(np.mean(total_TT))
    
print(np.std(total_TT))
    