def diffWaysToCompute(expression):
    def compute(left,right,operator):
        results=[]
        for l in left:
            for r in right:
                if operator=='+':
                    results.append(l+r)
                elif operator=='-':
                    results.append(l-r)
                elif operator=='*':
                    results.append(l*r)
        return results
    if expression.isdigit():
        return [int(expression)]
    results=[]
    for i,char in enumerate(expression):
        if char in '+-*':
            left=diffWaysToCompute(expression[:i])
            right=diffWaysToCompute(expression[i+1:])
            results.extend(compute(left,right,char))
    return results
expression="2-1-1"
print("Input = ",expression)
print("Output = ",diffWaysToCompute(expression))