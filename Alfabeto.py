def letras():
    for i in range(ord('A'), ord('M')+1):
        yield (chr(i))

if __name__ == '__main__':

        letra = letras()
        try:
            for i in range(ord('M')):
                print(next(letra))
                if i == 'M':
                        break
        except Exception as e:
            print(e)
