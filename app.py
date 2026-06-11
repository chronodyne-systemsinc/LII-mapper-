import streamlit as st
import pandas as pd

st.set_page_config(page_title="Connections Explorer", layout="wide")

st.title("🔗 Connections Explorer")
st.write("Upload your CSV of LinkedIn connections and explore, filter, and sort them easily.")

# Upload
uploaded = st.file_uploader("Upload Connections CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)

    # Clean column names
    df.columns = [c.strip() for c in df.columns]

    st.subheader("📊 Data Preview")
    st.dataframe(df, use_container_width=True)

    st.subheader("🔍 Search & Filter")

    # Search box
    search = st.text_input("Search by name, company, or position")

    filtered = df.copy()

    if search:
        search_lower = search.lower()
        filtered = filtered[
            df.apply(lambda row: search_lower in str(row).lower(), axis=1)
        ]

    # Column filters
    col1, col2, col3 = st.columns(3)

    with col1:
        company = st.selectbox("Filter by Company", ["All"] + sorted(df["Company"].dropna().unique().tolist()))
        if company != "All":
            filtered = filtered[filtered["Company"] == company]

    with col2:
        position = st.selectbox("Filter by Position", ["All"] + sorted(df["Position"].dropna().unique().tolist()))
        if position != "All":
            filtered = filtered[filtered["Position"] == position]

    with col3:
        date = st.selectbox("Filter by Connected On", ["All"] + sorted(df["Connected On"].dropna().unique().tolist()))
        if date != "All":
            filtered = filtered[filtered["Connected On"] == date]

    st.subheader("📁 Filtered Results")
    st.write(f"Showing {len(filtered)} connections")
    st.dataframe(filtered, use_container_width=True)

    # Download filtered results
    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download Filtered CSV", csv, "filtered_connections.csv", "text/csv")
