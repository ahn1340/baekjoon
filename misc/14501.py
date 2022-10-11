# parse data
N = int(input())

days = []
values = []
for i in range(N):
    d, v = list(map(int, input().split()))
    days.append(d)
    values.append(v)


def compute_maximum_value(days, values):
    """
    given list of days and values, compute maximum
    value one can get
    """
    memo = {}
    d_curr, d_max = len(days) - 1, len(days) - 1
    return _recursion(days, values, d_curr, d_max, memo)


def _recursion(days, values, d_curr, d_max, memo):
    """
    Recursively compute maximum value given current day
    and latest day that is free
    """
    # base case
    if d_curr == 0:
        if days[d_curr] > d_max + 1:
            memo[(d_curr, d_max)] = 0
            return 0
        else:
            memo[(d_curr, d_max)] = values[d_curr]
            return values[d_curr]
    # recursion
    else:
        # case 1. today's job can't be done
        if days[d_curr] + d_curr > d_max + 1:
            if (d_curr, d_max) in memo:
                val = memo[(d_curr, d_max)]
            else:
                val = _recursion(days, values, d_curr-1, d_max, memo)
                memo[(d_curr, d_max)] = val
                return val
        else:
            # case 2.1. do today's job
            if (d_curr-1, d_curr-1) in memo:
                val1 = memo[(d_curr-1, d_curr-1)]
            else:
                val1 = values[d_curr] + _recursion(days, values, d_curr-1, d_curr-1, memo)
                memo[(d_curr-1, d_curr-1)] = val1
            
            # case 2.2. don't do today's job
            if (d_curr-1, d_max) in memo:
                val2 = memo[(d_curr-1, d_max)]
            else:
                val2 = _recursion(days, values, d_curr-1, d_max, memo)
                memo[(d_curr-1, d_max)] = val2
            return max(val1, val2)

print(compute_maximum_value(days, values))
