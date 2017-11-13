import subprocess
from termcolor import cprint


class TestSummaryParser:
    def parse(self, summary):
        return [
            self.__parseAllTests(summary),
            self.__parseSuccessTests(summary),
            self.__parseFailedTests(summary),
            self.__parseFailedTestsCallstacks(summary)
        ]

    def __parseAllTests(self, summary):
        allTestsStrBegin = "Łączna liczba testów: "
        allTestsStrEnd = ". Zakończone pomyślnie:"

        allTestsStartIndex = summary.find(allTestsStrBegin)
        allTestsEndIndex = summary.find(allTestsStrEnd)

        allTestsSummary = summary[allTestsStartIndex:allTestsEndIndex]

        return allTestsSummary

    def __parseSuccessTests(self, summary):
        successTestsStrBegin = "Zakończone pomyślnie: "
        successTestsStrEnd = ". Zakończone niepowodzeniem:"

        successTestsStartIndex = summary.find(successTestsStrBegin)
        successTestsEndIndex = summary.find(successTestsStrEnd)

        successTestsSummary = summary[successTestsStartIndex:successTestsEndIndex]

        return successTestsSummary

    def __parseFailedTests(self, summary):
        failTestsStrBegin = ". Zakończone niepowodzeniem: "
        failTestsStrEnd = ". Pominięte:"

        failTestsStartIndex = summary.find(failTestsStrBegin) + 2
        failTestsEndIndex = summary.find(failTestsStrEnd)

        failTestsSummary = summary[failTestsStartIndex:failTestsEndIndex]

        return failTestsSummary

    def __parseFailedTestsCallstacks(self, summary):
        failTestsCallstacksStrBegin = "Zakończone niepowodzeniem: "
        failTestsCallstacksStrEnd = "Łączna liczba testów: "

        failTestsCallstackStartIndex = summary.find(
            failTestsCallstacksStrBegin)
        failTestsCallstackEndIndex = summary.find(failTestsCallstacksStrEnd)

        failTestsCallstackSummary = summary[failTestsCallstackStartIndex:failTestsCallstackEndIndex]

        return failTestsCallstackSummary


class TestSummaryPrinter:
    allTests = 0

    succeedTests = 0

    failedTests = 0

    failedTestsCallstacks = ""

    def addResults(self, results):
        allTestsSplit = str.split(results[0], sep=": ")
        allTestsLocal = int(allTestsSplit[1])
        self.allTests += allTestsLocal

        succeedTestsSplit = str.split(results[1], sep=": ")
        succeedTestsLocal = int(succeedTestsSplit[1])
        self.succeedTests += succeedTestsLocal

        failedTestsSplit = str.split(results[2], sep=": ")
        failedTestsLocal = int(failedTestsSplit[1])
        self.failedTests += failedTestsLocal

        self.failedTestsCallstacks += results[3]
        return

    def printAll(self):
        print("All tests: " + str(self.allTests))
        cprint("Succeed tests: " +
               str(self.succeedTests), 'green')
        cprint("Failed tests: " +
               str(self.failedTests), 'red')
        self.__printFailedTestsCallstacks()
        return

    def __printFailedTestsCallstacks(self):
        retval = ''
        for char in str(self.failedTestsCallstacks):
            retval += char if not char == '\n' else ''
            if char == '\n':
                cprint(retval, 'red')
                retval = ''
        if retval:
            return


proc = subprocess.Popen('dotnet', stdout=subprocess.PIPE)
tmp = str(proc.communicate()[0])

success = r"""Łączna liczba testów: 1. Zakończone pomyślnie: 1. Zakończone niepowodzeniem: 0. Pominięte: 0.
Pomyślne uruchomienie testu.
Czas wykonywania testu: 1,2975 Sekundy."""

fail = r"""Zakończone niepowodzeniem: TestLib2.UnitTest1.Test2
Komunikat o błędzie:
 Assert.True() Failure
Expected: True
Actual:   False
Ślad stosu:
   at TestLib2.UnitTest1.Test2() in c:\Users\luka-hyli\Documents\Visual Studio Code\RetryOperations\TestLib2\UnitTest2.cs:line 11
Zakończone niepowodzeniem: TestLib2.UnitTest1.Test3
Komunikat o błędzie:
 Assert.True() Failure
Expected: True
Actual:   False
Ślad stosu:
   at TestLib2.UnitTest1.Test3() in c:\Users\luka-hyli\Documents\Visual Studio Code\RetryOperations\TestLib2\UnitTest2.cs:line 17
Zakończone niepowodzeniem: TestLib2.UnitTest1.Test4
Komunikat o błędzie:
 Assert.True() Failure
Expected: True
Actual:   False
Ślad stosu:
   at TestLib2.UnitTest1.AssertMethod() in c:\Users\luka-hyli\Documents\Visual Studio Code\RetryOperations\TestLib2\UnitTest2.cs:line 28
   at TestLib2.UnitTest1.Test4() in c:\Users\luka-hyli\Documents\Visual Studio Code\RetryOperations\TestLib2\UnitTest2.cs:line 23

Łączna liczba testów: 3. Zakończone pomyślnie: 0. Zakończone niepowodzeniem: 3. Pominięte: 0."""

parser = TestSummaryParser()
printer = TestSummaryPrinter()

summaries = parser.parse(fail)
summaries2 = parser.parse(success)

printer.addResults(summaries)
printer.addResults(summaries2)
printer.printAll()


# for item in summaries:
#     print(item)


# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
