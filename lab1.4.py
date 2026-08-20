def search_emp(emp_list, emp_id, index=0):
    if index==len(emp_list):
        return False
    if emp_list[index]==emp_id:
        return True
    return search_emp(emp_list, emp_id, index+1)
employees=[132,4532,234,235,236]
emp_id=int(input("Enter emp id to search:"))
if search_emp(employees, emp_id):
    print("Employee id found.")
else:
    print("employee is is not found.")
