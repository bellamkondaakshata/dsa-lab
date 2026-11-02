def search_emp(emp_list, emp_id, index=0):
    if index == len(emp_list):
        return False
    if emp_list[index]==emp_id:
        return True
    return search_emp(emp_list, emp_id, index+1)
employees=[101,102,103,104,105]
emp_id=int(input("enter employee id to search:"))
if search_emp(employees, emp_id):
    print("employee id found")
else:
    print("employee id not found")
