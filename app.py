# =========================================================
# STRATEGIC SALES INTELLIGENCE DASHBOARD
# PROFESSIONAL ENTERPRISE EDITION
# FULLY EDITABLE + ERROR FREE VERSION
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Strategic Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL CSS UI
# =========================================================

st.markdown("""
<style>

/* =====================================================
GLOBAL
===================================================== */

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
    scroll-behavior: smooth;
}

/* =====================================================
BACKGROUND
===================================================== */

.stApp {

    background:
        radial-gradient(circle at top left, #1e293b 0%, transparent 30%),
        radial-gradient(circle at bottom right, #0f172a 0%, transparent 25%),
        linear-gradient(135deg, #020617, #0f172a, #111827);

    color: white;
}

/* =====================================================
ANIMATIONS
===================================================== */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(40px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

@keyframes floating {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-8px);
    }

    100% {
        transform: translateY(0px);
    }
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

    background: rgba(15,23,42,0.92);

    border-right: 1px solid rgba(255,255,255,0.06);

    backdrop-filter: blur(20px);
}

/* =====================================================
HEADER
===================================================== */

.main-title {

    font-size: 3.8rem;

    font-weight: 800;

    text-align: center;

    color: white;

    animation: fadeUp 1s ease;
}

.main-subtitle {

    text-align: center;

    font-size: 1.2rem;

    color: #cbd5e1;

    animation: fadeUp 1.3s ease;
}

/* =====================================================
GLASS CONTAINER
===================================================== */

.glass-container {

    background: rgba(255,255,255,0.05);

    border-radius: 24px;

    padding: 25px;

    border: 1px solid rgba(255,255,255,0.06);

    backdrop-filter: blur(18px);

    animation: fadeUp 1s ease;

    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}

/* =====================================================
KPI CARDS
===================================================== */

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.06);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 25px;

    border-radius: 24px;

    backdrop-filter: blur(16px);

    transition: all 0.4s ease;

    animation: fadeUp 0.8s ease;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-10px) scale(1.02);

    border: 1px solid #3b82f6;
}

/* =====================================================
CHARTS
===================================================== */

.stPlotlyChart {

    background: rgba(255,255,255,0.05);

    border-radius: 24px;

    padding: 20px;

    border: 1px solid rgba(255,255,255,0.06);

    transition: all 0.4s ease;

    animation: fadeUp 1s ease;
}

.stPlotlyChart:hover {

    transform: scale(1.01);
}

/* =====================================================
TABLES
===================================================== */

[data-testid="stDataFrame"] {

    background: rgba(255,255,255,0.04);

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.06);

    padding: 12px;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton>button {

    background: linear-gradient(135deg, #2563eb, #7c3aed);

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px 28px;

    font-size: 15px;

    font-weight: 600;

    transition: all 0.35s ease;
}

.stButton>button:hover {

    transform: translateY(-4px);
}

/* =====================================================
INPUTS
===================================================== */

.stSelectbox div,
.stMultiSelect div,
.stDateInput div {

    border-radius: 14px !important;
}

/* =====================================================
SCROLLBAR
===================================================== */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#3b82f6, #8b5cf6);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOADING EFFECT
# =========================================================

with st.spinner("🚀 Launching Dashboard..."):
    time.sleep(1)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
    Strategic Sales Intelligence
</div>

<div class="main-subtitle">
    Enterprise Revenue Analytics • Smart Business Decisions
</div>
""", unsafe_allow_html=True)

# =========================================================
# CLOCK
# =========================================================

current_time = datetime.datetime.now().strftime("%d %B %Y | %I:%M %p")

st.markdown(f"""
<div style='text-align:right; color:#94a3b8;'>

🕒 {current_time}

</div>
""", unsafe_allow_html=True)

# =========================================================
# BUSINESS OVERVIEW
# =========================================================

st.markdown("""
<div class="glass-container">

<h2>🚀 Executive Business Overview</h2>

<p style="font-size:17px; color:#cbd5e1; line-height:1.8;">

Monitor sales performance, revenue growth,
regional analytics, and business profitability
using a modern enterprise analytics platform.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Dashboard Controls")

uploaded_file = st.sidebar.file_uploader(
    "📁 Upload CSV or Excel",
    type=["csv", "xlsx"]
)

# =========================================================
# SAMPLE DATA
# =========================================================

def generate_sample_data():

    dates = pd.date_range("2024-01-01", "2025-12-31", freq="D")

    products = [
        "Laptop Pro",
        "Wireless Mouse",
        "Monitor 27",
        "Keyboard RGB",
        "USB Dock"
    ]

    regions = ["North", "South", "East", "West"]

    np.random.seed(42)

    data = []

    for date in dates:

        for _ in range(5):

            product = np.random.choice(products)
            region = np.random.choice(regions)

            sales = np.random.uniform(100, 2500)

            cost = sales * np.random.uniform(0.4, 0.7)

            data.append([
                date,
                product,
                region,
                sales,
                cost,
                f"CUST{np.random.randint(1000,9999)}"
            ])

    df = pd.DataFrame(data, columns=[
        "date",
        "product",
        "region",
        "sales",
        "cost",
        "customer_id"
    ])

    df["profit"] = df["sales"] - df["cost"]

    return df

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data(file):

    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    df.columns = df.columns.str.lower()

    df["date"] = pd.to_datetime(df["date"])

    if "cost" not in df.columns:
        df["cost"] = df["sales"] * 0.6

    df["profit"] = df["sales"] - df["cost"]

    return df

if uploaded_file is None:

    st.info("📂 Using Sample Dataset")

    df = generate_sample_data()

else:

    df = load_data(uploaded_file)

# =========================================================
# FILTERS
# =========================================================

st.sidebar.header("🔍 Filters")

search = st.sidebar.text_input("🔍 Search Product")

products = st.sidebar.multiselect(
    "Select Products",
    df["product"].unique(),
    default=df["product"].unique()
)

regions = st.sidebar.multiselect(
    "Select Regions",
    df["region"].unique(),
    default=df["region"].unique()
)

mask = (
    (df["product"].isin(products)) &
    (df["region"].isin(regions))
)

filtered_df = df[mask]

if search:
    filtered_df = filtered_df[
        filtered_df["product"]
        .str.contains(search, case=False)
    ]

# =========================================================
# EDITABLE DATASET
# =========================================================

st.subheader("📝 Editable Sales Dataset")

filtered_df = st.data_editor(
    filtered_df,
    use_container_width=True,
    num_rows="dynamic"
)

# =========================================================
# KPI CALCULATIONS
# =========================================================

today = filtered_df["date"].max()

last_period = filtered_df[
    filtered_df["date"] >= (today - datetime.timedelta(days=30))
]["sales"].sum()

prev_period = filtered_df[
    (filtered_df["date"] < (today - datetime.timedelta(days=30))) &
    (filtered_df["date"] >= (today - datetime.timedelta(days=60)))
]["sales"].sum()

sales_growth = (
    ((last_period - prev_period) / prev_period) * 100
    if prev_period > 0 else 0
)

total_revenue = filtered_df["sales"].sum()

total_profit = filtered_df["profit"].sum()

margin = (
    (total_profit / total_revenue) * 100
    if total_revenue > 0 else 0
)

avg_daily_sales = (
    filtered_df.groupby("date")["sales"]
    .sum()
    .mean()
)

transactions = filtered_df.shape[0]

# =========================================================
# KPI SECTION
# =========================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.0f}",
        f"{sales_growth:.1f}%"
    )

with k2:
    st.metric(
        "📈 Gross Profit",
        f"${total_profit:,.0f}",
        f"Margin {margin:.1f}%"
    )

with k3:
    st.metric(
        "🛒 Transactions",
        f"{transactions:,}"
    )

with k4:
    st.metric(
        "📦 Avg Daily Sales",
        f"${avg_daily_sales:,.0f}"
    )

# =========================================================
# MODERN CHART STYLE
# =========================================================

def modern_chart(fig):

    fig.update_layout(

        paper_bgcolor='rgba(0,0,0,0)',

        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(
            color='white',
            size=14
        ),

        title_font=dict(
            size=24,
            color='white'
        ),

        margin=dict(l=20, r=20, t=60, b=20),

        legend=dict(
            bgcolor='rgba(0,0,0,0)'
        )
    )

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(
        gridcolor='rgba(255,255,255,0.08)'
    )

    return fig

# =========================================================
# MONTHLY REVENUE
# =========================================================

st.subheader("📈 Revenue Analytics & Growth Trends")

filtered_df["month"] = (
    filtered_df["date"]
    .dt.to_period("M")
    .astype(str)
)

monthly = filtered_df.groupby("month").agg({
    "sales": "sum"
}).reset_index()

monthly["growth"] = (
    monthly["sales"]
    .pct_change() * 100
)

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Bar(
        x=monthly["month"],
        y=monthly["sales"],
        name="Revenue",
        marker_color="#3b82f6"
    ),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(
        x=monthly["month"],
        y=monthly["growth"],
        name="Growth %",
        line=dict(
            color="#8b5cf6",
            width=4
        )
    ),
    secondary_y=True
)

fig.update_layout(
    title="Monthly Revenue vs Growth Rate"
)

fig = modern_chart(fig)

st.plotly_chart(fig, use_container_width=True)

# =========================================================
# CHART ROW
# =========================================================

c1, c2 = st.columns(2)

# =========================================================
# PRODUCT PERFORMANCE
# =========================================================

with c1:

    st.subheader("🏆 Product Performance")

    product_sales = filtered_df.groupby(
        "product"
    )["sales"].sum().reset_index()

    fig2 = px.pie(
        product_sales,
        names="product",
        values="sales",
        hole=0.55
    )

    fig2.update_traces(
        textinfo="percent+label"
    )

    fig2 = modern_chart(fig2)

    st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# REGIONAL REVENUE
# =========================================================

with c2:

    st.subheader("🌍 Regional Revenue")

    region_sales = filtered_df.groupby(
        "region"
    )["sales"].sum().reset_index()

    fig3 = px.bar(
        region_sales,
        x="region",
        y="sales",
        color="sales",
        text_auto=".2s"
    )

    fig3.update_layout(
        title="Region Wise Revenue"
    )

    fig3 = modern_chart(fig3)

    st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# EDITABLE TOP PRODUCTS
# =========================================================

st.subheader("🔥 Editable Top Selling Products")

top_products = product_sales.sort_values(
    by="sales",
    ascending=False
).head(5)

edited_top_products = st.data_editor(
    top_products,
    use_container_width=True,
    num_rows="dynamic"
)

# =========================================================
# WHAT IF ANALYSIS
# =========================================================

st.subheader("🔮 Business Strategy Simulator")

price_change = st.slider(
    "Increase Product Price (%)",
    -20,
    30,
    5
)

elasticity = st.selectbox(
    "Demand Elasticity",
    [0.5, 1.0, 1.5]
)

current_rev = filtered_df["sales"].sum()

demand_change = (
    1 - (abs(price_change)/100) * elasticity
    if price_change > 0
    else 1 + (abs(price_change)/100) * elasticity
)

projected_rev = (
    current_rev *
    (1 + price_change/100) *
    demand_change
)

a, b = st.columns(2)

with a:
    st.metric(
        "Current Revenue",
        f"${current_rev:,.0f}"
    )

with b:
    st.metric(
        "Projected Revenue",
        f"${projected_rev:,.0f}",
        f"{((projected_rev-current_rev)/current_rev)*100:.1f}%"
    )

# =========================================================
# INSIGHT CARD
# =========================================================

st.markdown(f"""
<div class="glass-container">

<h2>📊 Executive Strategic Insight</h2>

<p style="font-size:18px; line-height:1.9; color:#e2e8f0;">

High-performing products and fast-growing regions
are generating the majority of company revenue.

Focusing marketing campaigns, inventory planning,
and customer retention strategies on these areas
can significantly improve future profitability.

</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# DOWNLOAD REPORT
# =========================================================

st.sidebar.header("📎 Export Report")

summary = f"""
==================================================
STRATEGIC BUSINESS REPORT
==================================================

Total Revenue: ${total_revenue:,.0f}

Gross Profit: ${total_profit:,.0f}

Profit Margin: {margin:.1f}%

Total Transactions: {transactions:,}

Average Daily Sales: ${avg_daily_sales:,.0f}

Projected Revenue: ${projected_rev:,.0f}

==================================================
"""

st.sidebar.download_button(
    "⬇ Download Executive Report",
    summary,
    file_name="executive_business_report.txt"
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<hr style="border:1px solid rgba(255,255,255,0.08);">

<div style='text-align:center; color:#94a3b8; padding:10px;'>

⚡ Enterprise Business Intelligence Platform

</div>
""", unsafe_allow_html=True)
