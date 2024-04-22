BLACK = '30m'
RED = '31m'
GREEN = '32m'
YELLOW = '33m'
BLUE = '34m'
MAGENTA= '35m'
CYAN= '36m'
GRAY = '37m'
IRED = '41m'
IGREEN = '42m'
IYELLOW = '43m'
IBLUE = '44m'
IMAGENTA= '45m'
ICYAN= '46m'
IGRAY = '47m'
BLANK = 0

def style(n, color):
    text = str(n)
    colored_text = f"\033[{color}{text}\033[00m"
    bold_text = "\033[1m" + colored_text + "\033[0m"
    return bold_text

def showlist(lst, i, j, color):
    if color == BLANK:
        for k in range(i,j):
            print(" ",end=" ")
    else:
        for k in range(i,j):
            print(str(style(lst[k], color)), end=" ")           
        
def showindex(letter,i, color):
    for k in range(0,i):
        print(" ", end=" ")
    print(style(letter, color))
    
def showletter(letter,color):
    print(style(letter, color), end=" ")
    
def showblank():
    print(" ", end=" ")
    
def anewline():
    print("")
    
def find(lst, elm):
    idx = 0
    while idx < len(lst) and lst[idx] != elm:
        idx = idx+1
    return idx
def show_find(lst, elm):
    idx = 0
    showlist([elm],0,1,YELLOW)
    anewline()
    while idx < len(lst) and lst[idx] != elm:
        showlist(lst,0,idx,GRAY)
        showlist(lst,idx,idx+1,IYELLOW)
        showlist(lst,idx+1,len(lst),BLUE)
        anewline()
        idx = idx+1
    if idx < len(lst):
        showlist(lst,0,idx,GRAY)
        showlist(lst,idx,idx+1,IYELLOW)
        showlist(lst,idx+1,len(lst),BLUE)
        anewline()
        showindex('^',idx,IGREEN)
        anewline()
    else:
        showlist(lst,0,idx,GRAY)
        anewline()   
        showindex('X',idx,IRED)
        anewline()
    return idx

def insert(lst,idx):
    elm = lst[idx]
    while idx > 0 and lst[idx-1] > elm:
        lst[idx] = lst[idx-1]
        idx      = idx-1
    lst[idx] = elm

def insertion_sort(lst):
    for idx in range(0, len(lst)):
        insert(lst,idx)
        
def show_insert(lst,idx):
    showlist(lst,0,idx,GREEN)
    showlist(lst,idx,idx+1,IYELLOW)
    showlist(lst,idx+1,len(lst),GRAY)
    anewline()
    oldidx = idx
    elm = lst[idx]
    if idx > 0:
        showlist(lst,0,idx-1,GREEN)
        showlist(lst,idx-1,idx,IYELLOW)
    showlist([" "],0,1,GRAY)
    showlist(lst,idx+1,len(lst),GRAY)
    anewline()
    while idx > 0 and lst[idx-1] > elm:
        lst[idx] = lst[idx-1]
        idx      = idx-1
        if idx > 0:
            showlist(lst,0,idx-1,GREEN)
            showlist(lst,idx-1,idx,IYELLOW)
        showlist([" "],0,1,GRAY)
        showlist(lst,idx+1,oldidx+1, YELLOW)
        showlist(lst, oldidx+1,len(lst),GRAY)
        anewline()
    lst[idx] = elm
    if idx > 0:
        showlist(lst,0,idx-1,GREEN)
        showlist(lst,idx-1,oldidx+1,YELLOW)
    else:
        showlist(lst,idx,oldidx+1,YELLOW)
    showlist(lst,oldidx+1,len(lst),GRAY)
    anewline()
    
def insert_with_res(lst,idx):
    elm = lst[idx]
    while idx > 0 and lst[idx-1] > elm:
        lst[idx] = lst[idx-1]
        idx      = idx-1
    lst[idx] = elm
    return idx
    
def show_insertion_sort(lst):
    showlist(lst, 0, len(lst), BLUE)
    anewline()
    res=0
    for idx in range(0, len(lst)):
        showlist(lst, 0, res, GREEN)
        showlist(lst, res, idx, YELLOW)
        if idx < len(lst):
            showlist(lst,idx,idx+1,IYELLOW)
            showlist(lst,idx+1,len(lst), GRAY)
        res=insert_with_res(lst,idx)
        anewline()
    showlist(lst, 0, len(lst), GREEN)
        
def show_detailed_insertion_sort(lst):
    showlist(lst, 0, len(lst), BLUE)
    anewline()
    for idx in range(0, len(lst)):
        show_insert(lst,idx)
        anewline()    
        if idx < len(lst):
            showlist(lst, 0, idx+1, GREEN)
            showlist(lst,idx+1,len(lst), BLUE)
        anewline()
        
def simple_quicksort(lst):
    if lst==[]:
        return []
    else:
        pivot   = lst[0]
        lesser  = simple_quicksort([x for x in lst[1:] if x < pivot])
        greater = simple_quicksort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater 
    
def show_simple_quicksort(lst):
    simple_quicksort_aux(lst,0,len(lst),lst)
    
def simple_quicksort_aux(lst, l, r, full):
    if lst==[]:
        return []
    elif len(lst) == 1:
        showlist(full,0,l,BLANK)
        showletter(lst[0],IGREEN)
        anewline()
        return(lst)
    else:
        showlist(full,0,l,BLANK)
        showlist(lst,0,1,IYELLOW)
        if l<r:
            showlist(lst,1,len(lst),BLUE)
        anewline()
        pivot   = lst[0]
        small= [x for x in lst[1:] if x < pivot]
        great= [x for x in lst[1:] if x >= pivot]
        m = len(small)
        showlist(full,0,l,BLANK)
        showlist(small,0,len(small),YELLOW)
        showletter(pivot,IGREEN)
        showlist(great,0,len(great),YELLOW)
        anewline()
        lesser  = simple_quicksort_aux([x for x in lst[1:] if x < pivot],l,l+len(small),full)
        greater = simple_quicksort_aux([x for x in lst[1:] if x >= pivot],l+len(small)+1,r,full)
        showlist(full,0,l,BLANK)
        if len(lesser) > 0:
            showlist(lesser,0,len(lesser),GREEN)
        showletter(pivot,IGREEN)
        if len(greater) > 0:
            showlist(greater,0,len(greater),GREEN)
        anewline()
        return lesser + [pivot] + greater 
        