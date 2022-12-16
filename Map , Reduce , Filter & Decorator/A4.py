def modified_result(pass_result):
    def distinction(marks):
        for y in marks:
            if y>=75:
                print("Amazing")
            else:
                return pass_result(marks)
    return distinction


@ modified_result
def result(marks):
    for x in marks:
        if x>=33:
            pass
        else :
            print("You are Fail")
            break
    else:
        print("You are Pass")

result({44,56,79,51,18})
