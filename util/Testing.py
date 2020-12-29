"""
Simple class for testing
"""
class Testing(object):
    def __init__(self, title=""):
        self.title = title
        self.funcs = []
        self.outcomes = []
        self.parameters = []
        self.titles = []

    def run(self):
        count = 0
        print("\n* Tests for " + self.title)
        print("Running tests...")
        for i, (title, out, func, p) in enumerate(zip(self.titles, self.outcomes, self.funcs, self.parameters)):

            result = None
            if type(p) is tuple:
                result = func(*p)
            else:
                result = func(p)

            valid = (out == result)
            test_title = ""
            if title is not None:
                test_title = title
            status = "✅" if valid else "❌"
            print("\tTest " + str(i+1) + ": " + test_title + " " + status)

            if valid:
                print("\t\t+ Params: " + str(p) + "\n\t\t\t -> Result: " + str(result) + " == Expected: " + str(out))
                count += 1
            else:
                print("\t\t- Expected: " + str(out) + ";\n\t\t\t Obtained: " + str(result))
        print("Finishing tests...")
        print("\t* Stats: " + str(count) + "/" + str(len(self.funcs)) + " successful.")
        print()

    def addTest(self, expected, _callback, *params, title=None):
        if expected is None or _callback is None or params is None:
            return
        self.titles.append(title)
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
        self.titles = []
