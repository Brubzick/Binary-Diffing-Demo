import angr
from main_compare import Compare, Compare2

def main():
    # proj1 is refrence, proj2 is comparing target 
    proj1 = angr.Project("./hello", auto_load_libs = False)
    proj2 = angr.Project("./shell_sort", auto_load_libs = False)

    compareScore = Compare2(proj1,proj2)
    print('compare score done')
    selfScore1 = Compare2(proj1,proj1)
    print('self1 score done')
    selfScore2 = Compare2(proj2,proj2)
    print('self2 score done')

    similarity = 2*compareScore/(selfScore1+selfScore2)

    print('Score of comparing project1 and project2: ', compareScore)
    print('Score of comparing project1 and itself: ', selfScore1)
    print('Score of comparing project2 and itself: ', selfScore2)
    print('Final similarity score: ', similarity)

if __name__ == '__main__':
    main()





