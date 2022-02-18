# 3x3-Quantum-Magic-Square
Implementation of the 3x3 Quantum Magic Square winning strategy outlined by (Brassard, G., Broadbent, A., &amp; Tapp, A., 2005)

A Magic square is a 3x3 matrix which is to be filled by two players, Alice and Bob. A referee observes the moves of the players and enforces the rules. The rules are:

    Alice fills the rows with 0's and 1's such that the entries for each row adds up to an even number. 

    Bob fills the columns with 0's and 1's such that the entries for each column adds up to an odd number.

If the shared elements of their entries are equal, then they score a point.

Below is an example of a winning strategy for row 2, column 3:

<img src="https://user-images.githubusercontent.com/63025867/154600734-c540c71e-de80-4ea6-9f50-ddaf505b4c57.png" align="center" height="80" width="500">

    Alice's entries (the row) add up to 0+0+0=0, which is an even number.
    
    Bob's entries (the column) add up to 0+0+1, which is an odd number.
    
    Their shared element (highlighted in red) is the same.
    

 Using classical methods, the highest Alice and Bob can score for a 3x3 Magic Square game is 8/9.

 (Brassard, G., Broadbent, A., &amp; Tapp, A., 2005) showed that they can score 9/9 if they share an entangled wavefunction and use quantum algorithms.
 
 The method is as follows:
 
    Alice has three 4x4 unitary matrices, one for each row: A1, A2, A3.
    
    Bob has three 4x4 unitary matrices, one for each column: B1, B2, B3.
    
    They share an entangled wavefunction ψ.
    
    For each game, they hand their matrices for the given row and column to the referee. 
    Then, the referee performs the following operation:

  <img src="https://user-images.githubusercontent.com/63025867/154602361-b10f6ec7-8a61-486d-8f8f-7bab1cd0d9ef.png" height="20" width="600">
    
   where ⨂ is the tensor product, ⋅ is the dot product and ψ is the wavefunction.
   
 This method combined with the strategy for using the resulting wavefunction described by (Brassard, G., Broadbent, A., &amp; Tapp, A., 2005) on page 22 works, but the calculation is cumbersome.
   
 Using this code, one can verify the method for all plays (i.e. rows and columns) of the 3x3 Magic Square game. 
 
 In order to perform the calculations required for each play, simple change the arguments of the variables:
    
    alice_matrix
    
 and
 
    bob_matrix
 
 to any of the matrices of Alice (A1, A2, A3) and Bob (B1, B2, B3) and observe the resulting wavefunction.

