#Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию. 
#В программе должны быть реализованы минимум один класс, три атрибута, два метода

#Импорт библиотек
import numpy as np
import re
#Создаём класс для генератора матриц
class Generator():

    attr1 = 'Использовать тестовые данные или случайные?'

    def __init__(self, N_test, A_test):
        self.N_test = N_test
        self.A_test = A_test

    def Generate(self, choice, N_test, A_test):
    
        while True:
            if choice == '1' or choice == '2' or choice == 'q':
                break

        if choice == '1':
            N = N_test
            matrix = A_test

        if choice == '2': # Генерация случайных данных
            while True:
                N = int(input("Введите число N="))
                if N < 2:
                    print('Число N слишком малое. Введите N >= 2')
                elif N % 2 != 0:
                    print('Введите чётное число N')
                else:
                        break
        #Формируем матрицу А
                matrix = np.random.randint(-10, 10, size=(N, N))

        if choice == 'q':
            exit()

        while True:
            K = int(input("Введите число K (модуль)="))
            if K:
                break

        n = N // 2  # Размерность матриц B, C, D, E (n x n)
        Zero = np.zeros((n, n), dtype=int)
        B = matrix[:n,:n]
        C = matrix[:n,n::]
        D = matrix[n::,n::]
        E = matrix[n::,:n]
        return N, matrix, Zero, K, B, C, D, E
    
#Создаём класс для рассчётов
class ResultMatrix:
    
    def __init__(self, B, C, D, E):
        self.B = B
        self.C = C
        self.D = D
        self.E = E

    attr1 = '\nМатрица A:\n'
    attr2 = '\nМатрица B:\n'
    attr3 = '\nРанг матрицы B:\n'
    attr4 = '\nМатрица C:\n'
    attr5 = '\nРанг матрицы C:\n'
    attr6 = '\nМатрица D:\n'
    attr7 = '\nМатрица E:\n'
    attr8 = '\nРезультирующая матрица:\n'

    def Main(self, B, C, D, E, N, K, Zero):
        
        def F(x, Z, Zero):
            if x == 0:
                return np.copy(Zero)
            else:
                return np.copy(Z)
            
#Сумма элементов квадрата, составленного из главных и побочных диагоналей подматриц результирующей матрицы, по модулю K должна быть максимальной. K вводится с клавиатуры
        def Sum(x, Z):
            a = 0
            for i in Z:
                a += i%x
            return a

#заменяем подматрицы нулевыми матрицами   
        max = -11
#Ограничение: первая строка матрицы должна содержать чётное количество нулей
        if np.linalg.matrix_rank(B) % 2 != 0 or np.linalg.matrix_rank(C) % 2 != 0:
            B_copy = np.copy(Zero)
            C_copy = np.copy(Zero)
            for c in range(2):
                E_copy = F(c, E, Zero)
                for d in range(2):
                    D_copy = F(d, D, Zero)
                    Matrix = np.vstack((np.hstack((B_copy, C_copy)), np.hstack((E_copy, D_copy))))
                    sum = Sum(K, np.diag(np.flip(B_copy, axis = 1))) + Sum(K, np.diag(C_copy)) + Sum(K, np.diag(np.flip(D_copy, axis = 1))) + Sum(K, np.diag(E_copy))
                    if max < sum:
                        max = sum
                        Result = np.copy(Matrix)
        else:
            for a in range(2):
                B_copy = F(a, B, Zero)
                for b in range(2):
                    C_copy = F(b, C, Zero)
                    for c in range(2):
                        E_copy = F(c, E, Zero)
                        for d in range(2):
                            D_copy = F(d, D, Zero)
                            Matrix = np.vstack((np.hstack((B_copy, C_copy)), np.hstack((E_copy, D_copy))))
                            if len(re.findall(r'\D[0]', str(Matrix[:1,:N]))) % 2 == 0 and len(re.findall(r'\D[0]', str(Matrix[:1,:N]))) > 0:
                                sum = Sum(K, np.diag(np.flip(B_copy, axis = 1))) + Sum(K, np.diag(C_copy)) + Sum(K, np.diag(np.flip(D_copy, axis = 1))) + Sum(K, np.diag(E_copy))
                                if max < sum:
                                    max = sum
                                    Result = np.copy(Matrix)
        return Result

# Тестовые данные
N_test = 10
A_test = np.ones((N_test, N_test), dtype=int)
#Создаём экземпляры классов
matrix = Generator(N_test, A_test)
print(matrix.__class__.attr1)
choice = input('Введите 1, если хотите использовать тестовые данные, 2 - если случайные, q - для выхода из программы): ')
gen = matrix.Generate(choice, N_test, A_test)
N = gen[0]
A = gen[1]
Zero = gen[2]
K = gen[3]
B = gen[4]
C = gen[5]
D = gen[6]
E = gen[7]
Matrix = ResultMatrix(B, C, D, E)
print(Matrix.__class__.attr1, A)
print(Matrix.__class__.attr2, B)
print(Matrix.__class__.attr3, np.linalg.matrix_rank(B))
print(Matrix.__class__.attr4, C)
print(Matrix.__class__.attr5, np.linalg.matrix_rank(C))
print(Matrix.__class__.attr6, D)
print(Matrix.__class__.attr7, E)
print(Matrix.__class__.attr8, Matrix.Main(B, C, D, E, N, K, Zero))



