from functools import wraps


def greeter(func):
    def f(self):
        val = func(self)
        splited = val.split()
        disp_string = "Aloha"
        for i in splited:
            disp_string += " " + i.capitalize()
        return disp_string

    return f


def sums_of_str_elements_are_equal(func):
    def f(self):
        numbers = func(self).split()
        t = 1
        sum1 = 0
        sum2 = 0
        for i in numbers[0]:
            if i == '-':
                t = -1
                continue
            sum1 += t * int(i)
        t = 1
        for i in numbers[1]:
            if i == '-':
                t = -1
                continue
            sum2 += t * int(i)
        if sum1 == sum2:
            return str(sum1) + " == " + str(sum2)
        else:
            return str(sum1) + " != " + str(sum2)

    return f


def format_output(*required_keys):
    def f(func):
        def g(self):
            js = func(self)
            result = {}
            keys = []
            for i in required_keys:
                t = i.split("__")
                val = ""
                for elem in t:
                    try:
                        js[elem]
                    except KeyError:
                        raise ValueError()
                    if js[elem] == "":
                        val += "Empty value "
                    else:
                        val += js[elem] + " "
                result[i] = val.rstrip()
            return result

        return g

    return f


def add_method_to_instance(klass):
    def f(func):
        @wraps(func)
        def g(self):
            return func()

        setattr(klass, func.__name__, g)
        return func

    return f
