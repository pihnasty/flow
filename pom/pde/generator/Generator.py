class Generator:

    def __init__(self, start_value, finish_value, func_r0, func_rk, eps):
        self.start_value = start_value
        self.finish_value = finish_value
        self.func_r0 = func_r0
        self.func_rk = func_rk
        self.eps = eps

    # def distribution_density(self):
    #     func = lambda x: self.func_rk[i](x)
    #     return func

    def integral(self, start_value, finish_value, func):
        sum = 0.0
        value = start_value
        while value < finish_value:
            sum = func(value) * self.eps
            value += self.eps
        return sum

    @staticmethod
    def functions_sum(functions):
        return lambda x: sum(function(x) for function in functions)
