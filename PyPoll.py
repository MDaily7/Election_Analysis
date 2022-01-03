#Assign a variable for the file to load and a path
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: perform analysis
    print(election_data)
#Create a filename variable to a direct path to the file
file_to_save = 'Analysis/election_analysis.txt'
#Using a with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #Write some data to the file.
    txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")

