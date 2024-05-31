
import json

with open('states.json') as file:
  data = json.load(file)
    
for state in data['states']:  
 #  print(state)   # for showing the data present in json file

    del state['area_codes']
    
with open('new_states.json', 'w') as f:  # making some changes in original file and that new data is stored in another file then display it.
    datnew = json.dump(data, f, indent=2)
    print(datnew)
    
