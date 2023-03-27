import os

# Get a dictionary of all environmental variables
env_vars = os.environ

# Loop through the dictionary and print each variable name and value
for var_name, var_value in env_vars.items():
    print(var_name + "=" + var_value)
