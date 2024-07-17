from helper.security import hash_password, verify_password, create_access_token
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
        
    