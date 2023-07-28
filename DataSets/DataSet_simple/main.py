from random import randrange


def generate_dataSet():
    target = 1000
    count = 0
    maxValue = 1000

    with open('path/to/dataSet', 'w') as fp:
        #   >
        while count < target:
            left = randrange(maxValue*2)-maxValue
            right = randrange(maxValue*2)-maxValue

            expression = str(left)+">"+str(right)
            if (eval(expression)):
                count += 1
                print(expression)
                fp.write("\n" + expression)

        #   <
        count = 0
        while count < target:
            left = randrange(maxValue * 2) - maxValue
            right = randrange(maxValue * 2) - maxValue

            expression = str(left) + "<" + str(right)
            if (eval(expression)):
                count += 1
                fp.write("\n" + expression)

        #   =
        count = 0
        while count < target:
            left = randrange(maxValue * 2) - maxValue

            expression = str(left) + "=" + str(left)
            count += 1
            fp.write("\n" + expression)


if __name__ == '__main__':
    generate_dataSet()

