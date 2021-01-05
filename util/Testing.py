class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""
Simple class for testing
"""
from copy import deepcopy
import time

class Testing(object):
    def __init__(self, title=""):
        self.title = title
        self.funcs = []
        self.expected = []
        self.parameters = []
        self.titles = []

    def run(self):
        count = 0
        print(bcolors.UNDERLINE + "\n* Tests for " + self.title + bcolors.ENDC)
        print("Running tests...")
        for i, (title, exp, func, input) in enumerate(zip(self.titles, self.expected, self.funcs, self.parameters)):
            
            result = None
            # execute callback func with params
            params = deepcopy(input)

            start_ms = time.time_ns() / 1000000 # milliseconds as float
            if type(params) is tuple:
                result = func(*params)
            else:
                result = func(params)
            end_ms = time.time_ns() / 1000000 # milliseconds as float

            time_in_ms = round(end_ms - start_ms, 4)
            timing = str(time_in_ms) + "ms"
            
            valid = (result == exp)
            test_title = ""
            if title is not None:
                test_title = title
            
            status = "✅" if valid else "❌"
            print(bcolors.BOLD + "\t" + str(i+1) + ") " + test_title + " " + status + " " + timing + bcolors.ENDC)
            if valid:
                print("\t\t+ Input: " + str(input))
                print("\t\t+ Expected: " + str(exp))
                print(bcolors.OKGREEN + "\t\t\t -> Output/Result: " + str(result) + bcolors.ENDC)
                count += 1
            else:
                print(bcolors.FAIL + "\t\t- Expected: " + str(exp) + "\n\t\t\t -> Obtained: " + str(result) + bcolors.ENDC)
                
            print()

        print("Finishing tests...")
        print(bcolors.BOLD + "\t* Stats: " + str(count) + "/" + str(len(self.funcs)) + " successful." + bcolors.ENDC)
        print()

    def addTest(self, expected, _callback, *params, title=None):
        if expected is None or _callback is None or params is None:
            return
        self.titles.append(title)
        self.expected.append(expected)
        self.funcs.append(_callback)

        if type(*params) is tuple:
            self.parameters.append(*params)
        else:
            self.parameters.append(params[0])

    def clean(self):
        self.funcs = []
        self.expected = []
        self.parameters = []
        self.titles = []
