from scipy import sparse

def make_A_3D(k):
    """Create the matrix for the temperature problem on a k-by-k-by-k grid.
    Parameters: 
      k: number of grid points in each dimension.
    Outputs:
      A: the sparse k**3-by-k**3 matrix representing the finite difference approximation to Poisson's equation.
    """
    # First make a list with one triple (row, column, value) for each nonzero element of A
    triples = []
    # Set up the nested loops
    for i in range(k):
        for z in range(k):
            for j in range(k):
            # what row of the matrix is grid point (i,j,k)?
                row = (j + z*k*k + i*k)# ???

                # the diagonal element in this row
                triples.append((row, row, 6.0))
                # connect to left grid neighbor
                if j > 0:
                    triples.append((row, row - 1, -1.0))
                # ... right neighbor
                if j < k - 1:
                    triples.append((row, row + 1, -1.0))

                # ... neighbor above
                if i > 0:
                    triples.append((row, row - k, -1.0))

                # ... neighbor below
                if i < k - 1:
                    triples.append((row, row + k, -1.0))

                # ... neighbor up
                if z > 0:
                    triples.append((row, row - k*k, -1.0))

                # ... neighbor down
                if z < k - 1:
                    triples.append((row, row + k*k, -1.0))


    
    # Finally convert the list of triples to a scipy sparse matrix
    ndim = k*k*k
    rownum = [t[0] for t in triples]
    colnum = [t[1] for t in triples]
    values = [t[2] for t in triples]
    A = sparse.csr_matrix((values, (rownum, colnum)), shape = (ndim, ndim))
    
    return A 