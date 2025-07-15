import pandas as pd
# import openpyxl

# # From a list
    # s1 = pd.Series([1, 3, 5, 7, 9])
    # print(s1)

# # With custom index
    # s2 = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
    # print(s2)

# # From a dictionary
    # data = {'apple': 3, 'banana': 5, 'cherry': 7}
    # s3 = pd.Series(data)
    # print(s3)


# # Basic operations
    # print(s2 * 2) 
    # print(s2 + s2) 

# # Boolean indexing
    # print(s2[s2 > 25])

# # Accessing elements
    # print(s2['b'])  
    # print(s2[1])  


# Pandas DataFrame
# A DataFrame is a 2-dimensional labeled data structure with columns that can be of different types.

# # # Creating a DataFrame
# # # From a dictionary of lists
    # data = {
    #     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    #     'Age': [25, 30, 35, 40],
    #     'City': ['NY', 'LA', 'Chicago', 'Houston']
    # }
    # df = pd.DataFrame(data)
    # print(df)

# # With custom index
    # df_indexed = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
    # print(df_indexed)

# # From a list of dictionaries
    # data_list = [
    #     {'Name': 'Alice', 'Age': 25, 'City': 'NY'},
    #     {'Name': 'Bob', 'Age': 30, 'City': 'LA'},
    #     {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
    # ]
    # df_from_list = pd.DataFrame(data_list)
    # print(df_from_list)

# # Viewing data
    # print(df.head(2))  # First 2 rows
    # print(df.tail(1))   # Last row
    # print(df.shape)     # Dimensions (rows, columns)
    # print(df.columns)   # Column names
    # print(df.dtypes)    # Data types of columns

# # Accessing columns
    # print(df['Name'])   # As Series
    # print(df[['Name', 'Age']])  # Multiple columns as DataFrame

# # Adding new column
    # df['Salary'] = [70000, 80000, 90000, 100000]
    # print(df)

# #  Indexing and Filtering
# # Basic Indexing

# # loc - label-based indexing
    # print(df.loc[0])           # First row
    # print(df.loc[0:2, 'Name']) # Rows 0-2, 'Name' column

# # Read Excel
# pip install openpyxl
    # excel_data = pd.read_excel("D:\\Courses\\Qtree\\Current\\May25 - Python\\Libraries\\data.xlsx", sheet_name='Sheet1')
    # print(excel_data.head())

# #create and write a file
# # Write to CSV
    # df.to_csv('output.csv', index=False)

# # Write to Excel
    # df.to_excel('output.xlsx', sheet_name='Employees', index=False)

# # With options
    # df.to_csv('output_advanced.csv', 
    #           index=True, 
    #           columns=['Name', 'Salary'],  # Only these columns
    #           encoding='utf-8')

# # # Create a sample DataFrame
    # data = {
    #     'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    #     'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories'],
    #     'Price': [1200, 800, 400, 300, 50],
    #     'Quantity': [15, 30, 25, 10, 50],
    #     'Date': pd.date_range('20230101', periods=5)
    # }
    # sales = pd.DataFrame(data)
    # sales['Revenue'] = sales['Price'] * sales['Quantity']

    # # Basic analysis
    # print("Summary Statistics:")
    # print(sales.describe())

    # print("\nCategory-wise Summary:")
    # print(sales.groupby('Category').agg({'Price': 'mean', 'Quantity': 'sum', 'Revenue': 'sum'}))

# # Filtering
    # high_value = sales[sales['Price'] > 500]
    # print("\nHigh Value Products:")
    # print(high_value)

# # Sorting
    # print("\nTop 3 Products by Revenue:")
    # print(sales.sort_values('Revenue', ascending=False).head(3))

# # Pivot table
    # print("\nPivot Table (Category vs Price):")
    # print(pd.pivot_table(sales, values='Price', index='Category', aggfunc=['mean', 'count']))

# # Save analysis results
    # sales.to_excel('sales_analysis.xlsx', sheet_name='Sales Data', index=False)