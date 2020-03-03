def one(input1, input2):
	if len(input1) == len(input2):
		return input1 + " " + input2
	if len(input1) > len(input2):
		return input1
	if len(input2) > len(input1):	
		return input2


def two(input):
    input = input.lower()
    l = input.split("bert")
    if len(l) % 2 == 0:
        return ""
    else:
        return "".join(l[(int(len(l)/2))])


def three(arg1):
    if arg1 % 3 == 0 and arg1 % 5 == 0:
        return "fizzbuzz"  
    if arg1 % 3 == 0:
        return "fizz"
    if arg1 % 5 == 0:
        return "buzz" 
    else:
        return "null"


def four(arg1):
	b = []
	x = []
	lk = []
	arg1 = arg1.split()
	for i in arg1:
		count = 0
		for c in i:
			count = count + int(c)
			lk.append(count)
	return max(lk)


def five(input):
    l1 = input.split(",")
    l2 = []
    i = 2
    while i < len(l1):
        if l1[i] == 'False':
            l2.append(l1[i-2])
            i = i + 4
        else:
            i = i + 4
    return list(dict.fromkeys(l2))


def six(input):
	import re
	a = len(re.findall("cei", input))
	b = len(re.findall("ie", input))
	c = len(re.findall("cie", input))
	if c > 0:
		return False
	if a > 0:
		return True
	if b > 0:
		return True
	else:
		return False



def seven(input):
	input = input.lower()
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0
	for i in input:
		if i in vowels:
			count = count + 1
	return count


def eight(input):
	n = input
	var_total = 1
	while n > 0:
		a = n
		var_total = var_total*a
		n = n-1
	return var_total



def nine(inputString, char):
    inputString = inputString.replace(" ", "")
    inde = inputString.find(char)
    if char in inputString:
        return inde + 1
    else:
        return inde

 
def ten(string, int, char):
	string = string.lower()
	findin = string.index(char) + 1
	if findin == int:
		return True
	else:
		return False
