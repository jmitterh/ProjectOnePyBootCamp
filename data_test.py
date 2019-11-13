import pandas as pd
data = pd.io.stata.read_stata('.\Resources\wdr2013_occupational_wages_0\OWWupdate1983_2008.dta')
data.to_csv('occ_wages_2003_2008.csv')