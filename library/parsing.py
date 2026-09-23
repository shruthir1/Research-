import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def parse_csv(file_path, output_path):
    curr = pd.read_csv(file_path)
    curr = curr.drop( columns=["color", "promoter","promoterDNA","ribozyme","ribozymeDNA","rbs","rbsDNA","cds","cdsDNA","terminator","terminatorDNA", ])
    curr.to_csv(output_path, index_label=False)

# def plot_gate_equation(parsed_csv):
#     curr = pd.read_csv(parsed_csv)
#     gates_amount = len(curr)

#     #to know how many boxes of graphs per row visually 
#     boxes_per_row = int(np.ceil(np.sqrt(gates_amount)))
#     rows_needed = int(np.ceil(gates_amount / boxes_per_row))
#     #play around with fig size to make it look better
#     fig, all_ax = plt.subplots(nrows=rows_needed, ncols=boxes_per_row,figsize=(6 * boxes_per_row, 5 * rows_needed),)
    

#reading first library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco1C1G1T1.csv', 'parsed_Eco1C1G1T1.csv')


#reading second library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco1C1G1T1b.csv', 'parsed_Eco1C1G1T1b.csv')

#reading third library file 
curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco2C2G2T2.csv')
curr = curr.drop( columns=["promoter", "promoterDNA","sgRNA","sgRNADNA","terminator","terminatorDNA", ])
curr.to_csv('parsed_Eco2C2G2T2.csv', index_label=False)

#reading fourth library file - not sure what is going on here yet
#curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco3C3G3T3.csv')

#reading fifth library file - i think its fine as is? dont know if it needs to be stripped of cols
curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco3C3G3T3.csv')
curr.to_csv('parsed_Eco3C3G3T3.csv', index_label=False)

#reading sixth library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1_v1.csv', 'parsed_EcoCB1_v1.csv')

#reading seventh library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1_v2.csv', 'parsed_EcoCB1_v2.csv')

#reading eighth library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1.csv', 'parsed_EcoCB1.csv')

#reading ninth library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib_110215.csv', 'parsed_EcoJS4ib_110215.csv')

#reading tenth library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib_111015.csv', 'parsed_EcoJS4ib_111015.csv')

#reading eleventh library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib.csv', 'parsed_EcoJS4ib.csv')

#reading twelfth library file - not sure what is going on here yet either 
#curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/parts_LacI_TetR.csv')