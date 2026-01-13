import functionx.timex
import functionx.namex

def lost(user, attempt, score,output):
    
    print()
    print("***Game status***")
    output+="\n\n***Game status***"
    print('Player name:', user)
    output+='\nPlayer name:'+ user
    print("Total attempts:", attempt)
    output+="\nTotal attempts:"+str(attempt)
    print("Final score:", score)
    output+="\nFinal score:"+str(score)
    print(user, "was defeated!!!")
    output+= '\n'+user+ " was defeated!!!"
    return functionx.timex.time(output) # Exit the function