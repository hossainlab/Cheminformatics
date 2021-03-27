import pandas as pd 
from chembl_webresource_client.new_client import new_client

# Target search 
target = new_client.target
target_query = target.search('coronavirus') 
targets = pd.DataFrame.from_dict(target_query) 

# Select relative bioactivity data for SARS coronavirus 
selected_target = targets.target_chembl_id[4] 

# activity 
activity = new_client.activity 
result = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
df = pd.DataFrame.from_dict(result) 

