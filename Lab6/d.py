# Import the necessary modules
import glob

# Specify the path of the email files
path = "/path/to/email/files/*.txt"

# Open the output file in write mode
with open("merged_emails.txt", "w") as outfile:
    
    # Loop through each email file
    for file in glob.glob(path):
        
        # Open the email file in read mode
        with open(file, "r") as infile:
            
            # Read the contents of the email file
            contents = infile.read()
            
            # Write the contents to the output file
            outfile.write(contents)
            
            # Add a separator between the email messages
            outfile.write("\n" + "="*50 + "\n")
