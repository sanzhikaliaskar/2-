with open('level1.txt', 'w') as f:
        for i in range(0, 650, 25):
            for j in range(0, 1050 , 25):
                f.write('*')
            f.write('\n')
