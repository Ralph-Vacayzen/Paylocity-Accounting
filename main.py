import streamlit as st
import pandas as pd

st.set_page_config('Paylocity Accounting', '📄')

st.caption('VACAYZEN')
st.title('Paylocity Accounting')
st.info('Remove unnecessary data from a paylocity export.')

file = st.file_uploader('Payroll Register Data Export', 'CSV')

if file is not None:
    columns = [
        'Co',
        'Location',
        'Employee',
        'ID',
        'Process',
        'Check Date',
        'Net',
        'E-REGHours',
        'E-REGAmount',
        'E-OTHours',
        'E-OTAmount',
        'E-PTOHours',
        'E-PTOAmount',
        'E-SICKMAmount',
        'E-SICKHours',
        'E-SICKAmount',
        'E-COMMHours',
        'E-COMMAmount',
        'E-HOLHours',
        'E-HOLAmount',
        'E-BRVMTHours',
        'E-BRVMTAmount',
        'E-REIMHours',
        'E-REIMAmount',
        'E-RETROHours',
        'E-RETROAmount'
    ]

    df = pd.read_csv(file, index_col=False)

    contained_columns = []

    for column in columns:
        if column in df.columns:
            contained_columns.append(column)

    df = df[contained_columns]

    st.download_button('DOWNLOAD', df.to_csv(index=False), 'Paylocity_Export.csv', 'CSV', use_container_width=True, type='primary')