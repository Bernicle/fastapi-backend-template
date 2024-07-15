from helper.security import hash_password, verify_password, create_access_token
import pytest

def test_password_hashing():
    test_value = "Pythonamic"
    hash_value = hash_password(test_value)
    assert isinstance(hash_value, (str)), "The data type receive must be in String."
    assert verify_password(test_value, hash_value), "Failed to verify the value."

    test_value = "1234passwOrd.!"
    hash_value = hash_password(test_value)
    assert isinstance(hash_value, (str)), "The data type receive must be in String."
    assert verify_password(test_value, hash_value), "Failed to verify the value."
    
    test_value = "1234passwiiiiiiiiiiiodjfakldjf sa.f asfd. saf jof  df!iiiiasdf af123 1r  afssgewg 346 2rfe fdsiiiiOrd.!"
    hash_value = hash_password(test_value)
    assert isinstance(hash_value, (str)), "The data type receive must be in String."
    assert verify_password(test_value, hash_value), "Failed to verify the value."
    
    
    with pytest.raises(TypeError):
        test_value = 123123
        hash_value = hash_password(test_value)

    with pytest.raises(TypeError):
        test_value = b'01001111011010101001011010101010'
        _ = hash_password(test_value)
        
    with pytest.raises(TypeError):
        test_value = 123918273
        hash_value = 19280219824902813
        _ = verify_password(test_value, hash_value)
        
    