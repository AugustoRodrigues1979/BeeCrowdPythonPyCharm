import threading
import time
from concurrent.futures import ThreadPoolExecutor
import logging

from enum import Enum
import types

class Constants(Enum):
    DEFAULT_AMOUNT_THREAD = 1000
    DEFAULT_AMOUNT_TASK = {
        'getExpectedResultFromNumber': None,
        'getChallengeResultFromNumber': None,
        'compareResults': None
    }

    WORKER_NOT_ALLOCATED = 1
    WORKER_ALLOCATED = 2
    WORKER_RUNNING = 3
    WORKER_END = 4
    WORKER_NOT_ALLOCATED_BY_ERROR = 5


class CustomThreadPool:
    def __init__(self,
                 amount_thread = Constants.DEFAULT_AMOUNT_THREAD.value,
                 task_dict = dict(Constants.DEFAULT_AMOUNT_TASK.value),
                 ):

        logging.basicConfig(
            level=logging.DEBUG,  #Set logging level
            format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s', #Set format for each entry log
            handlers=[logging.FileHandler('thread_log.log', mode='w')]  #Output to log file
        )
        self._worker_task = None
        self._actual_target_value = None #Set temporary variable for adm use
        self._amount_unprocessed_numbers = 0 #Set amount of unprocessed numbers
        self._running_task_dict = None #Set the number of running task dictionary entries
        self._amount_finished_processed_numbers = 0 #Set amount of finished processed numbers
        if type(amount_thread) != type(1) or amount_thread <= 0: #Check if amount of threads is greater than 0
            raise ValueError('Need give amount of threads greater than 0') #Raise exception because what amount of threads is minor or equal to zero

        if type(task_dict) != type(dict()) or len(task_dict) < 3: #Check if task dict is valid type and contain valid number task
            raise ValueError(f'Provided invalid task dict') #Raise exception because what task dict is invalid or not contains 3 task key

        default_task_dict = dict(Constants.DEFAULT_AMOUNT_TASK.value) #Setting a default task dict
        for key in default_task_dict.keys(): #For each key in default task dict
            if not key in task_dict.keys(): #Check if key not found in task dict provided by user code
                raise IndexError(f'Not found task key:{key}') #Raise exception because what not founded specify key in task dict

            if type(task_dict[key]) != type(lambda:True): #Check if key value contains type other than function type
                raise ValueError(f'Associated invalid task for {key}') #Raise exception because invalid type in key value

        self._amount_thread = amount_thread #Setting amount of threads
        self._task_dict = task_dict.copy() #Setting a task dict
        queue_amount = int(round((amount_thread*25)/100,0))
        self._threadPool = ThreadPoolExecutor(max_workers=amount_thread)

        logging.info('Created object by CustomThreadPool Class....')

    def setup_run(self,
            begin_interval = 0.00,
            end_interval = 0.01,
            step_interval = 0.01
            ):

        logging.info('Init Setup runners....')

        begin_interval = round(begin_interval,2) #Rounds to 2 decimal places
        end_interval = round(end_interval, 2) #Rounds to 2 decimal places
        step_interval = round(step_interval, 2) #Rounds to 2 decimal places

        interval_list = [begin_interval, end_interval, step_interval] #Creating a list with function's numeric arguments
        for interval in interval_list: #For each interval from the list
            if not isinstance(interval, (int, float)):
                raise ValueError('Invalid type in numeric arguments') #Raise an exception

        if begin_interval > end_interval or step_interval <= 0: #Check if numeric arguments are valid
            raise ValueError('Invalid Number provided in arguments') #Raise an exception

        default_status_worker = Constants.WORKER_NOT_ALLOCATED #Set a default state of worker
        default_worker_task_dict = {'status': default_status_worker, 'result': '', 'worker_task': None, 'thread': None} #Set a default entry
        worker_dict = {
            'expected_task_dict': default_worker_task_dict.copy(),
            'challenge_task_dict': default_worker_task_dict.copy(),
            'compare_task_dict': default_worker_task_dict.copy()
        } #Set a default worker dict
        worker_dict['expected_task_dict']['worker_task'] = self._task_dict['getExpectedResultFromNumber'] #Set a specificy task for key
        worker_dict['challenge_task_dict']['worker_task'] = self._task_dict['getChallengeResultFromNumber'] #Set a specificy task for key
        worker_dict['compare_task_dict']['worker_task'] = self._task_dict['compareResults'] #Set a specificy task for key

        amount_unprocessed_numbers = (end_interval - begin_interval) / step_interval #Get amount unprocessed numbers in float format
        self._amount_unprocessed_numbers = int(round(amount_unprocessed_numbers,0)) #Set amount unprocessed numbers in int format

        self._running_task_dict = dict() #Create a dict what will store all results from the task between begin interval to end interval
        target_value = begin_interval #Set begin range
        while target_value <= end_interval: #Run over all numbers between the start and end range
            target_value_str = f'{target_value:.02f}' #Get the string representation of target value
            self._running_task_dict[target_value_str] = worker_dict #Create a key and assign this key as a working dictionary
            target_value = round(target_value + step_interval,2) #Take the next target value

        logging.info('Setup runners ok....')

    def _call_get_expected_result_task(self, target_dict):
        logging.info(f'Begin Trigger GetExpectedThread [{target_dict['target_id']}]')

        try:
            task_dict = target_dict['target_info']['expected_task_dict']
            task = task_dict['worker_task']
            with self._threadPool as executor:
                thread = executor.submit(task, task_dict)
        except Exception as e:
            logging.info(f'Exception when Trigger GetExpectedThread [{target_dict['target_id']}].Reason: {e}')

        logging.info(f'End Trigger GetExpectedThread [{target_dict['target_id']}]')

    def _call_get_challenge_result_task(self, target_dict):
        logging.info(f'Begin Trigger ChallengeThread [{target_dict['target_id']}]')
        try:
            task_dict = target_dict['target_info']['challenge_task_dict']
            task = task_dict['worker_task']
            with self._threadPool as executor:
                thread = executor.submit(task, task_dict)
        except Exception as e:
            logging.info(f'Exception when Trigger GetExpectedThread [{target_dict['target_id']}].Reason: {e}')

        logging.info(f'End Trigger ChallengeThread [{target_dict['target_id']}]')

    def _call_compare_result_task(self, target_dict):
        expected_target_dict = target_dict['target_info']['expected_task_dict']
        challenge_target_dict = target_dict['target_info']['challenge_task_dict']

        keep_finished_threads = True
        while keep_finished_threads:
            is_finished_expected_thread = expected_target_dict['status']
            is_finished_challenge_thread = challenge_target_dict['status']
            if not is_finished_expected_thread or not is_finished_challenge_thread:
                time.sleep(3)
            else:
                keep_finished_threads = False

        compare_task_dict = target_dict['target_info']['compare_task_dict']
        compare_task_dict['expected_result'] = expected_target_dict['result']
        compare_task_dict['challenge_result'] = challenge_target_dict['result']
        task = compare_task_dict['worker_task']
        with self._threadPool as executor:
            executor.submit(task, compare_task_dict)

    def _call_safe_thread(self, target_dict):
        logging.info(f'Begin Trigger Threads associate to [{target_dict['target_id']}]')
        self._call_get_expected_result_task(target_dict)
        self._call_get_challenge_result_task(target_dict)
        self._call_compare_result_task(target_dict)
        logging.info(f'End Trigger Threads associate to [{target_dict['target_id']}]')

    def run(self):
        logging.info('Triggers threads begin....')
        self._amount_finished_processed_numbers = 0 #Set initial amount of unprocessed numbers
        for target_value_key in self._running_task_dict.keys(): #For each target value key setted in running_task dict
            target_value_dict = self._running_task_dict[target_value_key] #Get a dict associated in target value dict
            try:
                logging.info(f'Call Threads for [{target_value_key}]')
                with self._threadPool as executor:
                    target_dict = dict()
                    target_dict['target_id'] = target_value_key
                    target_dict['target_info'] = target_value_dict
                    executor.submit(self._call_safe_thread,target_dict)
                logging.info(f'End Call Threads for [{target_value_key}]')
            except Exception as e:
                    logging.info(f'Exception when Call Threads for [{target_value_key}] Reason: {e}')
                    raise e
        logging.info('Triggers threads finished....')