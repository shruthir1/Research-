import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def parse_csv(file_path, output_path):
    curr = pd.read_csv(file_path)
    curr = curr.drop( columns=["color", "promoter","promoterDNA","ribozyme","ribozymeDNA","rbs","rbsDNA","cds","cdsDNA","terminator","terminatorDNA", ])
    curr.to_csv(output_path, index_label=False)

def plot_gate_equation(parsed_csv):
    # f = pd.read_csv(parsed_csv)
    # rows = len(f) #how many gates needs to be plotted 

    # figure, axes = plt.subplots(rows, 1, figsize=(2, 5*rows))
    import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def parse_csv(file_path, output_path):
    curr = pd.read_csv(file_path)
    curr = curr.drop(columns=["color", "promoter","promoterDNA","ribozyme","ribozymeDNA","rbs","rbsDNA","cds","cdsDNA","terminator","terminatorDNA"], errors='ignore')
    curr.to_csv(output_path, index=False) # index=False prevents writing an unnamed column

# def plot_gate_equation(parsed_csv):
#     df = pd.read_csv(parsed_csv)
#     gates_amount = len(df)
    
#     if gates_amount == 0:
#         print(f"Skipping {parsed_csv}: File has no data.")
#         return

#     # Calculate an optimal square-ish grid instead of an ultra-tall column
#     boxes_per_row = int(np.ceil(np.sqrt(gates_amount)))
#     rows_needed = int(np.ceil(gates_amount / boxes_per_row))

#     # Handle edge case where there is only 1 gate in a file
#     if gates_amount == 1:
#         fig, ax = plt.subplots(figsize=(5, 4))
#         all_ax = [ax]
#     else:
#         fig, all_ax = plt.subplots(
#             nrows=rows_needed,
#             ncols=boxes_per_row,
#             figsize=(4 * boxes_per_row, 3.5 * rows_needed)
#         )
#         all_ax = np.array(all_ax).reshape(-1) # Flatten grid layout into a 1D array

#     # Generate log-spaced input values (common for biological response ranges)
#     x = np.logspace(-3, 2, 400)

#     # Loop through each row (gate) in the parsed dataframe
#     for i, (_, row) in enumerate(df.iterrows()):
#         ax = all_ax[i]
        
#         name = row["name"]
#         ymin = row["ymin"]
#         ymax = row["ymax"]
#         K = row["K"]
#         n = row["n"]

#         # Calculate the Hill equation y = ymin + (ymax - ymin) / (1.0 + (x / K)^n)
#         y = ymin + (ymax - ymin) / (1.0 + (x / K) ** n)

#         # Plot details
#         ax.plot(x, y, color="darkcyan", lw=2, label=name)
#         ax.set_xscale("log")
#         ax.set_yscale("log")
#         ax.set_title(name, fontsize=10, fontweight="bold")
#         ax.set_xlabel("Input", fontsize=8)
#         ax.set_ylabel("Output", fontsize=8)
#         ax.grid(True, which="both", linestyle=":", alpha=0.5)

#     # Hide extra blank axes bounding boxes if the grid is incomplete
#     for j in range(gates_amount, len(all_ax)):
#         all_ax[j].set_axis_off()

#     plt.suptitle(f"Gate Transfer Functions: {parsed_csv}", fontsize=12, fontweight="bold", y=1.02)
#     plt.tight_layout()
#     plt.show()


parsed_csv_files = []
#reading first library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco1C1G1T1.csv', 'parsed_Eco1C1G1T1.csv')


#reading second library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco1C1G1T1b.csv', 'parsed_Eco1C1G1T1b.csv')

#reading third library file 
curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco2C2G2T2.csv')
curr = curr.drop( columns=["promoter", "promoterDNA","sgRNA","sgRNADNA","terminator","terminatorDNA", ])
curr.to_csv('parsed_Eco2C2G2T2.csv', index_label=False)
# parsed_csv_files.append('parsed_Eco2C2G2T2.csv') the plots are NOT gates? but format is diff

#reading fourth library file - not sure what is going on here yet
#curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco3C3G3T3.csv')

#reading fifth library file - i think its fine as is? dont know if it needs to be stripped of cols
curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco3C3G3T3.csv')
curr.to_csv('parsed_Eco3C3G3T3.csv', index_label=False)
# parsed_csv_files.append('parsed_Eco3C3G3T3.csv')

#reading sixth library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1_v1.csv', 'parsed_EcoCB1_v1.csv')
parsed_csv_files.append('parsed_EcoCB1_v1.csv')

#reading seventh library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1_v2.csv', 'parsed_EcoCB1_v2.csv')
parsed_csv_files.append('parsed_EcoCB1_v2.csv')

#reading eighth library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1.csv', 'parsed_EcoCB1.csv')
parsed_csv_files.append('parsed_EcoCB1.csv')

#reading ninth library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib_110215.csv', 'parsed_EcoJS4ib_110215.csv')
parsed_csv_files.append('parsed_EcoJS4ib_110215.csv')

#reading tenth library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib_111015.csv', 'parsed_EcoJS4ib_111015.csv')
parsed_csv_files.append('parsed_EcoJS4ib_111015.csv')
#reading eleventh library file

parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib.csv', 'parsed_EcoJS4ib.csv')
parsed_csv_files.append('parsed_EcoJS4ib.csv')

#reading twelfth library file - not sure what is going on here yet either 
#curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/parts_LacI_TetR.csv')

#plotting csv files 

# for file in parsed_csv_files:
#     plot_gate_equation(file)