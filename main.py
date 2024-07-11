import angr
from main_compare import Compare

def main():
    # proj1 is refrence, proj2 is comparing target 
    proj1 = angr.Project("./angr_ctf/dist/16_angr_arbitrary_write", auto_load_libs = False)
    proj2 = angr.Project("./angr_ctf/dist/17_angr_arbitrary_jump", auto_load_libs = False)

    compareScore = Compare(proj1,proj2)
    selfScore1 = Compare(proj1,proj1)
    selfScore2 = Compare(proj2,proj2)

    similarity = 2*compareScore/(selfScore1+selfScore2)

    print('Score of comparing project1 and project2: ', compareScore)
    print('Score of comparing project1 and itself: ', selfScore1)
    print('Score of comparing project2 and itself: ', selfScore2)
    print('Final similarity score: ', similarity)

if __name__ == '__main__':
    main()





