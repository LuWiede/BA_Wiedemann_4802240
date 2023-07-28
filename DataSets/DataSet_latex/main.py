import math
from random import randrange


def generate_dataSet():
    target = 1000
    count = 0
    maxValue = 1000

    with open('path/to/dataSet', 'w') as fp:
        #  \boxed{} =
        while count < target:
            left = randrange(maxValue * 2) - maxValue

            expression = str("\\boxed{") + str(left) + str("}") + "=" + str(left)
            count += 1
            fp.write("\n" + expression)

        # \boxed{} <
        count = 0
        while count < target:
            left = randrange(maxValue * 2) - maxValue
            right = randrange(maxValue * 2) - maxValue

            expression = str(left) + "<" + str(right)

            if (eval(expression)):
                expression_boxed = str("\\boxed{") + str(left) + str("}") + "<" + str(right)
                count += 1
                fp.write("\n" + expression_boxed)

        # \boxed >
        count = 0
        while count < target:
            left = randrange(maxValue*2)-maxValue
            right = randrange(maxValue*2)-maxValue

            expression = str(left)+">"+str(right)
            if (eval(expression)):
                count += 1
                expression_boxed = str("\\boxed{") + str(left) + str("}") + ">" + str(right)
                fp.write("\n" + expression_boxed)

        # \frac =
        count = 0
        while count < target:
            left = (randrange(maxValue * 2) - maxValue)
            right = (randrange(maxValue * 2) - maxValue)
            if (left == 0):
                left = left + 1
            if (right == 0):
                right = right + 1

            count += 1
            expression = str("\\frac{") + str(left) + str("}") + str("{") + str(right) + str("}") + \
                              "=" + str(left) + str("/") + str(right)
            fp.write("\n" + expression)

        # \frac \frac =
        count = 0
        while count < target:
            left = (randrange(maxValue * 2) - maxValue)
            right = (randrange(maxValue * 2) - maxValue)

            if (left == 0):
                left = left + 1
            if (right == 0):
                right = right + 1

            count += 1
            expression = str("\\frac{") + str(left) + str("}") + str("{") + str(right) + str("}") + \
                             "=" + str("\\frac{") + str(left) + str("}") + str("{") + str(right) + str("}")
            fp.write("\n" + expression)

        # \frac <
        count = 0
        while count < target:
            left = (randrange(maxValue * 2) - maxValue)
            left1 = (randrange(maxValue * 2) - maxValue)
            right = (randrange(maxValue * 2) - maxValue)
            right1 = (randrange(maxValue * 2) - maxValue)

            if (left == 0):
                left = left + 1
            if (left1 == 0):
                left1 = left1 + 1
            if (right == 0):
                right = right + 1
            if (right1 == 0):
                right1 = right1 + 1

            expression = str(left) + "//" + str(left1) + "<" + str(right) + "//" + str(right1)

            if (eval(expression)):
                expression_frac = str("\\frac{") + str(left) + str("}") + str("{") + str(left1) + str("}") + \
                                  "<" + str(right) + str("/") + str(right1)
                count += 1
                fp.write("\n" + expression_frac)

        # \frac \frac <
        count = 0
        while count < target:
            left = (randrange(maxValue * 2) - maxValue)
            left1 = (randrange(maxValue * 2) - maxValue)
            right = (randrange(maxValue * 2) - maxValue)
            right1 = (randrange(maxValue * 2) - maxValue)

            if (left == 0):left = left + 1
            if (left1 == 0): left1 = left1 + 1
            if (right == 0): right = right + 1
            if (right1 == 0): right1 = right1 + 1

            expression = str(left) + "//" + str(left1) + "<" + str(right) + "//" + str(right1)

            if (eval(expression)):
                expression_frac = str("\\frac{") + str(left) + str("}") + str("{") + str(left1) + str("}") + \
                                 "<" + str("\\frac{") + str(right) + str("}") + str("{") + str(right1) + str("}")
                count += 1
                fp.write("\n" + expression_frac)

        # \frac >
        count = 0
        while count < target:
            left = (randrange(maxValue * 2) - maxValue)
            left1 = (randrange(maxValue * 2) - maxValue)
            right = (randrange(maxValue * 2) - maxValue)
            right1 = (randrange(maxValue * 2) - maxValue)

            if (left == 0): left = left + 1
            if (left1 == 0): left1 = left1 + 1
            if (right == 0): right = right + 1
            if (right1 == 0): right1 = right1 + 1

            expression = str(left) + "//" + str(left1) + ">" + str(right) + "//" + str(right1)
            if (eval(expression)):
                count += 1
                expression_frac = str("\\frac{") + str(left) + str("}") + str("{") + str(left1) + str("}") + \
                                       ">" + str(right) + str("/") + str(right1)
                fp.write("\n" + expression_frac)

        # \frac \frac >
        count = 0
        while count < target:
            left = (randrange(maxValue * 2) - maxValue)
            left1 = (randrange(maxValue * 2) - maxValue)
            right = (randrange(maxValue * 2) - maxValue)
            right1 = (randrange(maxValue * 2) - maxValue)

            if (left == 0):
                left = left + 1
            if (left1 == 0):
                left1 = left1 + 1
            if (right == 0):
                right = right + 1
            if (right1 == 0):
                right1 = right1 + 1

            expression = str(left) + "//" + str(left1) + ">" + str(right) + "//" + str(right1)
            if (eval(expression)):
                count += 1
                expression_frac = str("\\frac{") + str(left) + str("}") + str("{") + str(left1) + str("}") + \
                                  ">" + str("\\frac{") + str(right) + str("}") + str("{") + str(right1) + str("}")
                fp.write("\n" + expression_frac)

        # \sqrt =
        count = 0
        while count < target:
            left = randrange(maxValue)
            expression = str("\\sqrt{") + str(left) + str("}") + "=" + str(math.sqrt(left))
            count += 1
            fp.write("\n" + expression)

        # \sqrt <
        count = 0
        while count < target:
            left = randrange(maxValue)
            right = randrange(maxValue)

            expression = str(math.sqrt(left)) + "<" + str(math.sqrt(right))

            if (eval(expression)):
                expression_sqrt = str("\\sqrt{") + str(left) + str("}") + "<" + str(round(math.sqrt(right)))
                count += 1
                fp.write("\n" + expression_sqrt)

        # \sqrt >
        count = 0
        while count < target:
            left = randrange(maxValue)
            right = randrange(maxValue)

            expression = str(math.sqrt(left)) + ">" + str(math.sqrt(right))
            if (eval(expression)):
                count += 1
                expression_sqrt = str("\\sqrt{") + str(left) + str("}") + ">" + str(round(math.sqrt(right)))
                fp.write("\n" + expression_sqrt)
        '''
        # ** =
        count = 0
        maxValue1 = 10
        while count < target:
            left = randrange(maxValue1 * 2)
            right = randrange(maxValue1 * 2)

            expression = str(left) + str("^") + str(right) + "=" + str(left ** right)
            count += 1
            fp.write("\n" + expression)

        # x^y < a^b
        count = 0
        maxValue1 = 10
        while count < target:
            x = randrange(maxValue1 * 2)
            y = randrange(maxValue1 * 2)
            a = randrange(maxValue1 * 2)
            b = randrange(maxValue1 * 2)

            expression = str(x ** y) + "<" + str(a ** b)
            if (eval(expression)):
                count += 1
                expression_pot = str(x) + str("^") + str(y) + "<" + str(a) + str("^") + str(b)
                fp.write("\n" + expression_pot)

        # x^y > a^b
        count = 0
        maxValue1 = 10
        while count < target:
            x = randrange(maxValue1 * 2)
            y = randrange(maxValue1 * 2)
            a = randrange(maxValue1 * 2)
            b = randrange(maxValue1 * 2)

            expression = str(x ** y) + ">" + str(a ** b)
            if (eval(expression)):
                count += 1
                expression_pot = str(x) + str("^") + str(y) + ">" + str(a) + str("^") + str(b)
                fp.write("\n" + expression_pot)
                
        '''
       # x  mod y  = z
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue)

            z = (x % y)
            if(y == 0): y+= 1

            expression = str("(") + str(x) + str("\\mod ") + str(y) + str(")") + "=" + str(z)
            count += 1
            fp.write("\n" + expression)

       # (x % y) < a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2)
            a = randrange(maxValue * 2) - maxValue

            if(y == 0): y += 1
            z = x % y

            expression = str(z) + "<" + str(a)

            if (eval(expression)):
                expression_mod = str("(") + str(x) + str("\\mod ") + str(y) + str(")") + "<" + str(a)
                count += 1
                fp.write("\n" + expression_mod)

      # (x % y) > a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2)
            a = randrange(maxValue * 2) - maxValue

            if(y == 0): y += 1
            z = x % y

            expression = str(z) + ">" + str(a)

            if (eval(expression)):
                expression_mod = str("(") + str(x) + str("\\mod ") + str(y) + str(")") + ">" + str(a)
                count += 1
                fp.write("\n" + expression_mod)


if __name__ == '__main__':
    generate_dataSet()
