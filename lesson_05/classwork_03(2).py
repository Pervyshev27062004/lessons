def sum_and_max(*args):
    mv_sum = 0
    mv_min = args[0]
    if len(args):
        for element in args:
            mv_sum += element
            if element < mv_min:
                mv_min = element
        return mv_sum, mv_min