🔗 Connections Explorer
A simple, fast, and interactive Streamlit app for exploring your exported LinkedIn Connections CSV.
Upload your file, filter it, search it, sort it, and export the results — all in one clean interface.

🚀 Features
📤 Upload Your LinkedIn Connections CSV
Just drag and drop your exported Connections.csv file from LinkedIn.

📊 Instant Data Preview
The app automatically cleans column names and displays your data in a responsive table.

🔍 Global Search
Search across all fields (name, company, position, etc.) using a single search box.

🎯 Smart Filters
Filter your connections by:

Company

Position

Connected On date

Filters update instantly and can be combined.

📁 Export Filtered Results
Download your filtered dataset as a new CSV — perfect for outreach lists, research, or CRM imports.

🛠️ How to Run the App
Install dependencies:

bash
pip install streamlit pandas
Save the script as app.py.

Run Streamlit:

bash
streamlit run app.py
Open the browser window that appears and upload your LinkedIn CSV.

📦 File Requirements
Your CSV should be the standard LinkedIn export containing fields like:

First Name

Last Name

Email Address

Company

Position

Connected On

The app automatically trims whitespace and handles typical LinkedIn formatting.

📝 Notes & LinkedIn Export Tips
LinkedIn’s data export process can be a bit messy, so here are important things to know:

1. Downloading your data
Go to:

Settings → Data Privacy → Get a copy of your data → Download your data

LinkedIn will send you a ZIP archive containing multiple CSV files, including:

Connections.csv

Messages.csv

Other profile/activity data

2. Important: Clean the top of the CSV before uploading
LinkedIn sometimes adds header text, disclaimers, or metadata above the actual column names in the CSV.

If your file looks like this:

Code
Some text about your data export...
More metadata...
First Name,Last Name,Email Address,Company,Position,Connected On
John,Doe,...
You must delete the lines above the real column headers, otherwise the app will error.

The first line of your CSV must be the actual column names.

3. Connections + Messages
If you’re working with both:

Connections.csv

Messages.csv

You’ll need to trim the top metadata from each file before loading them into any tool.

🧩 Code Overview
The app uses:

Streamlit for UI

Pandas for data handling

A simple search + filter pipeline

A download button for exporting results
