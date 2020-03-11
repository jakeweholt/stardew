def calculate_potential_harvests(days_remaining: int, days_to_grow_first_crop: int, days_to_regrow: int = 0) -> int:
    """
    Calculates the maximum number of potential left in a given month, according to the crop specifications.

    :param days_remaining: int, Days remaining in the month.
    :param days_to_grow_first_crop: int, Days required for first harvest.
    :param days_to_regrow: int, Default=0, Days required for regrowing (if crop does not regrow, then it is not required)
    :return: int, number of harvests possible, given crop specifications.
    """
    harvests = 0
    if days_to_regrow == 0:
        days_to_regrow = days_to_grow_first_crop
    if days_remaining > days_to_grow_first_crop:
        harvests += 1
        days_remaining = days_remaining - days_to_grow_first_crop
    else:
        return 0

    while days_remaining > days_to_regrow:
        harvests += 1
        days_remaining = days_remaining - days_to_regrow

    return harvests


def find_optimal_knap_sack(W: int, wt: 'list[int]', val: 'list[int]', n: int) -> (int, list):
    """
    :param W: int, Maximum weight of knap_sack (days remaining in month).
    :param wt: list[int], List of weights per item (days required per crop/value combo).
    :param val: list[int], List of values per item (value for crop/days required combo).
    :param n: int, length of either wts or val (could refactor out).
    :return: (int, list[ints]), maximum possible value, keeping weights under W, and also list of weights for reverse searching.
    """
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]

    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    # stores the result of Knapsack
    res = K[n][W]
    temp_res = res
    keepers = []
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:

            # This item is included.
            keepers.append(wt[i - 1])

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
    return (temp_res, keepers)
