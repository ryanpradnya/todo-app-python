class QueryFilterDTO:
    def __init__(self, key: str, criteria: str, val: any):
        self.key = key
        self.criteria = criteria
        self.val = val
