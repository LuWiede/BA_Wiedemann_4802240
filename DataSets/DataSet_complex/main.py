import math
from random import randrange


def generate_dataSet():
    target = 1000
    maxValue = 1000

    with open('path/to/dataSet', 'w') as fp:

        # x+y > a
        count = 0
        while count < target:
            left = randrange(maxValue * 2) - maxValue
            left1 = randrange(maxValue * 2) - maxValue
            right = randrange(maxValue * 2) - maxValue

            left_add = left + left1

            expression = str(left_add) + ">" + str(right)

            if (eval(expression)):
                count += 1
                expression_add = str("(") + str(left) + str("+") + str(left1) + str(")") + ">" + str(right)
                fp.write("\n" + expression_add)

        # x+y < a
        count = 0
        while count < target:
            left = randrange(maxValue * 2) - maxValue
            left1 = randrange(maxValue * 2) - maxValue
            right = randrange(maxValue * 2) - maxValue

            left_add = left + left1

            expression = str(left_add) + "<" + str(right)

            if (eval(expression)):
                count += 1
                expression_add = str("(") + str(left) + str("+") + str(left1) + str(")") + "<" + str(right)
                fp.write("\n" + expression_add)

        # x+y = a
        count = 0
        while count < target:
            left = randrange(maxValue * 2) - maxValue
            left1 = randrange(maxValue * 2) - maxValue

            right = left + left1

            if (eval(expression)):
                expression_add = str("(") + str(left) + str("+") + str(left1) + str(")") + "=" + str(right)
                count += 1
                fp.write("\n" + expression_add)

        # x+y > \boxed{a}
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue * 2) - maxValue

            a = randrange(maxValue * 2) - maxValue

            left = (x + y)

            expression = str(left) + ">" + str(a)

            if (eval(expression)):
                expression_add = str(x) + str("+") + str(y) + ">" + str("\\boxed{") + str(a) + str("}")
                count += 1
                fp.write("\n" + expression_add)

        # (x+y) + z < \boxed{a}
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue * 2) - maxValue

            a = randrange(maxValue * 2) - maxValue

            left = (x + y)

            expression = str(left) + "<" + str(a)

            if (eval(expression)):
                expression_add = str(x) + str("+") + str(y) + "<" + str("\\boxed{") + str(a) + str("}")
                count += 1
                fp.write("\n" + expression_add)

        # (x+y) + z = \boxed{a}
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue * 2) - maxValue

            a = (x + y)

            left = (x + y)

            expression = str(left) + "==" + str(a)

            if (eval(expression)):
                expression_add = str(x) + str("+") + str(y) + "=" + str("\\boxed{") + str(a) + str("}")
                count += 1
                fp.write("\n" + expression_add)

        # \frac{x}{y} + z > a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue * 2) - maxValue

            a = randrange(maxValue * 2) - maxValue
            if y == 0: y += 1
            if x == 0: x += 1

            left = (x / y) + z

            expression = str(left) + ">" + str(a)

            if (eval(expression)):
                expression_add = str("\\frac{") + str(x) + str("}{") + str(y) + str("}+") + str(z) + ">" + str(a)
                count += 1
                fp.write("\n" + expression_add)

        # \frac{x}{y} + z < a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue * 2) - maxValue

            a = randrange(maxValue * 2) - maxValue
            if y == 0: y += 1
            if x == 0: x += 1
            left = (x / y) + z

            expression = str(left) + "<" + str(a)

            if (eval(expression)):
                expression_add = str("\\frac{") + str(x) + str("}{") + str(y) + str("}+") + str(z) + "<" + str(a)
                count += 1
                fp.write("\n" + expression_add)

        # \frac{x}{y} + z = a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue * 2) - maxValue
            if y == 0: y += 1
            if x == 0: x += 1
            a = (x / y) + z

            expression = str(a) + "==" + str(a)
            if (eval(expression)):
                expression_add = str("\\frac{") + str(x) + str("}{") + str(y) + str("}+") + str(z) + "=" + str(a)
                count += 1
                fp.write("\n" + expression_add)

        # \sqrt{x} + z > a
        count = 0
        while count < target:
            x = randrange(maxValue)
            z = randrange(maxValue * 2) - maxValue
            left = randrange(maxValue * 2) - maxValue

            a = math.sqrt(x)+z

            expression = str(a) + ">" + str(left)

            if (eval(expression)):
                expression_add = str("\\sqrt{") + str(x) + str("}+") + str(z) + ">" + str(left)
                count += 1
                fp.write("\n" + expression_add)

        # \sqrt{x} + z < a
        count = 0
        while count < target:
            x = randrange(maxValue)
            z = randrange(maxValue * 2) - maxValue
            left = randrange(maxValue * 2) - maxValue

            a = math.sqrt(x)+z

            expression = str(a) + "<" + str(left)

            if (eval(expression)):
                expression_add = str("\\sqrt{") + str(x) + str("}+") + str(z) + "<" + str(left)
                count += 1
                fp.write("\n" + expression_add)

        # \sqrt{x} + z = a
        count = 0
        while count < target:
            x = randrange(maxValue)
            z = randrange(maxValue * 2) - maxValue

            a = math.sqrt(x)+z

            expression = str(a) + "==" + str(a)

            if (eval(expression)):
                expression_add = str("\\sqrt{") + str(x) + str("}+") + str(z) + "=" + str(a)
                count += 1
                fp.write("\n" + expression_add)

        # (x+y) \mod z > a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue)
            a = randrange(maxValue * 2) - maxValue
            if z == 0: z += 1
            left = (x+y)%z

            expression = str(left) + ">" + str(a)

            if (eval(expression)):
                expression_add = str("(") + str("(") + str(x) + str("+") + str(y) + str(") \\mod ") + str(z) + str(")") + ">" + str(a)
                count += 1
                fp.write("\n" + expression_add)

        # (x+y) \mod z < a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue)
            a = randrange(maxValue * 2) - maxValue
            if z == 0: z += 1
            left = (x+y)%z

            expression = str(left) + "<" + str(a)

            if (eval(expression)):
                expression_add = str("(") + str("(") + str(x) + str("+") + str(y) + str(") \\mod ") + str(z) + str(")") + "<" + str(a)
                count += 1
                fp.write("\n" + expression_add)

        # (x+y) \mod z = a
        count = 0
        while count < target:
            x = randrange(maxValue * 2) - maxValue
            y = randrange(maxValue * 2) - maxValue
            z = randrange(maxValue)
            if z == 0: z += 1
            left = (x+y)%z

            expression = str(left) + "==" + str(left)

            if (eval(expression)):
                expression_add = str("(") + str(x) + str("+") + str(y) + str(") \\mod ") + str(z) + str(")") + "=" + str(left)
                count += 1
                fp.write("\n" + expression_add)


if __name__ == '__main__':
    generate_dataSet()
