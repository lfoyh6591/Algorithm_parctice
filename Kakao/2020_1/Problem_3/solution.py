def cut_matrix(matrix, x1, y1, x2, y2):
    ret = []
    for i in range(x1, x2+1):
        l = []
        for j in range(y1, y2+1):
            l.append(matrix[i][j])
        ret.append(l)
    
    return ret

def rotate(matrix, m, n):
    new_mat = [[0]*m for i in range(n)]
    for row in range(m):
        for col in range(n):
            new_mat[col][m-row-1] = matrix[row][col]
    
    return new_mat

def find_piece(lock):
    l = len(lock)
    xmin, xmax, ymin, ymax = l, 0, l, 0
    for i in range(l):
        for j in range(l):
            if lock[i][j] == 0:
                if xmin > i:
                    xmin = i
                if xmax < i:
                    xmax = i
                if ymin > j:
                    ymin = j
                if ymax < j:
                    ymax = j
    
    return xmin, ymin, xmax, ymax

def compare(key, x, y, piece, m, n):
    for i in range(m):
        for j in range(n):
            if piece[i][j] == key[x+i][y+j]:
                # print(f'x {x} y {y} i {i} j {j}')
                return False
            
    return True    

def solution(key, lock):
    l_key = len(key)
    x1, y1, x2, y2 = find_piece(lock)
    m = x2 - x1 + 1
    n = y2 - y1 + 1
    
    if (m > l_key) or (n > l_key):
        return False
    # print(f'x1 {x1} y1 {y1} x2 {x2} y2 {y2} m {m} n {n}')
    
    piece1 = cut_matrix(lock, x1, y1, x2, y2)
    piece2 = rotate(piece1, m, n)
    piece3 = rotate(piece2, n, m)
    piece4 = rotate(piece3, m, n)

    # print(piece1)
    # print(piece2)
    # print(piece3)
    # print(piece4)
    # print(key)
    
    for i in range(len(key) - m + 1):
        for j in range(len(key) - n + 1):
            if compare(key, i, j, piece1, m, n) or compare(key, i, j, piece3, m, n):
                return True
    
    for i in range(len(key) - n + 1):
        for j in range(len(key) - m + 1):
            if compare(key, i, j, piece2, n, m) or compare(key, i, j, piece4, n, m):
                return True
    
    return False