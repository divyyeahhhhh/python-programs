def pascal_tri(numRows):
    '''Print Pascal's triangle with numRows.'''
    if numRows == 1:
        return [[1]] # base case is reached!
    else:
        res_arr = pascal_tri(numRows-1) # recursive call to pascal_tri
        # use previous row to calculate current row 
        cur_row = [1] # every row starts with 1
        prev_row = res_arr[-1] 
        for i in range(len(prev_row)-1):
            # sum of 2 entries directly above
            cur_row.append(prev_row[i] + prev_row[i+1]) 
        cur_row += [1] # every row ends with 1
        res_arr.append(cur_row)
        return res_arr
      tri_array = pascal_tri(5)
      for i,row in enumerate(tri_array):
  for j in range(len(tri_array) - i + 1):
    print(end=" ") # leading spaces
  for j in row:
    print(j, end=" ") # print entries
  print("\n")  # print new line
