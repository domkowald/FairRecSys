# create the Scipy sparse matrix representation out of a distribution file (in a data folder)

import scipy.sparse
import sys
type = 'artist'

row = []
col = []
val = []

with open('data/user_' + type + '_dist.txt') as f:
    for line in f:
        user, tracks = line.split('\t', 1)
        for t_parts in tracks[:-2].split(';'):
            track, count = t_parts.split(' ', 1)
            row.append(int(user))
            col.append(int(track))
            val.append(int(count))

print(len(row))
print(len(col))
print(len(val))
sys.stdout.flush()

sparse_matrix = scipy.sparse.coo_matrix((val, (row, col)))
print(sparse_matrix.getnnz())
sys.stdout.flush()

scipy.sparse.save_npz('data/' + type + '_matrix.npz', sparse_matrix)
test_matrix = scipy.sparse.load_npz('data/' + type + '_matrix.npz')
print(test_matrix.getnnz())
sys.stdout.flush()
