import commands

class Testkit:
    def __init__(self):
        self.actuator = commands.Actuator()
        self.module_tests = self.get_module_tests()
        self.run_module_tests()


    def get_module_tests(self):
        """ Tests are written as 1 line commands in a .txt """
        lines = []
        with open("tests.txt", "r+") as file:
            for line in file.readlines():
                lines.append(line.replace("\n", ""))
        return lines


    def run_module_tests(self):
        nick = "Bob"
        self.module_test_loop(nick, True)


    def module_test_loop(self, nick, pm):
        num = 1
        for test in self.module_tests:
            print("\nTEST {} <{}>".format(num, test))
            try:
                result = self.actuator.command(test, nick, pm)
                print(result)

            except Exception as e:
                print("TEST FAILED! ( {} - <{}> )".format(num, test))
                print("{}\n".format(e, "\n"))
            num += 1


test = Testkit()