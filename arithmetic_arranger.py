def arithmetic_arranger(*argv):
    # Error handling
    if len(argv[0]) > 5:
        return 'Error: Too many problems.'
    else: 
        pass
    
    summands_1 = ''
    summands_2 = ''
    equals_ = ''
    answers = ''
    
    for i, problem in enumerate(argv[0]):
        summand1 = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        summand2 = problem.split(' ')[2]
        
        # Error handling
        if operator == '+' or operator == '-':
            pass
        else:
            return "Error: Operator must be '+' or '-'." 
        
        # Error handling
        if not summand1.isdigit() or not summand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        else: 
            ans = str(eval(problem))
        
        # Error handling
        if len(summand1) > 4 or len(summand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        else:            
            pass
        
        # Formatting
        if len(summand1) > len(summand2):
            ## the ' ' * 2 accounts for the space and the operator
            summand1 = ' ' * 2 + summand1  
            summand2 = operator + ' ' * (len(summand1) - len(summand2) - 1) + summand2
            equals = '-' * len(summand1)   
            ans = ' ' * (len(summand2) - len(ans)) + ans
            
        elif len(summand1) <= len(summand2):
            ## the ' ' * 2 accounts for the space and the operator
            summand2 = operator + ' ' + summand2 
            summand1 = ' ' * (len(summand2) - len(summand1)) + summand1
            equals = '-' * len(summand2)
            ans = ' ' * (len(summand2) - len(ans)) + ans
        
        # Formats the results
        if i != len(argv[0]) - 1:
            summands_1 += summand1 + ' ' * 4
            summands_2 += summand2 + ' ' * 4
            equals_ += equals + ' ' * 4
            answers += ans + ' ' * 4
        else:
            summands_1 += summand1
            summands_2 += summand2
            equals_ += equals
            answers += ans
        
    arranged_problems1 = summands_1 + '\n' + summands_2 + '\n' + equals_ + '\n' + answers
    arranged_problems2 = summands_1 + '\n' + summands_2 + '\n' + equals_
    
    if len(argv) == 1:
        return arranged_problems2
    if len(argv) > 1:
        if argv[1] == True:
            return arranged_problems1
        else:
            return arranged_problems2