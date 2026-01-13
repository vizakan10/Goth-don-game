import functionx.timex
import functionx.namex

def win(user, attempt, score,output):
    print()
    print("***Game status***")
    output+="***\n\nGame status***"
    print('Player name:', user)
    output+='\nPlayer name:'+str(user)
    print("Total attempts:", attempt)
    output+="\nTotal attempts:"+ str(attempt)
    print("Final score:", score)
    output+="\nFinal score:"+str(score)
    print(user, "saved letter-kind")
    output+='\n'+user+"saved letter-kind"
    return functionx.timex.time(output)