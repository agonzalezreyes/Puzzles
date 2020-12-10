class Testing(object):
    def __init__(self, title=""):
        self.title = title
        self.funcs = []
        self.outcomes = []
        self.parameters = []

    def run(self):
        count = 0
        print("* Tests for " + self.title)
        print("Starting tests...")
        for i, (out, func, p) in enumerate(zip(self.outcomes, self.funcs, self.parameters)):
            
            result = None
            if type(p) is tuple:
                result = func(*p)
            else:
                result = func(p)

            valid = (out == result)
            status = "✅" if valid else "❌"
            print("\tTest " + str(i+1) + ": " + status)

            if valid:
                print("\t\t+ Input: " + str(p) + " -> Result: " + str(result) + " == Expected: " + str(out))
                count += 1
            else:
                print("\t\t- Expected: " + str(out) + "; Obtained: " + str(result))
        print("Finishing tests...")
        print("\t* Stats: " + str(count) + "/" + str(len(self.funcs)) + " successful.")

    def addTest(self, expected, _callback, *params):
        if expected is None or _callback is None or params is None:
            return
        self.outcomes.append(expected)
        self.funcs.append(_callback)
        
        if type(*params) is tuple:
            self.parameters.append(*params)
        else:
            self.parameters.append(params[0])

    def clean(self):
        self.funcs = []
        self.outcomes = []
        self.parameters = []
