#############################################################################
# Happy Scenario
#############################################################################

import pytest

from api.v1.tests.authentication.authenthication_test import get_authorization_header


def test_get_items_success(test_client):
    headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")
    response = test_client.get("/api/v1/module1/items", headers=headers)
    assert response.status_code == 200, "The expected return status in not 200"
    data = response.json()
    assert isinstance(data, list), "Expected Return Type if in `List`"

def test_basic_register(test_client, test_faker):
    product_name = test_faker.ecommerce_name()

    pay_load = {
        "name":product_name, 
        "description":product_name,
        "price":test_faker.ecommerce_price()
    }
    headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")
    response = test_client.post("/api/v1/module1/items", json=pay_load, headers=headers)
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}", headers=headers)
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."

def test_many_register(test_client, test_faker):
    for i in range(50):
        product_name = test_faker.ecommerce_name()
        pay_load = {
            "name":product_name, 
            "description":product_name,
            "price":test_faker.ecommerce_price()
        }
        
        pay_load_keys = pay_load.keys()

        
        headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")

        response = test_client.post("/api/v1/module1/items", json=pay_load, headers=headers)
        
        assert response.status_code == 201, "Failed to Create a new Record/Data."
        created_data = response.json()
        assert all({ pay_load[k] == created_data[k] for k in pay_load_keys}), "The Created Data is not the Same with the Pay Load."
        
        response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}", headers=headers)
        assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
        retrieve_data = response.json()
        
        created_data_keys = set(created_data.keys())
        retrieve_data_keys = set(retrieve_data.keys())
        
        assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."
        assert all({ retrieve_data[k] == created_data[k] for k in created_data})
    
def test_create_and_update(test_client, test_faker):
    
    product_name = test_faker.ecommerce_name()
    pay_load = {
        "name":product_name, 
        "description":product_name,
        "price":test_faker.ecommerce_price()
    }

    headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")
    response = test_client.post("/api/v1/module1/items", json=pay_load, headers=headers)
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}", headers=headers)
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."
    new_data = {"name":"Instant Sisig (Chicken)", "description":"Premade, Microwavable Food."}
    response = test_client.put(f"/api/v1/module1/items/{created_data.get('id')}", json=new_data, headers=headers)
    assert response.status_code == 200, "Failed to update the data."
    updated_data = response.json()
    assert all(updated_data[key] == new_data[key] for key in new_data.keys()), "The return data is not updated based on new_data."
    
def test_create_and_delete(test_client, test_faker):
    product_name = test_faker.ecommerce_name()
    pay_load = {
        "name":product_name, 
        "description":product_name,
        "price":test_faker.ecommerce_price()
    }

    headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")
    response = test_client.post("/api/v1/module1/items", json=pay_load, headers=headers)
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}", headers=headers)
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."
    
    response = test_client.delete(f"/api/v1/module1/items/{created_data.get('id')}", headers=headers)
    assert response.status_code == 204, "Failed to update the data."
    
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}", headers=headers)
    assert response.status_code == 400, "The status must be 400, since the data related to the provided ID is already deleted."
    lastest_data = response.json()
    assert "detail" in lastest_data.keys(), "the Key detail must be return to display the details of error."

#############################################################################
# Error Handling
#############################################################################

def test_register_with_missing_column1(test_client, test_faker):
    
    product_name1 = test_faker.ecommerce_name()    
    #Missing column 'name'
    pay_load1 = {
        "description":product_name1,
        "price":test_faker.ecommerce_price()
    }
    
    product_name2 = test_faker.ecommerce_name()    
    #Missing column 'name'
    pay_load2 = {
        'name': product_name2,
        "description":product_name2
    }
    
    headers = get_authorization_header(test_client,"poncebernard123", "loremIpsum123")

    response1 = test_client.post("/api/v1/module1/items", json=pay_load1, headers=headers)
    assert response1.status_code == 422, "Expected Status Code 422 is not received."
    created_data = response1.json()
    assert 'name' in str(created_data), "The error message should indicate that the 'name' column is missing"

    response2 = test_client.post("/api/v1/module1/items", json=pay_load2, headers=headers)
    assert response2.status_code == 422, "Expected Status Code 422 is not received."
    created_data = response2.json()
    assert 'price' in str(created_data), "The error message should indicate that the 'price' column is missing"
    