    for func_dict in functions:
        for name, func in func_dict.items():
            x0 = x0_values[name]
            df = func
            # Extract the second derivative based on the function name
            d2_name = 'd2' + name
            d2f = func_dict.get(d2_name, None)
            if d2f is not None:
                x_min, iter_count, _ = method_newton(df, d2f, x0)
                print(f"Minimum for function {name}: {x_min} after {iter_count} iterations")
            else:
                print(f"Second derivative for function {name} not found.")