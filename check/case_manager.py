from check.cases import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class CaseManager :
    @staticmethod
    def invoke(case,data):
        # call case classa
        print("case",case)
        print("data",data)
        return getattr(case,'execute')(data)


def call_case(case,data):
    casemodule = __import__("cases." + case.lower() +".controller",
                      fromlist=["cases." + case.lower() +".controller"])
    print("casemodule",casemodule)
    CaseManager.invoke(casemodule.Client(),data)


