import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import data -- change path
corona_dataset_csv = pd.read_csv("/content/drive/My Drive/UST/time_series_covid19_confirmed_US.csv")
corona_dataset_csv.head()

#remove useless columns -- change columns
df = corona_dataset_csv.drop(["UID", "iso2", "iso3", "code3", "FIPS", "Admin2", "Lat", "Long_"],axis=1)

#group dataset with column name
corona_dataset_aggregated = df.groupby("Combined_Key").sum()

#example visualization - makes line plot with both cities as line
corona_dataset_aggregated.loc["San Francisco, California, US"].plot()
corona_dataset_aggregated.loc["San Diego, California, US"].plot()
plt.legend()


corona_dataset_aggregated.loc["San Francisco, California, US"].plot()
#plots first derivative
corona_dataset_aggregated.loc["San Francisco, California, US"].diff().plot()

#first derivative of all cities i.e. Max infection rate of all cities
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries :
  max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"] = max_infection_rate

#changing data frame to corona_data
corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])

#Maximum infection rate oa all the cities in US
corona_data.head()

#example imports death dataset and does the same

#join max infection and death rate data
cases = corona_data.join(corona_death,how="inner")
cases.head()

#Correlation Matrix b/w max infection rate and max death rate
cases.corr()

#Plot max infection rate vs. max death rate
x = cases["max_infection_rate"]
y = cases["max_death_rate"]
sns.scatterplot(x,y)

#hidden markov portion!!!
ir=np.array(cases['max_infection_rate'])
dr=np.array(cases['max_death_rate'])
features=np.column_stack((ir,dr))

from hmmlearn.hmm import GaussianHMM
score_list=[]
hmm=GaussianHMM(n_components=3)
hmm.fit(features)

from sklearn.model_selection import train_test_split
train,test = train_test_split(cases, test_size=0.33, shuffle=False)
ir_train=np.array(train['max_infection_rate'])
dr_train=np.array(train['max_death_rate'])
train_features=np.column_stack((ir_train,dr_train))

ir_test=np.array(test['max_infection_rate'])
dr_test=np.array(test['max_death_rate'])
test_features=np.column_stack((ir_test,dr_test))

from hmmlearn.hmm import GaussianHMM
hm=GaussianHMM(n_components=4)
hm.fit(train_features)

#i believe they do 50 days, 100, and 200 days, I think we can do shorter intervals
n_latency_days=5
day_index=50
previous_data_start_index = max(0, day_index - n_latency_days)
previous_data_end_index = max(0, day_index - 1)
previous_data = test.iloc[previous_data_start_index:previous_data_end_index]

ir_prv=np.array(previous_data['max_infection_rate'])
dr_prv=np.array(previous_data['max_death_rate'])
prv50_features=np.column_stack((ir_prv,dr_prv))

day_index=100
previous_data_start_index = max(0, day_index - n_latency_days)
previous_data_end_index = max(0, day_index - 1)
previous_data = test.iloc[previous_data_start_index:previous_data_end_index]

ir_prv=np.array(previous_data['max_infection_rate'])
dr_prv=np.array(previous_data['max_death_rate'])
prv100_features=np.column_stack((ir_prv,dr_prv))

day_index=200
previous_data_start_index = max(0, day_index - n_latency_days)
previous_data_end_index = max(0, day_index - 1)
previous_data = test.iloc[previous_data_start_index:previous_data_end_index]

ir_prv=np.array(previous_data['max_infection_rate'])
dr_prv=np.array(previous_data['max_death_rate'])
prv200_features=np.column_stack((ir_prv,dr_prv))

outcome_score_50f=hm.score(prv50_features)
prediction_50f=hm.predict_proba(prv50_features)

outcome_score_100f=hm.score(prv100_features)
prediction_100f=hm.predict_proba(prv100_features)

outcome_score_200f=hm.score(prv200_features)
prediction_200f=hm.predict_proba(prv200_features)

print(outcome_score_50f,outcome_score_100f,outcome_score_200f)

data = {'First 50 Days':  [outcome_score_50f],
        'First 100 Days': [outcome_score_100f],
         'First 200 Days': [outcome_score_200f]
        }
df_final = pd.DataFrame (data, columns = ['First 50 Days','First 100 Days', 'First 200 Days'])

df_final
