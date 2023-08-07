import csv  # In-built module of Python
with open('data.csv', mode='r') as data:
    data_dict = list(csv.DictReader(data)) # to read the CSV file and convert into a dictionary(We read by this method because dictionary is faster than list.)
    age_lst = []
    salary_lst = []
    condition_count = 0
    for item in data_dict:
        age_lst.append(item['Age'])
        salary_lst.append(float(item['Salary']))
        if item['Age']==28 and item['Gender']=="Female":
            condition_count += 1
    average_of_salary = sum(salary_lst)/len(salary_lst)
    min_age = min(age_lst)
    max_age = max(age_lst)
    print(f"Average of Salary is {str(average_of_salary)}")
    print(f"Minimum Age is {str(min_age)}")
    print(f"Maximum Age is {(max_age)}")
    print(f"The number of rows that satisfy the condition that age is 28 and Gender is Female is {(condition_count)}")


"""
Output of the about code will be:
Average of Salary is 68400.0
Minimum Age is 27
Maximum Age is 52
The number of rows that satisfy the condition that age is 28 and Gender is Female is 0
"""