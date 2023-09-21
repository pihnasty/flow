import math
import pandas as pd

betta = math.pi
class CorrelationFunctions:


#=======================================================================================================================
    def exp(tau, correlation_tau):
        return math.exp(- tau/correlation_tau)

    def exp_1_plus_tau(tau, correlation_tau):
        return math.exp(- tau/correlation_tau) * (1.0 + tau/correlation_tau)

    def exp_1_minus_tau(tau, correlation_tau):
            return math.exp(- tau/correlation_tau) * (1.0 - tau/correlation_tau)

    def exp_cos_betta_tau(tau, correlation_tau):
        return math.exp(-tau/correlation_tau) * math.cos(betta * tau)
#================= common way to calculate the fourier coefficients ====================================================
    def fourier_series_for_function_exp(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            values[n] = 2.0 * correlation_tau / (omega**2 * correlation_tau**2 + 1) * (1.0 - (-1.0) ** n * math.exp(- 1.0 / correlation_tau))
        return values

    def fourier_series_for_function_exp_1_plus_tau(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            values[n] = 4.0 * correlation_tau * (1.0 - (-1.0)**n * math.exp(-1.0 / correlation_tau) ) /  (omega * omega * correlation_tau * correlation_tau + 1) **2
            - 2.0 * (-1.0)**n * math.exp(-1.0 / correlation_tau) / (omega * omega * correlation_tau * correlation_tau + 1)
        return values

    def fourier_series_for_function_exp_1_minus_tau(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            exp_tau = math.exp(-1.0 / correlation_tau)
            temp0 = (omega**2 * correlation_tau**2 + 1)
            temp1 = 2.0 * (-1.0)**n * exp_tau / temp0 **2
            values[n] = temp1 - 2.0 * omega**2 * correlation_tau**2 * ( 2.0 * correlation_tau * (-1.0)**n * exp_tau - 2.0 * correlation_tau - (-1.0)**n *exp_tau) / temp0 ** 2
        return values
#=======================================================================================================================
    def continuous_spectrum_fourier_series_for_function_exp(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            values[n] = 2.0 * correlation_tau / (omega * omega * correlation_tau * correlation_tau + 1)
        return values

    def continuous_spectrum_fourier_series_for_function_exp_1_plus_tau(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            values[n] = 4.0 * correlation_tau / (omega**2 * correlation_tau**2 + 1) ** 2.0
        return values

    def continuous_spectrum_fourier_series_for_function_exp_1_minus_tau(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            values[n] = 4.0 * omega**2 * correlation_tau**3 / (omega**2 * correlation_tau**2 + 1)**2
        return values

    def continuous_spectrum_fourier_series_for_function_exp_cos_betta_tau(number_of_harmonics, correlation_tau):
        values = [0.0] * number_of_harmonics
        for n in range(number_of_harmonics):
            omega = math.pi * n
            alfa = 1.0 / correlation_tau
            temp1 = omega * omega + betta * betta + alfa **2
            temp2 = alfa **2 + (betta - omega) ** 2
            temp3 = alfa **2 + (betta + omega) ** 2
            values[n] = 2.0 * temp1 / (temp2 * temp3)
        return values

#=======================================================================================================================
    def fourier_series_exp(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.fourier_series_for_function_exp(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value

    def fourier_series_exp_1_plus_tau(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.fourier_series_for_function_exp_1_plus_tau(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value

    def fourier_series_exp_1_minus_tau(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.fourier_series_for_function_exp_1_minus_tau(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value
#=======================================================================================================================
    def continuous_spectrum_fourier_series_exp(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.continuous_spectrum_fourier_series_for_function_exp(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value

    def continuous_spectrum_fourier_series_exp_1_plus_tau(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.continuous_spectrum_fourier_series_for_function_exp_1_plus_tau(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value

    def continuous_spectrum_fourier_series_exp_1_minus_tau(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.continuous_spectrum_fourier_series_for_function_exp_1_minus_tau(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value

    def continuous_spectrum_fourier_series_exp_cos_betta_tau(tau, correlation_tau, number_of_harmonics):
        value = 0.0
        harmonics = CorrelationFunctions.continuous_spectrum_fourier_series_for_function_exp_cos_betta_tau(number_of_harmonics, correlation_tau)
        for n in range(number_of_harmonics):
            koef =1.0
            if (n==0):
                koef = 1.0/2.0
            value = value + koef * harmonics[n] * math.cos(math.pi * n * tau)
        return value
#================= numeric way to calculate the fourier coefficients ===================================================
    def numeric_case_fourier_series(func, number_of_harmonics):
        elements_size = len(func['time'])
        delta_tau = ( max(func['time']) - min(func['time']) ) / (elements_size -1)
        values = [0.0] * number_of_harmonics
        for num in range(number_of_harmonics):
            value = 0.0
            for n in range(elements_size):
                tau = func["time"][n]
                value = value + func["correlation"][n] * math.cos(math.pi * num * tau) * delta_tau
            values[num] = 2 * value
        return values
#=======================================================================================================================
    def get_function_value_by_function_id(type_id, tau, correlation_tau):
        if type_id == 0:
            return CorrelationFunctions.exp(tau, correlation_tau)
        if type_id == 1:
            return CorrelationFunctions.exp_1_plus_tau(tau, correlation_tau)
        if type_id == 2:
            return CorrelationFunctions.exp_1_minus_tau(tau, correlation_tau)
        if type_id == 3:
            return CorrelationFunctions.exp_cos_betta_tau(tau, correlation_tau)
        raise NameError("This type of function is not supported.")
#=======================================================================================================================
    def get_fourier_coefficients_by_function_id(type_id, number_of_harmonics, correlation_tau):
        if type_id == 0:
            return CorrelationFunctions.fourier_series_for_function_exp(number_of_harmonics, correlation_tau)
        if type_id == 1:
            return CorrelationFunctions.fourier_series_for_function_exp_1_plus_tau(number_of_harmonics, correlation_tau)
        if type_id == 2:
            return CorrelationFunctions.fourier_series_for_function_exp_1_minus_tau(number_of_harmonics, correlation_tau)
        raise NameError("This type of function is not supported.")
#================== Numeric Fourier coefficients are calculated for the interval [0;1] =================================
    def get_numeric_fourier_coefficients_by_function_id(type_id, number_of_harmonics, correlation_tau):
        size = 10000
        theory_cor_function = pd.DataFrame()
        theory_cor_function['time'] = [0.0] * size
        theory_cor_function['correlation'] = [0.0] * size
        tau_max = 1.0
        tau_min = 0.0
        delta_tau = (tau_max - tau_min) / size
        for n in range(size):
            tau = delta_tau * n
            theory_cor_function['time'][n] = tau
            theory_cor_function['correlation'][n] = CorrelationFunctions.get_function_value_by_function_id(type_id, tau, correlation_tau)
        return CorrelationFunctions.numeric_case_fourier_series(theory_cor_function, number_of_harmonics)

#================== The function values are calculated for the interval [-1;1] =========================================
    def get_function_value_by_coefficients(size, coefficients, tau_first = -1.0, tau_end = 1.0):
        delta_tau = (tau_end - tau_first) / (size - 1)
        function = pd.DataFrame()
        function['time'] = [0.0] * size
        function['flow'] = [0.0] * size

        for i_tau in range(size):
            tau = i_tau * delta_tau + tau_first
            function['time'][i_tau] = tau

            value = 0.0
            for coefficient_numer in range( len(coefficients)):
                coef = 1.0
                if (coefficient_numer==0):
                    coef = 0.5
                value = value + coef * coefficients[coefficient_numer] * math.cos(math.pi * coefficient_numer * tau)

            function['flow'][i_tau] = value

        return function
#================== The function values are calculated for the interval [-1;1] =========================================
    def get_correlation_function_value_by_coefficients(size, coefficients, tau_first = -1.0, tau_end = 1.0):
        delta_tau = (tau_end - tau_first) / (size - 1)
        correlation_function = pd.DataFrame()
        correlation_function['time'] = [0.0] * size
        correlation_function['correlation'] = [0.0] * size

        for i_tau in range(size):
            tau = i_tau * delta_tau +  tau_first
            correlation_function['time'][i_tau] = tau

            value = 0.0
            for coefficient_numer in range( len(coefficients)):
                if (coefficient_numer==0):
                    a_a =  coefficients[coefficient_numer]**2 /4
                else:
                    a_a =  coefficients[coefficient_numer]**2 / 2.0
                value = value + a_a * math.cos(math.pi * coefficient_numer * tau)
            correlation_function['correlation'][i_tau] = value
        return correlation_function