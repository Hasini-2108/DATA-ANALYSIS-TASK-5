# Task 5: Data Analysis on CSV Files Using Jupyter Notebook

## Objective
Analyze sales data from a CSV file using Python in Jupyter Notebook. The notebook performs data exploration, aggregation, visualization, filtering, and generates business insights using Pandas and Matplotlib.

## Requirements

Install the required libraries before running the notebook:

```bash
pip install pandas matplotlib notebook
```

## Dataset

Place the `sales.csv` file in the same directory as your Jupyter Notebook.

Example dataset structure:

| Product | Region | Sales |
|----------|---------|--------|
| Laptop | North | 1500 |
| Mobile | South | 900 |
| Tablet | East | 1200 |

## Steps Performed in the Notebook

### 1. Import Libraries
- Pandas for data analysis
- Matplotlib for data visualization

### 2. Load CSV File
- Read the sales data using `pd.read_csv()`

### 3. Explore the Dataset
- Display first 5 rows
- Check dataset shape
- View column names
- Generate summary statistics
- Identify missing values

### 4. Grouping and Aggregation
- Calculate total sales by product
- Calculate total sales by region

### 5. Data Visualization
- Bar chart showing sales by product
- Pie chart showing sales contribution by region

### 6. Filter Data
- Display rows where sales are greater than 1000

### 7. Generate Insights
- Identify the top-selling product
- Determine the region with the highest sales

## How to Run

1. Open Jupyter Notebook:

```bash
jupyter notebook
```

2. Create a new Python notebook or open the provided notebook file.
3. Ensure `sales.csv` is in the same folder as the notebook.
4. Run each cell sequentially from top to bottom.
5. View the outputs, charts, and insights generated in the notebook.

## Expected Output

The notebook will display:
- Dataset preview
- Statistical summary
- Missing value report
- Sales aggregation results
- Visual charts
- Filtered records
- Key business insights

Example:

```text
--- Insights ---
Top-selling product: Laptop with sales: 5000
Region contributing most sales: North with sales: 8000
```

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- Matplotlib

## Learning Outcomes

By completing this task, you will learn:
- How to use Jupyter Notebook for data analysis
- Loading and exploring CSV datasets
- Performing data aggregation with Pandas
- Creating visualizations with Matplotlib
- Extracting meaningful insights from data
