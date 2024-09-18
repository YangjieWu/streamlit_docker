import streamlit as st
import pandas as pd
import plotly.express as px

# env
# C:\Users\wuyan\OneDrive\Desktop\repository
# .venv\Scripts\activate

# Sample data
data = {
    'CustomerID': range(1, 101),
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70] * 10,
    'Income': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000] * 10,
    'SpendingScore': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120] * 10
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Customer Profile Dashboard")

# Sidebar filters
age_filter = st.sidebar.slider("Select Age Range", 0, 100, (25, 70))
income_filter = st.sidebar.slider("Select Income Range", 20000, 130000, (30000, 120000))

# Filter data based on user input
filtered_df = df[(df['Age'].between(age_filter[0], age_filter[1])) & 
                 (df['Income'].between(income_filter[0], income_filter[1]))]

# Plotting
fig = px.scatter(filtered_df, x='Income', y='SpendingScore', 
                 color='Age', 
                 hover_data=['CustomerID'], 
                 title="Customer Profile: Income vs Spending Score",
                 labels={'Income': 'Annual Income', 'SpendingScore': 'Spending Score'})

st.plotly_chart(fig)

# Show the filtered data
st.subheader("Filtered Customer Data")
st.write(filtered_df)
