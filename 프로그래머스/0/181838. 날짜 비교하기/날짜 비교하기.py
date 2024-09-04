def compare_years(date1, date2):
    if date1[0] < date2[0]:
        return 1
    
    elif date1[0] > date2[0]:
        return 0
    
    else:
        return compare_months(date1, date2)

def compare_months(date1, date2):
    if date1[1] < date2[1]:
        return 1
    
    elif date1[1] > date2[1]:
        return 0
    
    else:
        return compare_days(date1, date2)

def compare_days(date1, date2):
    if date1[2] < date2[2]:
        return 1
    
    elif date1[2] > date2[2]:
        return 0
    
    else:
        return 0

def print_comparison_step(step, value1, value2, result):
    comparison = "less than" if value1 < value2 else "greater than or equal to"
    print(f"{step} comparison: {value1} is {comparison} {value2}, result: {result}")

def detailed_compare_years(date1, date2):
    result = compare_years(date1, date2)
    print_comparison_step("Year", date1[0], date2[0], result)
    
    return result

def detailed_compare_months(date1, date2):
    result = compare_months(date1, date2)
    print_comparison_step("Month", date1[1], date2[1], result)
    
    return result

def detailed_compare_days(date1, date2):
    result = compare_days(date1, date2)
    print_comparison_step("Day", date1[2], date2[2], result)
    
    return result

def detailed_solution(date1, date2):
    result = detailed_compare_years(date1, date2)
    
    if date1[0] == date2[0]:
        result = detailed_compare_months(date1, date2)
        
        if date1[1] == date2[1]:
            result = detailed_compare_days(date1, date2)
    
    return result

def solution(date1, date2):
    #comparing days start!
    return detailed_solution(date1, date2)