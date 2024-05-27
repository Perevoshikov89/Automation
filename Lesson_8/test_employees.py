import requests
import json
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
    
    name = "QA_masters"
    descr = "masters_of_QA"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
   
    firstName = "Ivan"
    lastName = "Ivanov"
    middleName = "Ivanovich"
    company = companyId
    email = "ivanov_ivan@mail.ru"
    url = "string"
    phone = "89991234567"
    birthdate = "1990-01-01"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    
    body = api.get_employees_list(companyId) 
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Ivan"
    assert body[-1]["lastName"] == "Ivanov"
    assert body[-1]["middleName"] == "Ivanovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89991234567"
    assert body[-1]["birthdate"] == "1990-01-01"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    name = "Motoparts"
    descr = "Запчасти для мотоциклов"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
  
    new_company = api.get_company(new_id)
    companyId = new_company['id']
   
    body = api.get_employees_list(companyId)
    begin_list = len(body) 
   
    firstName = "Moto"
    lastName = "Motov"
    middleName = "Akropovich"
    company = companyId
    email = "motoparts@moto.ru"
    url = "string"
    phone = "89992345678"
    birthdate = "2000-01-01"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
 
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Moto"
    assert body[-1]["lastName"] ==  "Motov"
    assert body[-1]["middleName"] == "Akropovich"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "89992345678"
    assert body[-1]["birthdate"] == "2000-01-01"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    name = "По ветру"
    descr = "Одежда для мотоциклистов"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    firstName = "Ветер"
    lastName = "Ветров"
    middleName = "Ветрович"
    company = companyId
    email = "po_vetru@mail.ru"
    url = "string"
    phone = "89998765432"
    birthdate = "2000-01-02"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employees_list(companyId) 
   
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]

    new_email = "po_vetru@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "po_vetru@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False