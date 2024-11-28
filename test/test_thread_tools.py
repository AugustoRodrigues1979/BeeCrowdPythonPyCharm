import time
import unittest
from concurrent.futures.thread import ThreadPoolExecutor

import pytest
import random
from test.threads_tools import CustomThreadPool, Constants
from unittest.mock import patch

def all_dummy_task_dict():
    return {
        'getExpectedResultFromNumber': lambda x: 'x',
        'getChallengeResultFromNumber': lambda x: 'x',
        'compareResults': lambda x, y: True
    }  # Returning a task dict with all task equal to dummy task


@pytest.fixture(scope="class")
def empty_task_dict(self):
    yield dict()  #Returning a empty task dict


@pytest.fixture(scope="class")
def all_task_is_none_objetc_in_task_dict():
    task_dict = {
        'getExpectedResultFromNumber': None,
        'getChallengeResultFromNumber': None,
        'compareResults': None
    }  #Setting a task dict with all task equal to invalid task (none)
    yield task_dict  #Provide task dict for test function
    del task_dict  # Free task dict


@pytest.fixture(scope="class")
def get_expected_result_task_is_equal_none_in_task_dict():
    task_dict = {
        'getExpectedResultFromNumber': None,
        'getChallengeResultFromNumber': lambda x: 'x',
        'compareResults': lambda x, y: True
    }  #Setting a task dict with only get Expected Result task equal to invalid task (none)
    yield task_dict  #Provide task dict for test function
    del task_dict  # Free task dict


@pytest.fixture(scope="class")
def get_challenge_result_task_is_equal_none_in_task_dict():
    task_dict = {
        'getExpectedResultFromNumber': lambda x: 'x',
        'getChallengeResultFromNumber': None,
        'compareResults': lambda x, y: True
    }  #Setting a task dict with only get Challenge Result task equal to invalid task (none)
    yield task_dict  #Provide task dict for test function
    del task_dict  # Free task dict


@pytest.fixture(scope="class")
def compare_result_task_is_equal_none_in_task_dict():
    task_dict = {
        'getExpectedResultFromNumber': lambda x: 'x',
        'getChallengeResultFromNumber': lambda x: 'x',
        'compareResults': None
    }  #Setting a task dict with only get compare Results task equal to invalid task (none)
    yield task_dict  #Provide task dict for test function
    del task_dict  # Free task dict

def setup_init_data_for_call_run_method():
    task_dict = all_dummy_task_dict()  #Setting task dict
    thread_pool = CustomThreadPool(1, task_dict)  #Try call CustomThreadPool
    begin_interval = round(random.uniform(0, 50.01), 2)  #Select a float number between 0 and 50.01 (inclusive number 50)
    end_interval = round(random.uniform(begin_interval, 50.01), 2)  #Select a float number between begin interval to 50.01 (inclusive number 50)
    step_interval = round(random.random(), 2)  #Select a float number how step interval
    thread_pool.setup_run(begin_interval, end_interval, step_interval) #Run setup run method with range of values
    return thread_pool, begin_interval, end_interval, step_interval #Return instance

class TestThreadPool(unittest.TestCase):
    def setUp(self):
        random.seed(time.time())  # Set a seed for random algoritm

    def test_get_default_amount_thread_when_created_obj_without_amount_thread_argument(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        thread_pool = CustomThreadPool(task_dict=task_dict)  #Create an object for CustomThreadPool
        assert thread_pool._amount_thread == Constants.DEFAULT_AMOUNT_THREAD.value  #Assert if _amount_threads is equal to default value

    def test_create_pool_threads_with_amount_thread_greater_than_0(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict)  #Create an object for CustomThreadPool with one thread
        assert thread_pool._amount_thread == 1  #Assert if _amount_threads is equal to 1

    def test_raise_error_when_try_create_pool_threads_with_amount_thread_minor_the_zero(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        msg_error = 'Expected error when create pool threads with amount minor the zero'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(-1,
                                           task_dict)  #Create an object for Custom Thread Pool with amount thread minor the zero

    def test_raise_error_when_try_create_pool_threads_with_amount_thread_equal_the_zero(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        msg_error = 'Expected error when create pool threads with amount equal the zero'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(0,
                                           task_dict)  #Create an object for Custom Thread Pool with amount thread minor the zero

    def test_raise_error_when_change_default_amount_thread(self):
        msg_error = 'Should not possible assigment any value for Enum variable named DEFAULT_AMOUNT_THREAD'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            Constants.DEFAULT_AMOUNT_THREAD.value = 1  #Attempt invalid when assignment any value to enum type variable

    def test_raise_error_when_do_not_provided_task_dict(self):
        msg_error = 'Do not possible create pool thread without task associated'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(1)  #Create an object for CustomThreadPool with one thread and none task dict

    def test_raise_error_when_do_provided_invalid_task_dict(self):
        msg_error = 'Do not possible create pool thread with empty task dict'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(1, 'dict()')  #Try call CustomThreadPool invalid task dict

    def test_raise_error_when_do_provided_empty_task_dict(self):
        msg_error = 'Do not possible create pool thread with empty task dict'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(1, dict())  #Try call CustomThreadPool with empty task dict

    def test_raise_error_when_do_provided_task_dict_without_get_expected_result_key(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        del task_dict['getExpectedResultFromNumber']  #Remove a specify task key
        msg_error = 'Do not possible create pool thread without getExpectedResultFromNumber key in task dict'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(1, task_dict)  #Try call CustomThreadPool without task key

    def test_raise_error_when_do_provided_task_dict_without_get_challenge_result_from_number_key(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        del task_dict['getChallengeResultFromNumber']  #Remove a specify task key
        msg_error = 'Do not possible create pool thread without getChallengeResultFromNumber key in task dict'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(1, task_dict)  #Try call CustomThreadPool without task key

    def test_raise_error_when_do_provided_task_dict_without_compare_result_from_number_key(self):
        task_dict = all_dummy_task_dict()  #Setting task dict
        del task_dict['compareResults']  #Remove a specify task key
        msg_error = 'Do not possible create pool thread without compareResults key in task dict'  #Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool = CustomThreadPool(1, task_dict)  #Try call CustomThreadPool without task key

    def test_setup_run_should_raise_when_provided_begin_interval_what_not_is_number(self):
        task_dict = all_dummy_task_dict()  # Setting task dict
        thread_pool = CustomThreadPool(1, task_dict)  # Try call CustomThreadPool
        msg_error = "Begin interval should is number type"  # Setting a message error
        with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=None, end_interval=100, step_interval=1)

    def test_setup_run_should_raise_when_provided_end_interval_what_not_is_number(self):
        task_dict = all_dummy_task_dict() #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict) #Create Thread Pool
        msg_error = "End interval should is number type" #Setting a message error
        with self.assertRaises(Exception, msg=msg_error): #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=1, end_interval='100', step_interval=1)

    def test_setup_run_should_raise_when_provided_step_interval_what_not_is_number(self):
        task_dict = all_dummy_task_dict() #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict)  #Create Thread Pool
        msg_error = "Step interval should is number type" #Setting a message error
        with self.assertRaises(Exception, msg=msg_error): #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=1, end_interval=100, step_interval=dict())

    def test_setup_run_should_raise_when_provided_begin_interval_greather_then_end_interval(self):
        task_dict = all_dummy_task_dict() #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict) #Create Thread Pool
        msg_error = "Begin interval should is minor the end interval" #Setting a message error
        with self.assertRaises(Exception, msg=msg_error): #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=100, end_interval=2, step_interval=-1)

    def test_setup_run_should_raise_when_provided_end_interval_minor_then_begin_interval(self):
        task_dict = all_dummy_task_dict() #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict) #Create Thread Pool
        msg_error = "End interval should is greathest the begin interval" #Setting a message error
        with self.assertRaises(Exception, msg=msg_error): #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=100, end_interval=2, step_interval=-1)

    def test_setup_run_should_raise_when_provided_step_interval_equal_to_zero(self):
        task_dict = all_dummy_task_dict() #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict) #Try call CustomThreadPool
        msg_error = "Step interval should is greather then zero" #Setting a message error
        with self.assertRaises(Exception, msg=msg_error): #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=1, end_interval=100, step_interval=0)

    def test_setup_run_should_raise_when_provided_step_interval_minor_then_zero(self):
        task_dict = all_dummy_task_dict() #Setting task dict
        thread_pool = CustomThreadPool(1, task_dict) #Try call CustomThreadPool
        msg_error = "Step interval should is greather then zero" #Setting a message error
        with self.assertRaises(Exception, msg=msg_error): #Setting a way for capture an exception
            thread_pool.setup_run(begin_interval=1, end_interval=100, step_interval=-1)

    def test_setup_run_should_provided_correct_amount_unprocessed_numbers(self):
        thread_pool, begin_interval, end_interval, step_interval = setup_init_data_for_call_run_method()
        expected_amount_unprocessed_numbers = int(
            round((end_interval - begin_interval) / step_interval)) #Obtain expected amount unprocessed numbers
        obtained_amount_unprocessed_numbers = thread_pool._amount_unprocessed_numbers #Get amount unprocessed numbers provided by setup run method
        self.assertEqual(expected_amount_unprocessed_numbers,obtained_amount_unprocessed_numbers) #Assert if numbers are equal

    def test_setup_run_create_running_task_dict_when_each_entry_in_this_dict_contain_all_amount_unprocessed_numbers(self):
        thread_pool, begin_interval, end_interval, step_interval = setup_init_data_for_call_run_method()
        expected_amount_keys = int(round((end_interval - begin_interval) / step_interval)) #Obtain expected amount keys for each unprocessed numbers
        thread_pool.setup_run(begin_interval, end_interval, step_interval) #Call setup run with a specify range
        obtained_amount_keys = len(thread_pool._running_task_dict) #Get amount keys in this dict
        self.assertEqual(expected_amount_keys, obtained_amount_keys) #Assert if numbers are equal

    def test_run_raise_exception_when_dont_possible_triggers_associate_by_unique_value(self):
        test_class = setup_init_data_for_call_run_method()[0]
        with patch.object(test_class._threadPool, 'submit', side_effect=Exception("An error occurred")): #Setting a way for capture an exception
            msg_error = "Expected exception when occurs any exception when triggers a thread"  #Setting a message error if expection do not raise with success
            with self.assertRaises(Exception, msg=msg_error):  #Setting a way for capture an exception
                test_class.run() #Run method what should raise a exception




if __name__ == '__main__':
    unittest.main()
