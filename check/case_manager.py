"""
==================================================
          Check Component Case Manager
==================================================
"""

class CaseManager :

    def __init__(self):
        pass
    @staticmethod
    def invoke(case,data):
        # call case class
        return getattr(case,'execute')(data)

def call_case(case,data):

    case = __import__("cases." + case.lower() +".controller.Client", fromlist=["cases." + case.lower() +".controller"])

    CaseManager.invoke(case,data)

#driver_manager

call_case('P2P','DATADATA')