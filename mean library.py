import pandas as pd

data = { 
    
    'age' : [25,45,44,23,12,35,68,64],
    'name' : ['Manuel','Shane','Drew','Bill', 'Dean','John','Megan','Sarah'],
        
        }

df = pd.DataFrame(data)

Avg_age = df['age'].mean()

print(f"The average age is {Avg_age}")