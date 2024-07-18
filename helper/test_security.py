from helper.security import hash_password, verify_password, create_access_token, decode_access_token
import pytest

def test_password_hashing():
    test_value :str = "Pythonamic"
    hash_value = hash_password(test_value)
    assert isinstance(hash_value, (str)), "The data type receive must be in String."
    assert verify_password(test_value, hash_value), "Failed to verify the value."

    test_value :str  = "1234passwOrd.!"
    hash_value = hash_password(test_value)
    assert isinstance(hash_value, (str)), "The data type receive must be in String."
    assert verify_password(test_value, hash_value), "Failed to verify the value."
    
    test_value :str  = "1234passwiiiiiiiiiiiodjfakldjf sa.f asfd. saf jof  df!iiiiasdf af123 1r  afssgewg 346 2rfe fdsiiiiOrd.!"
    hash_value = hash_password(test_value)
    assert isinstance(hash_value, (str)), "The data type receive must be in String."
    assert verify_password(test_value, hash_value), "Failed to verify the value."
    
def test_invalid_input():    
    with pytest.raises(TypeError):
        test_value : int = 123123
        _ = hash_password(test_value)

    with pytest.raises(TypeError):
        test_value = b'01001111011010101001011010101010'
        _ = hash_password(test_value)

    with pytest.raises(TypeError):
        test_value : bool = True
        _ = hash_password(test_value)

    with pytest.raises(TypeError):
        test_value = None
        _ = hash_password(test_value)
        
    with pytest.raises(TypeError):
        test_value : int = 123918273
        hash_value : int = 19280219824902813
        _ = verify_password(test_value, hash_value)
        
def test_token_generation():
    user = {
        "id": 15,
        "name": "Lorem Ipsum",
        "age": 28
    }
    dummy_secret = {
        "SECRET_KEY":"3dWdasgSdpSi0/D4qtaZ31BVg8t6/pq5j6VkPt6ucZA=",
        "ALGORITHM": "HS256"
    }
    
    access_token = create_access_token(data=user, SECRET_SETTING=dummy_secret)
    assert access_token != None
    assert isinstance(access_token, (str))

    decoded_token = decode_access_token(encoded_jwt=access_token, SECRET_SETTING=dummy_secret)
    assert isinstance(decoded_token, (dict))
    assert decoded_token.keys() 
    assert "exp" in decoded_token.keys()
    assert set(user.keys()).issubset(set(decoded_token.keys()))
