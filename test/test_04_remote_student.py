from src.remote_student import update_remote_students

class TestPurity:
    def test_returns_new_list_and_reference(self): 
        test_input = [{ "name": 'Euler', "age": 27, "location": 'remote' }]
        result = update_remote_students(test_input)
        assert result is not test_input

    def test_input_values_remain_unchanged(self): 
        test_input = [{ "name": 'Euler', "age": 27}] #must be an example that will be mutated 
        original = [{ "name": 'Euler', "age": 27}]
        update_remote_students(test_input)
        assert test_input == original

class TestOutput: 
    def test_location_added(self): 
        test_input = [{ "name": 'Euler', "age": 27}]
        result = update_remote_students(test_input)
        assert result == [{ "name": 'Euler', "age": 27, "location": 'remote' }]

    def test_location_added_using_list_with_multiple_values(self): 
        test_input = [
            { "name": 'Hypatia', "age": 31, "location": 'leeds' },
            { "name": 'Ramanujan', "age": 22 },
            { "name": 'Tao', "age": 47, "location": 'manchester' }
            ]
        result = update_remote_students(test_input)
        assert result == [
            { "name": 'Hypatia', "age": 31, "location": 'leeds' },
            { "name": 'Ramanujan', "age": 22, "location": 'remote' },
            { "name": 'Tao', "age": 47, "location": 'manchester' }
            ]
