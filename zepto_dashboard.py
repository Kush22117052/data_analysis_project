import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Zepto Product Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("zepto_v2.csv")
    df['revenue'] = df['discountedSellingPrice'] * df['availableQuantity']
    df['price_per_gram'] = df['discountedSellingPrice'] / df['weightInGms']
    df['weight_category'] = df['weightInGms'].apply(lambda x: 'Low' if x < 1000 else ('Medium' if x < 5000 else 'Bulk'))
    return df

df = load_data()

st.title("📊 Zepto Product Dashboard")

# Layout
tab1, tab2, tab3 = st.tabs(["Overview", "Revenue & Discounts", "Weight Analysis"])

# ---------------- OVERVIEW TAB ----------------
with tab1:
    st.header("🛒 Stock Overview")
    
    # Inventory Pie
    stock_count = df['outOfStock'].value_counts().reset_index()
    stock_count.columns = ['outOfStock', 'Count']
    fig_stock = px.pie(stock_count, names='outOfStock', values='Count', title='Stock Availability')
    st.plotly_chart(fig_stock, use_container_width=True)

    # Categories
    st.subheader("📦 Number of Products per Category")
    category_count = df['category'].value_counts().reset_index()
    category_count.columns = ['category', 'count']
    fig_cat = px.bar(category_count, x='category', y='count', title='Product Count by Category', color='category')
    st.plotly_chart(fig_cat, use_container_width=True)

# ---------------- REVENUE TAB ----------------
with tab2:
    st.header("💰 Revenue and Discount Insights")

    # Revenue per category
    revenue_df = df.groupby('category')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
    fig_revenue = px.bar(revenue_df, x='category', y='revenue', title='Estimated Revenue by Category', color='revenue')
    st.plotly_chart(fig_revenue, use_container_width=True)

    # Top 10 discounted products
    st.subheader("🔥 Top 10 Discounted Products")
    top_discount = df[['name', 'mrp', 'discountPercent']].drop_duplicates('name').sort_values(by='discountPercent', ascending=False).head(10)
    fig_discount = px.bar(top_discount, x='name', y='discountPercent', title='Top 10 Discounted Products')
    st.plotly_chart(fig_discount, use_container_width=True)

    # Highest average discount by category
    st.subheader("🏷️ Categories with Highest Average Discount")
    avg_discount = df.groupby('category')['discountPercent'].mean().reset_index()
    avg_discount = avg_discount.sort_values(by='discountPercent', ascending=False).head(5)
    fig_avg_discount = px.bar(avg_discount, x='category', y='discountPercent', title='Top 5 Categories by Avg Discount')
    st.plotly_chart(fig_avg_discount, use_container_width=True)

# ---------------- WEIGHT ANALYSIS TAB ----------------
with tab3:
    st.header("⚖️ Weight & Price Analysis")

    # Price per gram
    price_df = df[df['weightInGms'] >= 100].dropna(subset=['price_per_gram'])
    fig_ppg = px.histogram(price_df, x='price_per_gram', nbins=50, title='Price per Gram Distribution')
    st.plotly_chart(fig_ppg, use_container_width=True)

    # Weight Category distribution
    weight_cat = df['weight_category'].value_counts().reset_index()
    weight_cat.columns = ['Weight Category', 'Count']
    fig_weight = px.pie(weight_cat, names='Weight Category', values='Count', title='Product Weight Categories')
    st.plotly_chart(fig_weight, use_container_width=True)

    # Total weight by category
    df['total_weight'] = df['weightInGms'] * df['availableQuantity']
    total_weight = df.groupby('category')['total_weight'].sum().reset_index().sort_values(by='total_weight', ascending=False)
    fig_tweight = px.bar(total_weight, x='category', y='total_weight', title='Total Inventory Weight per Category')
    st.plotly_chart(fig_tweight, use_container_width=True)

