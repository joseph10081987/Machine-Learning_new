# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:57:20 2019

@author: HA163WN
"""

#from pulp import *
def jspl():
    import pandas as pd
    import string
    import numpy as np
    import warnings
    warnings.filterwarnings("ignore")
    import json

    #Read json file
    #with open(grade_json,"r")as read_file:
        #grade=json.load(read_file)

    #Reading the contents of the excel file - 10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx
    Mn_in = pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx", sheet_name = "Model_Angul")
    A_in = pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx", sheet_name = "Inputs_Demand_Plan_Angul",\
                         header=[3])
    B_in = pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx", sheet_name = "Inputs_Aim_Chemistry_Angul",\
                         header=[1])
    C_in = pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx", sheet_name = "Inputs_Ferro_Alloys_Angul",\
                         header=[1])
    D_in = pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx", sheet_name = "Inputs_Grade Classification")
    E_in = pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx", sheet_name = "Inputs_Opening_Chemistry",\
                         header=[1])

    A_in=A_in.drop(A_in.columns[0],axis=1)
    df = A_in

    A_in

    opening_temp=pd.DataFrame(E_in.iloc[14,:]).T
    opening_temp=opening_temp[['     C', '     MN','     S', '      P', '   SI', '    AL', '    CU', '     CA', '    NI',
           '     CR', '     MO', '    TI', '     V', '     NB', '      B']]
    opening_temp.columns=["OP_%C","OP_%Mn","OP_%S","OP_%P","OP_%Si","OP_%Al","OP_%Cu","OP_%Ca","OP_%Ni","OP_%Cr","OP_%Mo",\
                          "OP_%Ti","OP_%V","OP_%Nb","OP_%B"]
    opening_temp.reset_index(drop=True)
    opening_chemistry_final = pd.DataFrame(np.repeat(opening_temp.values,25,axis=0))
    opening_chemistry_final.columns = opening_temp.columns

    input_chemistry=pd.DataFrame(E_in.iloc[0,:]).T
    input_chemistry = pd.DataFrame(input_chemistry.iloc[0,4:]).T
    input_chemistry=input_chemistry.fillna(0)
    input_chemistry=input_chemistry.astype(float)
    input_chemistry.columns = ['IN_%C', "IN_%Mn","IN_%S","IN_%P","IN_%Si","IN_%Al","IN_%Cu","IN_%Ca","IN_%Ni",\
                               "IN_%Cr","IN_%Mo","IN_%Ti","IN_%V","IN_%Nb","IN_%B"]
    input_chemistry.reset_index(drop=True, inplace=True)
    input_chemistry
    input_chemistry_final = pd.DataFrame(np.repeat(input_chemistry.values,25,axis=0))
    input_chemistry_final.columns = input_chemistry.columns

    df_merged = pd.concat([df,input_chemistry],axis=1)
    df2 = B_in.iloc[:,2:]
    df2.columns=['Grade', 'Blank1', '%C', '%Mn', '%S', '%P', '%Si', '%Al', '%Cu',
           '%Ca', '%Ni', '%Cr', '%Mo', '%Ti', '%V', '%Nb', '%B', 'Blank2',
           'LB_%C', 'LB_%Mn', 'LB_%S', 'LB_%P', 'LB_%Si', 'LB_%Al', 'LB_%Cu', 'LB_%Ca',
           'LB_%Ni', 'LB_%Cr', 'LB_%Mo', 'LB_%Ti', 'LB_%V', 'LB_%Nb', 'LB_%B',
           'Blank3', 'UB_%C', 'UB_%Mn', 'UB_%S', 'UB_%P', 'UB_%Si', 'UB_%Al',
           'UB_%Cu', 'UB_%Ca', 'UB_%Ni', 'UB_%Cr', 'UB_%Mo', 'UB_%Ti', 'UB_%V', 'UB_%Nb',
           'UB_%B']

    df2=df2.fillna(0.0)
    df2=df2.drop(['Blank1','Blank2','Blank3'],axis=1)
    df2_values=df2.iloc[:,1:]
    df2_grade=df2[["Grade"]]
    #df2_grade=grade
    df2_values=df2_values/100
    df2=pd.concat([df2_grade,df2_values],axis=1)
    s = df['Grade'].values.tolist()
    n=len(df2['Grade'])

    for i in range (0,n):
        if s[0]==(df2['Grade'][i]):
            k=df2.iloc[i]

    # code for lower bound and upper bound
    for i in range (0,n):
        if s[0]==(df2['Grade'][i]):
            k=df2.iloc[i]
            data = k[16:31]
            #data.append(k[18:33])
            ls = pd.DataFrame(data)
            transposed_df =ls.T
            #print(transposed_df)

    lowerbound=transposed_df.reset_index(drop=True)

    lb_list = lowerbound.values.tolist()[0]
    tempdf=pd.DataFrame(index=range(25),columns=range(15))

    lb_col=["LB_%C","LB_%Mn","LB_%S","LB_%P","LB_%Si","LB_%Al","LB_%Cu","LB_%Ca","LB_%Ni","LB_%Cr","LB_%Mo","LB_%Ti",\
            "LB_%V","LB_%Nb","LB_%B"]

    tempdf.columns=lb_col

    #len(lb_list)

    #transposed_df.iloc[0,4]

    for j in range(25):
        for i in range(15):
            tempdf.iloc[j,i]=lb_list[i]

    lowerbound_final=tempdf

    # code for lower bound and upper bound
    #df_repeated = []
    for i in range (0,n):
        if s[0]==(df2['Grade'][i]):
            k=df2.iloc[i]
            data = k[31:]
            #data.append(k[18:33])
            ls = pd.DataFrame(data)
            transposedub_df =ls.T
            #print(transposedub_df)

    lb_list = transposedub_df.values.tolist()[0]
    tempdfub=pd.DataFrame(index=range(25),columns=range(15))

    lb_col=["UB_%C","UB_%Mn","UB_%S","UB_%P","UB_%Si","UB_%Al","UB_%Cu","UB_%Ca","UB_%Ni","UB_%Cr","UB_%Mo",\
            "UB_%Ti","UB_%V","UB_%Nb","UB_%B"]

    tempdfub.columns=lb_col

    #len(lb_list)

    #transposed_df.iloc[0,4]

    for j in range(25):
        for i in range(15):
            tempdfub.iloc[j,i]=lb_list[i]

    upperbound_final=tempdfub
    #upperbound_final

    df4 = C_in.iloc[:,1:]
    df4.columns=['Ferro Alloys_Name', 'Ferro Alloys_Code', 'Include', 'FA_%C', 'FA_%Mn', 'FA_%S',
           'FA_%P', 'FA_%Si', 'FA_%Al', 'FA_%Cu', 'FA_%Ca', 'FA_%Ni', 'FA_%Cr', 'FA_%Mo', 'FA_%Ti', 'FA_%V',
           'FA_%Nb', 'FA_%B', 'Consider (Y/N)', 'Cost Per Tonne', 'Unnamed: 21',
           'Supply Capacity (Tons)']
    df4=df4.drop(['Unnamed: 21'],axis=1)
    columns = ['Supply Capacity (Tons)','Ferro Alloys_Code','Include']
    df4.drop(columns, inplace=True, axis=1)

    ferro_alloy=df4.iloc[0:25,1:16]
    ferro_alloy=ferro_alloy.fillna(0.0)

    cost_fa=df4["Cost Per Tonne"].iloc[0:25]

    quantity=pd.DataFrame(columns=range(0,1),index=range(0,26))
    quantity.columns=["Quantity"]
    quantity=quantity.fillna(df["Qty (MT)"][0])

    consider=pd.DataFrame(df4["Consider (Y/N)"][0:25])
    consider.columns=['Consider1']
    consider_final=consider.copy()
    consider_final["Consider2"]=consider.values
    consider_final["Consider3"]=consider.values
    consider_final["Consider4"]=consider.values
    consider_final["Consider5"]=consider.values
    consider_final["Consider6"]=consider.values
    consider_final["Consider7"]=consider.values
    consider_final["Consider8"]=consider.values
    consider_final["Consider9"]=consider.values
    consider_final["Consider10"]=consider.values
    consider_final["Consider11"]=consider.values
    consider_final["Consider12"]=consider.values
    consider_final["Consider13"]=consider.values
    consider_final["Consider14"]=consider.values
    consider_final["Consider15"]=consider.values

    ferro_alloy_name=df4["Ferro Alloys_Name"][0:25]

    #Read source file
    sourcedf=pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx",sheet_name="Inputs_Grade Classification",\
                           header=[2])
    sourcedf=sourcedf.dropna(how='all',axis=1)
    sourcedf=sourcedf.iloc[:, :-1]
    sourcedf=sourcedf.fillna("Unknown")
    grade=df['Grade'][0]

    for i in range(len(sourcedf['Grade'])):
        if sourcedf['Grade'][i]==grade:
            grade_df=pd.DataFrame(sourcedf.iloc[i,:]).T

    grade_df

    recovery=pd.read_excel("10Sep_B96599_Ferro Alloys Consumption Model - Angul.xlsx",sheet_name="Inputs_Ferro_Alloys_Angul",\
                           header=[37])
    #recovery=recovery['Grade'][0]
    recovery=recovery.dropna(how='all',axis=1)
    recovery.fillna("NA")

    #Recovery for C,S,P,Al,Cu
    c_recovery=recovery['%C'][0]
    s_recovery=recovery["%S"][0]
    p_recovery=recovery["%P"][0]
    al_recovery=recovery["%Al"][0]
    cu_recovery=recovery["%Cu"][0]
    ni_recovery=recovery["%Ni"][0]
    cr_recovery=recovery["%Cr"][0]
    mo_recovery=recovery["%Mo"][0]
    ti_recovery=recovery["%Ti"][0]
    v_recovery=recovery["%V"][0]
    nb_recovery=recovery["%Nb"][0]
    b_recovery=recovery["%B"][0]

    #Mn recovery
    mn_recovery_other=recovery["%Mn"][0]
    mn_recovery_femnhc=recovery["%Mn"][1]
    mn_recovery_mn=recovery["%Mn"][2]
    #Ca Recovery
    ca_recovery_other=recovery["%Ca"][0]
    ca_recovery_casi=recovery["%Ca"][1]
    ca_recovery_ca=recovery["%Ca"][2]

    #Si recovery vlookup
    if str(grade_df['Al Killed/ Si Killed'])=="Si Killed":
        si_recovery= recovery["%Si"][0]
    else:
        if (input_chemistry_final["IN_%Al"][0]>int(0.0005)) and (input_chemistry_final["IN_%C"][0]>int(0.001)):
            si_recovery=recovery["%Si"][5]
        else:
            if (input_chemistry_final["IN_%Al"][0]>int(0.0005)):
                si_recovery=recovery["%Si"][6]
            else:
                if (input_chemistry_final["IN_%C"][0]<int(0.0002)):
                    si_recovery=recovery["%Si"][1]
                else:
                    if (input_chemistry_final["IN_%C"][0]<int(0.0005)):
                        si_recovery=recovery["%Si"][2]
                    else:
                        if (input_chemistry_final["IN_%C"][0]<int(0.0007)):
                            si_recovery=recovery["%Si"][3]
                        else:
                            si_recovery=recovery["%Si"][4]

    dummydf=df.iloc[:,0:93]
    openingdf=pd.DataFrame(index=range(25),columns=range(15))
    collist=["Rec_%C","Rec_%Mn","Rec_%S","Rec_%P","Rec_%Si","Rec_%Al","Rec_%Cu","Rec_%Ca","Rec_%Ni","Rec_%Cr",\
             "Rec_%Mo","Rec_%Ti","Rec_%V","Rec_%Nb","Rec_%B"]
    openingdf.columns=collist

    for i in range(len(openingdf)):
        openingdf["Rec_%Si"][i]=si_recovery
        openingdf["Rec_%C"][i]=c_recovery
        openingdf["Rec_%P"][i]=p_recovery
        openingdf["Rec_%Al"][i]=al_recovery
        openingdf["Rec_%S"][i]=s_recovery
        openingdf["Rec_%Cu"][i]=cu_recovery
        openingdf["Rec_%Ni"][i]=ni_recovery
        openingdf["Rec_%Cr"][i]=cr_recovery
        openingdf["Rec_%Mo"][i]=mo_recovery
        openingdf["Rec_%Ti"][i]=ti_recovery
        openingdf["Rec_%V"][i]=v_recovery
        openingdf["Rec_%Nb"][i]=nb_recovery
        openingdf["Rec_%B"][i]=b_recovery
        openingdf["Rec_%Mn"]=mn_recovery_other
        openingdf["Rec_%Mn"][4]=mn_recovery_femnhc
        openingdf["Rec_%Mn"][5]=mn_recovery_mn
        openingdf["Rec_%Ca"]=ca_recovery_other
        openingdf["Rec_%Ca"][11]=ca_recovery_ca
        openingdf["Rec_%Ca"][21]=ca_recovery_casi
    #openingdf
    finaldf=dummydf.join(openingdf)

    recovery_final=openingdf

    final_temp=lowerbound_final.join(upperbound_final.join(input_chemistry_final.join(ferro_alloy.join(quantity.join(cost_fa)))))
    final_temp1=final_temp.join(recovery_final.join(consider_final))
    final_temp2=final_temp1.join(ferro_alloy_name)
    finaldf=final_temp2.join(opening_chemistry_final)

    finaldf["OP_%S"]=0
    finaldf["OP_%Si"]=0
    finaldf["OP_%Al"]=0
    finaldf["OP_%Cu"]=0
    finaldf["OP_%Ca"]=0
    finaldf["OP_%Ni"]=0
    finaldf["OP_%Cr"]=0
    finaldf["OP_%Mo"]=0
    finaldf["OP_%Ti"]=0
    finaldf["OP_%V"]=0
    finaldf["OP_%Nb"]=0
    finaldf["OP_%B"]=0

    #finaldf.to_excel("jrp.xlsx",index=False)

    st_left_lb = list()
    st_right_lb = list()
    num_elements = 15
    constr_lb_left =[''] * num_elements #where 3 is the number of elements
    constr_lb_right =[''] * num_elements #where 3 is the number of elements

    finaldf

    #Lower bound constraints#new iteration
    for j in range(num_elements):
        zerocoeff = [0]*len(finaldf)
        for i in range(len(finaldf)):
          #word = df.iloc[i, (j + num_elements * 3)]
          #print(str(word))
            #print("I is",i,"&& J is",j)
            #print("the consider is ",str(df.iloc[i, (j + ((num_elements*5)+2))]))
            if(finaldf.iloc[i, (j + num_elements*3)] == 0):  #to identify alloys with zero composition of the element
                      zerocoeff[i] = 1
            if(i != 0):
                constr_lb_left[j] =  constr_lb_left[j] + "+" + "("  + "x" + str(i+1) + "*" + str(finaldf.iloc[i, (j + num_elements*3)]) \
                                    +"*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+ "*"+str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+ ")" #ferro mix
                #constr_lb_right[j] = constr_lb_right[j] + "+" + "x" + str(i+1)
                if(zerocoeff[i] == 0):
                    #constr_lb_right[j] = constr_lb_right[j] + "+"+"x" + str(i+1)
                    #add consider inventory
                    constr_lb_right[j] = constr_lb_right[j] + "+"+"("+"x" + str(i+1)+"*"+\
                                        str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+")"
            else:
                constr_lb_left[j] = constr_lb_left[j]  + "(" + "x" + str(i + 1) + "*" + str(finaldf.iloc[i, (j + num_elements * 3)]) \
                                    + "*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+"*"+str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+ ")"  # ferro mix
                #constr_lb_right[j] = constr_lb_right[j] + "(" + "x" + str(i + 1)
                #include consider inventory
                constr_lb_right[j] = constr_lb_right[j] + "(" +"("+ "x" + str(i + 1)+"*"+\
                                        str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+")"

            if (i == (len(finaldf)-1)):
                constr_lb_left[j] = constr_lb_left[j] + "+" + "("  + str(finaldf.iloc[i, (j + num_elements * 6)+3]) + "*" \
                                    + str(finaldf.iloc[i, (num_elements * 4)]) + "*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+ ")"  # ferro mix
                # include the opening chemistry
                #constr_lb_left[j] = constr_lb_left[j]+"+"+"(" + str(df.iloc[i, (num_elements * 4)]) +"*"+ str(df.iloc[i, j+(num_elements * 6)+3])+")"
                constr_lb_right[j] = constr_lb_right[j] + "+" + str(finaldf.iloc[i, (num_elements * 4)]) + ")"
                # include the opening chemistry
                #constr_lb_right[j] = str(df.iloc[i, j]) +"*"+str(df.iloc[i, (j + ((num_elements*4)+2))])+ "*" + constr_lb_right[j]
                constr_lb_right[j] = str(finaldf.iloc[i, j]) +"*" + constr_lb_right[j]
                st_left_lb.append(constr_lb_left[j])
                st_right_lb.append(constr_lb_right[j])
                #constr_lb[j] = constr_lb[j] + str(df.iloc[i, (j + num_elements*2)]) + '*' + df.loc[i, "Qty"]
                #print(constr_lb_left[j])
                #print(constr_lb_right[j])
    #print(st_left_lb)
    #print(st_right_lb)

    #upper bound constraints
    constr_ub_left =[''] * num_elements #where 3 is the number of elements
    constr_ub_right =[''] * num_elements #where 3 is the number of elements
    st_left_ub = list()
    st_right_ub = list()
    zerocoeff = [0]*len(finaldf)
    zeroupper = [0]*num_elements
    for j in range(num_elements):

        for i in range(len(finaldf)):
            #word = finaldf.iloc[i, (j + num_elements * 3)]
            #print(str(word))
            if(finaldf.iloc[i, (j + num_elements*3)] == 0):  #to identify alloys with zero composition of the element
                  zerocoeff[i] = 1
            if(i != 0):
                constr_ub_left[j] =  constr_ub_left[j] + "+" + "("  + "x" + str(i+1) + "*" + str(finaldf.iloc[i, (j + num_elements*3)])\
                                    + "*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+"*"+str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+  ")" #ferro mix
                if(zerocoeff[i] == 0):
                    #print("")
                    #constr_ub_right[j] = constr_ub_right[j] + "+" + "x" + str(i+1)
                    constr_ub_right[j] = constr_ub_right[j] + "+"+"("+"x" + str(i+1)+"*"+\
                                        str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+")"

            else:
                constr_ub_left[j] = constr_ub_left[j]  + "(" + "x" + str(i + 1) + "*" + str(finaldf.iloc[i, (j + num_elements * 3)])\
                                    +"*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+ "*"+str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+  ")"  # ferro mix
                #constr_ub_right[j] = constr_ub_right[j] + "(" + "x" + str(i + 1)
                constr_ub_right[j] = constr_ub_right[j] + "(" +"("+ "x" + str(i + 1)+"*"+\
                                        str(finaldf.iloc[i, (j + ((num_elements*5)+2))])+")"

            if (i == (len(finaldf)-1)):
                constr_ub_left[j] = constr_ub_left[j] + "+" + "("  + str(finaldf.iloc[i, (j + num_elements * 6)+3]) + "*" \
                                    + str(finaldf.iloc[i, (num_elements * 4)]) + "*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+ ")"  # ferro mix
                #including opening parameters
                #constr_ub_left[j] = constr_ub_left[j]+"+"+"(" + str(finaldf.iloc[i, (num_elements * 4)]) +"*"+ str(finaldf.iloc[i, j+(num_elements * 6)+3])+")"
                #constr_ub_right[j] = constr_ub_right[j] +"+"+ str(finaldf.iloc[i, (num_elements * 4)]) +")"
                constr_ub_right[j] = constr_ub_right[j] +"+"+ str(finaldf.iloc[i, (num_elements * 4)]) +")"
                if(finaldf.iloc[i, num_elements + j] == 0):
                    zeroupper[j] = 1
                #constr_ub_right[j] = str(finaldf.iloc[i, num_elements + j]) +"*"+str(finaldf.iloc[i, (j + ((num_elements*4)+2))])+  "*" \
                                #+ constr_ub_right[j]
                constr_ub_right[j] = str(finaldf.iloc[i, num_elements + j]) + "*" \
                                    + constr_ub_right[j]
                #constr_ub_right[j] = str(finaldf.iloc[i, num_elements + j]) +  "*" + constr_ub_right[j]
                st_left_ub.append(constr_ub_left[j])
                st_right_ub.append(constr_ub_right[j])
                #constr_lb[j] = constr_lb[j] + str(finaldf.iloc[i, (j + num_elements*2)]) + '*' + finaldf.loc[i, "Qty"]
                #print(constr_ub_left[j])
                #print(constr_ub_right[j])
    #print(st_left_ub)
    #print(st_right_ub)
    #print(zeroupper)

    #Objective Function
    obj = ""
    for i in range(len(finaldf)):
        if(i == 0):
            obj = "x" + str(i+1) + "*" + str(finaldf.iloc[i, (num_elements * 4)+1])
        else:
            obj = obj + "+" + "x" + str(i+1) + "*" + str(finaldf.iloc[i, (num_elements * 4)+1])

    #print(obj)
    # import the library pulp as p
    import pulp as p

    # Create a LP Minimization problem
    Lp_prob = p.LpProblem('Problem', p.LpMinimize)
    var_names = ['x' + str(i+1) for i in range(len(finaldf))]
    x_cont = [p.LpVariable(i, lowBound=0, cat="Continuous") for i in var_names]
    #print(type(x_cont[1]))
    for i in range(len(finaldf)):
        #print('x'+ str(i+1) + " = " + "p.LpVariable(" + '"' + var_names[i] + '"' + "," +  "lowBound=0)")
        exec('x'+ str(i+1)  + " = " + "p.LpVariable(" + '"' + var_names[i] + '"' +  "," +  "lowBound=0)")

    # Create problem Variables
    # x1 = p.LpVariable("x1", lowBound=0)  # Create a variable x >= 0
    # x2 = p.LpVariable("x2", lowBound=0)  # Create a variable y >= 0

    # Objective Function
    Lp_prob += eval(obj)

    # Constraints:
    #Lp_prob += ((x1*0.02) + (x2*0.00018)+(0.0009*239)) <= 0.0019 * (x1+x2+239)  #these 2 lines are for C
    #Lp_prob += ((x1*0.02) + (x2*0.00018)+(0.0009*239))  >= 0.0017 * (x1+x2+239)
    #Lp_prob += ((x1*2) + (x2*0.18)+(0.09*239)) <= 0.19 * (x1+x2+239)  #these 2 lines are for C
    #Lp_prob += ((x1*2) + (x2*0.18)+(0.09*239))  >= 0.17 * (x1+x2+239)

    for i in range(num_elements):
        #print("Lp_prob += " + st_left_lb[i] + " >= " + st_right_lb[i])
        exec("Lp_prob += " + st_left_lb[i] + " >= " + st_right_lb[i])

    for i in range(num_elements):
        if(zeroupper[i] == 1):
            #print("Lp_prob += " + st_left_ub[i] + " == " + st_right_ub[i])
            exec("Lp_prob += " + st_left_ub[i] + " == " + st_right_ub[i])
        else:
            #print("Lp_prob += " + st_left_ub[i] + " <= " + st_right_ub[i])
            exec("Lp_prob += " + st_left_ub[i] + " <= " + st_right_ub[i])

    #Lp_prob += ((x1*60) + (x2*0)+(1.16*239)) <= 0.53 * (x1+x2+239)  #these 2 lines are for Mn
    #Lp_prob += ((x1*60) + (x2*0)+(1.16*239)) >= 0.48 * (x1+x2+239)

    #Lp_prob += ((x1*1) + (x2*1)) <= 1
    #Lp_prob += ((x1*-1) + (x2*1)) >= -3
    #Lp_prob += ((x1*1) + (x2*1)) >= -2
    #Lp_prob += ((x1*1) + (x2*1)) <= 2

    # Display the problem
    #print(Lp_prob)

    status = Lp_prob.solve()  # Solver
    #print(p.LpStatus[status])  # The solution status

    # Printing the final solution
    finaldfresult = pd.DataFrame(np.zeros([1, len(finaldf)]))

    # print(finaldfresult)

    for i in range(len(finaldf)):
        finaldfresult.iloc[0, i] = p.value(eval(var_names[i]))

    alloy_name=[]
    alloy_name=list(finaldf.iloc[:,92])
    finaldfresult.columns=alloy_name
    #print(finaldfresult)
    #print(Lp_prob.objective)
    #print(p.value(Lp_prob.objective))

    output=finaldfresult.T
    output.reset_index(inplace=True)
    output.columns=[["Ferro_alloy_Name","Quantity(Tons)"]]
    #ferro_dict = dict(zip(output.Ferro_alloy_Name, output.Quantity(Tons)))
    outputdict=output.to_dict()
    #print(output)
    #print(outputdict)
    print(Lp_prob.objective)

    print("The optimized cost is predicted as" ,"₹",round(p.value(Lp_prob.objective),2))
    return output
