from enum import Enum


class QueryFilter(Enum):
    equal = 'equal'
    not_equal = 'notEqual'
    greather_than_or_equal = 'greatherThanOrEqual'
    less_than_or_equal = 'lessThanOrEqual'
    greather_than = 'greatherThan'
    less_than = 'lessThan'
    includes = 'includes'
    in_vals = 'in'
