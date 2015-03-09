class Fibonacci():

    # calculate the xth fibonacci value where x = number. Number is in the range[0, 1000]
    def fibonacciNum(self, number):
        if number < 1:
            return -1
        if 1 == number:
            return 0
        elif 2 == number:
            return 1
        a = 0
        b = 1
        sn = 0
        for i in range(0, number -2):
            sn = a + b
            a = b
            b = sn
        return sn

    # calculate Finonacci and save the file
    def calculateFibonacci(self, MAX_NUMBER = 1000):
        if MAX_NUMBER < 1:
            return -1
        try:
            fib = Fibonacci()
            fw = open('fibonacciABC.txt','w')

            buf = []
            for i in range(1, MAX_NUMBER):
                buf.append(str(fib.fibonacciNum(i)))
            fibonacciString = '\n'.join(buf)
            fw.write(fibonacciString)
            fw.close()
        except IOError as err:
            print('File Error:'+str(err))



    # read the fibonacci string from file 'fibonacciABC.txt'
    def responseFibonacci(self, num):
        fw = open('fibonacciABC.txt','r')
        buf = []
        for i in range(1, num+1):
            buf.append(fw.readline().strip('\n'))
        fibonacciString = ' '.join(buf)
        fw.close()
        return fibonacciString