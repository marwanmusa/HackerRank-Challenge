def solve(meal_cost, tip_percent, tax_percent):
    """
    Task:
    Given the meal price (base cost of a meal),
    tip percent (the percentage of the meal price being added as tip),
    and tax percent (the percentage of the meal price being added as tax) for a meal,
    find and print the meal's total cost. Round the result to the nearest integer.

    Function Description:
    Complete the solve function in the editor below.

    solve has the following parameters:
        - int meal_cost: the cost of food before tip and tax
        - int tip_percent: the tip percentage
        - int tax_percent: the tax percentage
    Returns The function returns nothing.
    Print the calculated value, rounded to the nearest integer.

    Args:
        meal_cost (_type_): _description_
        tip_percent (_type_): _description_
        tax_percent (_type_): _description_
    """
    tip = (tip_percent * meal_cost)/100
    tax = (tax_percent * meal_cost)/100
    total_cost = round(meal_cost + tip + tax)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
