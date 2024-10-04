import unittest
import json
import dacite
from ProjectManagerSdk.models.taskdto import TaskDto

class TestDaciteParsing(unittest.TestCase):

    # Attempt to deserialize a task similar to how we do it in QueryTasks
    def test_basic_parsing(self):

        content = '{ "data": [{"id": "d71246fa-22e5-47e5-bbd8-42e10ff69fc9", "name": "Test Task"}] }'

        # This is the code we use for parsing in QueryTasks
        data = []
        for dict in json.loads(content)['data']:
            data.append(dacite.from_dict(data_class=TaskDto, data=dict))

        # Some assertions
        self.assertEqual(1, len(data))
        self.assertEqual("d71246fa-22e5-47e5-bbd8-42e10ff69fc9", data[0].id)
        self.assertEqual("Test Task", data[0].name)
        
    # Attempt to deserialize a task similar to how we do it in QueryTasks
    def test_extra_fields(self):

        content = '{ "data": [{"id": "d71246fa-22e5-47e5-bbd8-42e10ff69fc9", "name": "Test Task", "some_random_new_Field": "hello" }] }'

        # This is the code we use for parsing in QueryTasks
        data = []
        for dict in json.loads(content)['data']:
            data.append(dacite.from_dict(data_class=TaskDto, data=dict))

        # Some assertions
        self.assertEqual(1, len(data))
        self.assertEqual("d71246fa-22e5-47e5-bbd8-42e10ff69fc9", data[0].id)
        self.assertEqual("Test Task", data[0].name)
        
