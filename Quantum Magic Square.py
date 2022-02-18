import numpy as np

## A 3x3 Quantum Magic Square Game
class MagicSquare:
    ## Arguments are Alice and Bob's Matrices and their shared entangled wavefunction
    def __init__(self, matrix1, matrix2, wavefunction):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.wavefunction = wavefunction

    ## A Getter that calculates the indexes of eigenstates
    def index_calculator(self):
        lst=[]
        lst2=[]
        for x in range(1,5):
            lst.append(x)
            for y in lst[:]:
                if(type(y)==int and y<x):
                    lst.append([y,x])
                elif(type(y)!=int):
                    lst.append([y,x])
        lst.insert(0,0)
        count=0
        for x in lst:
            count += 1
            x = str(x).replace("[","")
            x = x.replace("]","")
            lst2.insert(count,x)
        return lst2

    ## A Getter that performs the operation [A⊗B]·Ψ where A and B are
    ## Alice and Bob's matrices,⊗ is the tensor product,· is the dot product
    ## and Ψ is the wavefunction
    def play(self):        
        ## Retrieve the row number
        if((self.matrix1==A1).all()):
            row_number = 1
        elif((self.matrix1==A2).all()):
            row_number = 2
        elif((self.matrix1==A3).all()):
            row_number = 3

        ## Retrieve the column number
        if((self.matrix2==B1).all()):
            column_number = 1
        elif((self.matrix2==B2).all()):
            column_number = 2
        elif((self.matrix2==B3).all()):
            column_number = 3

        ## Print out the row and column for the game
        print("ROW: "+str(row_number)+", COLUMN: "+str(column_number))

        ## Referee performs the operation [A⊗B]·Ψ 
        d = np.dot(np.kron(self.matrix1,self.matrix2),self.wavefunction)

        ## Print out the eigenstates of [A⊗B]·Ψ 
        d = np.dot(np.kron(self.matrix1,self.matrix2),self.wavefunction)

        ## Format the eigenstates and eigenvalues for printing
        eigenvalues_list = []
        eigenstates_list = []
        for x in np.where(d!=0)[0]+1:
            eigenstates=["0","0","0","0"]
            for y in self.index_calculator()[x-1].split(","):
                if(int(y)==0):
                    pass
                else:
                    eigenstates[int(y)-1] = "1" 
            eigenstates.reverse()
            eigenstates_list.append(",".join(eigenstates))
            eigenvalues_list.append(str(np.round(d[x-1],2)))

        ## Format the final wavefunction with for printing
        final_wavefunction = ""
        for x,y in zip(eigenvalues_list,eigenstates_list):
            if("-" not in x and eigenstates_list.index(y)!=0):
                final_wavefunction += "+"+x+"*"+"|"+y.replace(",","")+">" + "\n"
            else:
                final_wavefunction += x+"*"+"|"+y.replace(",","")+">" + "\n"
        
        return "Final wavefunction:"+"\n"+final_wavefunction

# Alice's unitary matrices: A1, A2, A3  
A1 = (1/2)**(1/2)*np.array([[1j,0,0,1],[0, -1j, 1, 0],[0, 1j, 1, 0], [1, 0, 0, 1j]])
A2 = (1/2)*np.array([[1j,1,1,1j],[-1j, 1, -1, 1j],[1j, 1, -1, -1j], [-1j, 1, 1, -1j]])
A3 = (1/2)*np.array([[-1,-1,-1,1],[1, 1, -1, 1],[1, -1, 1, 1], [1, -1, -1, -1]])

# Bob's unitary matrices: B1, B2, B3
B1 = (1/2)*np.array([[1j, -1j, 1, 1],[-1j, -1j, 1, -1],[1, 1, -1j, 1j], [-1j, 1j, 1, 1]])
B2 = (1/2)*np.array([[-1, 1j, 1, 1j],[1, 1j, 1, -1j],[1, -1j, 1, 1j], [-1, -1j, 1, -1j]])
B3 = (1/2)**(1/2)*np.array([[1, 0, 0, 1],[-1, 0, 0, 1],[0, 1, 1, 0], [0, 1, -1, 0]])

## Wavefunction for a 3x3 Magic Square Game 
wavefunction = np.zeros(16)
np.put(wavefunction, [3,6,9,12],[1/2,-1/2,-1/2,1/2])

## Set Alice's matrix to A1, A2 or A3 - For rows
alice_matrix = A1

## Set Bob's matrix to B1, B2 or B3 - For columns
bob_matrix = B1

## Initiate the Magic Square
m = MagicSquare(alice_matrix,bob_matrix,wavefunction)
## Play the Magic Square
solution = m.play()
print(solution)










