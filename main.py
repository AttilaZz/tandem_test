import pandas as pd
import numpy as np
def get_employees_df():


  return pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82"
        "ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
  )
def get_departments_df():
  dep_df = pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5"
        "bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv"
  )
  dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})


  return dep_df


employees = get_employees_df()
departments = get_departments_df()

# 1. Please calculate the average, median, lower and upper quartiles of an employees' salaries.

average_emp = employees.loc[:, 'SALARY'].mean()
median_emp = employees.loc[:, 'SALARY'].median()
lower_quart_emp = employees.loc[:, 'SALARY'].quantile(0.25)
upper_quart_emp = employees.loc[:, 'SALARY'].quantile(0.75)
print("Average of Employees Salaries        = ", average_emp)
print("Median of Employees Salaries         = ", median_emp)
print("Lower quartile of Employees Salaries = ", lower_quart_emp)
print("Upper quartile of Employees Salaries = ", upper_quart_emp)
print("==========================================================================")



# 2. Please calculate the average salary per department. Please include the department name in the results.

average_by_dept = employees.groupby("DEPARTMENT_ID")['SALARY'].mean()
average_by_dept_with_name = pd.merge(average_by_dept, departments, how='left', left_on='DEPARTMENT_ID', right_on='DEPARTMENT_IDENTIFIER')[['SALARY', 'DEPARTMENT_NAME']].rename(columns={'SALARY': 'AVG_SALARY'})
average_by_dept_with_id = pd.merge(average_by_dept, departments, how='left', left_on='DEPARTMENT_ID', right_on='DEPARTMENT_IDENTIFIER')[['SALARY', 'DEPARTMENT_IDENTIFIER']].rename(columns={'DEPARTMENT_IDENTIFIER': 'DEPARTMENT_ID', 'SALARY': 'AVG_DEPT_SALARY'})
print(average_by_dept_with_name)


# 3. Please create a new column named `SALARY_CATEGORY` with value "low" when the salary is lower than average and "high" if is it higher or equal.

employees['SALARY_CATEGORY'] = np.where(employees['SALARY'] < average_emp, "low", "high")
print(employees.head())


# 4. Please create another column named `SALARY_CATEGORY_AMONG_DEPARTMENT` with value "low" when the employee salary is lower than average in his / her department and "high" in the other case.

employees = pd.merge(employees, average_by_dept_with_id, how='left', on='DEPARTMENT_ID')
employees['SALARY_CATEGORY_AMONG_DEPARTMENT'] = np.where(employees['SALARY'] < employees['AVG_DEPT_SALARY'], "low", "high")


# 5. Please filter the dataframe `employees` to include only the rows where `DEPARTMENT_ID` equals to 20. Assign the result to new variable.

employees_20 = employees[employees['DEPARTMENT_ID'] == 20]

# 6. Please increase the salary by 10% for all employees working at the department 20.

employees['SALARY'] = np.where(employees['DEPARTMENT_ID'] == 20, employees['SALARY'] * 1.1, employees['SALARY'] )

# 7. Please check if any of the `PHONE_NUMBER` column values are empty.

print("is there any missing phone numbers ? -> ",employees['PHONE_NUMBER'].isna().any())
