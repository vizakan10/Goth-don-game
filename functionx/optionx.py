import random
import functionx.lostx
import functionx.winx


output=''
def game(user):
    global output
    name=''
    attempt=0
    score=0
    num=0
    score = random.randrange(1, 50)
    for i in range(1, 21):
        elements = []
        attempt = i
        
        if 1 <= attempt <= 5:
            for i in range(0, 5):
                choice = random.randrange(15, 101)
                elements.append(choice)
        elif 6 <= attempt <= 10:
            for i in range(0, 5):
                choice = random.randrange(250, 2001)
                elements.append(choice)
        elif 11 <= attempt <= 15:
            for i in range(0, 5):
                choice = random.randrange(3000, 10001)
                elements.append(choice)
        else:
            for i in range(0, 5):
                choice = random.randrange(20000, 100001)
                elements.append(choice)
        print("Player's name-",user)
        output+="\nPlayer'sname-"+str(user)+'\n'
        print("Attempt:", attempt)
        output+="Attempt:"+ str(attempt)+'\n'
        print(user + "'s", "life score is:", score)
        output+=str(user) + "'s  life score is:"+str(score)+'\n'

        for val in elements:
            val = str(val) + "  "
            print(val, end="")
            output+=val+" "

        try:
            num = int(input("\nSelect a number to fight:"))
            output+="\nSelect a number to fight:"+str(num)
           
        except ValueError:
            print("No such enemy")
            output+="\nNo such enemy"
            
            result_timestamp = functionx.lostx.lost(user, attempt, score,output)
            return result_timestamp# Exit the function on invalid input

        if num not in elements:
            print("No such enemy")
            output+="\nNo such enemy"
            
            result=functionx.lostx.lost(user, attempt, score,output)
            return result # Exit the function on invalid input
        else:
            if num <= score:
                print(user, "killed", num)
                output+='\n'+str(user)+"  killed "+str(num)
                score += int(num)
                if attempt == 20:
                    result_timestamp = functionx.winx.win(user, attempt, score,output)
                    return result_timestamp
                print()
                output+='\n'
            else:
                print(num, "killed", user)
                output+='\n'+str(num)+" killed "+str(user)
                
                result_timestamp = functionx.lostx.lost(user, attempt, score,output)
                return result_timestamp  # Exit the function if defeated




    


