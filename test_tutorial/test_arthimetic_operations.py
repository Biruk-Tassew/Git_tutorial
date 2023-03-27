'test_arthimetic_operations.py'
import pytest
from arthimetic_operations import ArthimeticClass

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output

    def test_substract(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = -1.0
        # act
        actual_output = ArthimeticClass.subtract(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.subtract(str(x), y)
        with pytest.raises(TypeError):
            ArthimeticClass.subtract(x, str(y))
        with pytest.raises(TypeError):
            ArthimeticClass.subtract(str(x), str(y))
        
        assert expected_output == actual_output
    
    def test_multiply(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 2.0
        # act
        actual_output = ArthimeticClass.multiply(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(str(x), y)
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(x, str(y))
        with pytest.raises(TypeError):
            ArthimeticClass.multiply(str(x), str(y))
        
        assert expected_output == actual_output

    def test_divide(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 0.5
        # act
        actual_output = ArthimeticClass.divide(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.divide(str(x), y)
        with pytest.raises(TypeError):
            ArthimeticClass.divide(x, str(y))
        with pytest.raises(TypeError):
            ArthimeticClass.divide(str(x), str(y))
        
        assert expected_output == actual_output
