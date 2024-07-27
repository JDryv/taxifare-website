import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
"""
## Enter your request:
"""
columns = st.columns(7)

d = columns[0].date_input(
    "Pickup date",
    datetime.date(2019, 7, 6))
columns[0].write(d)

t = columns[1].time_input('Pickup time', datetime.time(8, 45))
columns[1].write(t)

pickup_longitude = columns[2].number_input('pickup longitude')
columns[2].write(pickup_longitude)

pickup_latitude = columns[3].number_input('pickup latitude')
columns[3].write(pickup_latitude)

passenger_count = int(columns[6].number_input('passenger count'))
columns[6].write(passenger_count)

dropoff_longitude = columns[4].number_input('dropoff longitude')
columns[4].write(dropoff_longitude)

dropoff_latitude = columns[5].number_input('dropoff latitude')
columns[5].write(dropoff_latitude)



## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('You are using the API provided by Le Wagon')


#2. Let's build a dictionary containing the parameters for our API...

dict   = {"pickup_datetime"   : datetime.datetime.combine(d, t),
          "pickup_longitude"  : pickup_longitude,
          "pickup_latitude"   : pickup_latitude,
          "dropoff_longitude" : dropoff_longitude,
          "dropoff_latitude"  : dropoff_latitude,
          "passenger_count"   : passenger_count
}
#3. Let's call our API using the `requests` package...

response = requests.get(url, params=dict)


# 4. Let's retrieve the prediction from the **JSON** returned by the API...
data = response.json()



'''
## Finally, we can display the prediction to the user
'''

st.markdown(f'## predicted fare : {round(data["fare"],2)}')
