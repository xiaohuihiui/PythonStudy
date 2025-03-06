import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create a dataframe to hold our data
# I'll define column names based on what we can see in the image
columns = [
    "序号", "日期栏", "凭证编号", "明细编号", "摘要", "科目", "借方金额",
    "贷方金额", "方向", "余额", "对方科目", "结算方式", "结算号", "用户名",
    "单位名称", "机构", "部门", "个人往来", "项目", "供应商", "客户"
]

# Generate some sample data (about 20 rows)
# This will create data similar to what we see in the screenshots
np.random.seed(42)  # For reproducibility

# Create a base date and generate sequential dates
base_date = datetime(2023, 1, 1)
dates = [base_date + timedelta(days=i) for i in range(20)]
dates_formatted = [d.strftime("%Y-%m-%d") for d in dates]

# Generate random transaction amounts between 5,000 and 10,000
amounts = np.random.uniform(5000, 10000, 20).round(2)
small_amounts = np.random.uniform(100, 1000, 20).round(2)

# Create sample Chinese text for categorical fields
department_options = ["财务部", "销售部", "生产部", "人事部", "技术部"]
person_options = ["张三", "李四", "王五", "赵六", "钱七"]
method_options = ["现金", "银行", "支票", "转账", "其他"]
category_options = ["收入", "支出", "转账", "借款", "还款"]

# Build the dataframe
data = {
    "序号": list(range(1, 21)),
    "日期栏": dates_formatted,
    "凭证编号": [f"P{2023}{i:04d}" for i in range(1, 21)],
    "明细编号": [f"D{i:04d}" for i in range(1, 21)],
    "摘要": np.random.choice(category_options, 20),
    "科目": [f"科目{i}" for i in range(1, 21)],
    "借方金额": amounts,
    "贷方金额": small_amounts,
    "方向": np.random.choice(["借", "贷"], 20),
    "余额": amounts - small_amounts,
    "对方科目": [f"对方科目{i}" for i in range(1, 21)],
    "结算方式": np.random.choice(method_options, 20),
    "结算号": [f"JS{i:06d}" for i in range(1, 21)],
    "用户名": np.random.choice(person_options, 20),
    "单位名称": [f"公司{i}" for i in range(1, 21)],
    "机构": ["总部" for _ in range(20)],
    "部门": np.random.choice(department_options, 20),
    "个人往来": np.random.choice(person_options, 20),
    "项目": [f"项目{i}" for i in range(1, 21)],
    "供应商": [f"供应商{i}" for i in range(1, 21)],
    "客户": [f"客户{i}" for i in range(1, 21)]
}

df = pd.DataFrame(data)

# Create two Excel files - one with all data and one with just a few rows
# First file (left screenshot with all data)
with pd.ExcelWriter('财务数据完整版.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    
    # Access the openpyxl workbook and worksheet objects to format them
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    
    # Set column widths to match the screenshot
    for i, col in enumerate(df.columns):
        column_width = max(len(col) * 1.2, 12)
        column_letter = openpyxl.utils.get_column_letter(i + 1)
        worksheet.column_dimensions[column_letter].width = column_width

# Second file (right screenshot with fewer rows)
with pd.ExcelWriter('财务数据简版.xlsx', engine='openpyxl') as writer:
    # Take just the first 5 rows for the second sheet
    df.head(5).to_excel(writer, sheet_name='Sheet1', index=False)
    
    # Format similarly to the first file
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    
    for i, col in enumerate(df.columns):
        column_width = max(len(col) * 1.2, 12)
        column_letter = openpyxl.utils.get_column_letter(i + 1)
        worksheet.column_dimensions[column_letter].width = column_width

print("Excel files have been created successfully!")