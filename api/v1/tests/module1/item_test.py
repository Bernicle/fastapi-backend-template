
def test_get_items_success(test_client):
    response = test_client.get("/api/v1/module1/items")
    assert response.status_code == 200, "The expected return status in not 200"
    data = response.json()
    assert isinstance(data, list), "Expected Return Type if in `List`"

def test_basic_register(test_client):

    response = test_client.post("/api/v1/module1/items", json={"name":"Instant Sisig (Pork)", "description":"Precook, Microwavable Food."})
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}")
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."

def test_create_and_update(test_client):

    response = test_client.post("/api/v1/module1/items", json={"name":"Instant Sisig (Pork)", "description":"Precook, Microwavable Food."})
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}")
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."
    new_data = {"name":"Instant Sisig (Chicken)", "description":"Premade, Microwavable Food."}
    response = test_client.put(f"/api/v1/module1/items/{created_data.get('id')}", json=new_data)
    assert response.status_code == 200, "Failed to update the data."
    updated_data = response.json()
    assert all(updated_data[key] == new_data[key] for key in new_data.keys()), "The return data is not updated based on new_data."
    

def test_create_and_delete(test_client):
    response = test_client.post("/api/v1/module1/items", json={"name":"Instant Sisig (Pork)", "description":"Precook, Microwavable Food."})
    assert response.status_code == 201, "Failed to Create a new Record/Data."
    created_data = response.json()
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}")
    assert response.status_code == 200, "Failed to get the data. assuming that the data we retrieve is already created."
    retrieve_data = response.json()
    
    created_data_keys = set(created_data.keys())
    retrieve_data_keys = set(retrieve_data.keys())
    
    assert created_data_keys == retrieve_data_keys, "The Keys/Column Name that inserted is not same with created data."
    
    response = test_client.delete(f"/api/v1/module1/items/{created_data.get('id')}")
    assert response.status_code == 204, "Failed to update the data."
    
    response = test_client.get(f"/api/v1/module1/items/{created_data.get('id')}")
    assert response.status_code == 400, "The status must be 400, since the data related to the provided ID is already deleted."
    lastest_data = response.json()
    assert "detail" in lastest_data.keys(), "the Key detail must be return to display the details of error."
