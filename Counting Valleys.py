def countingValleys(n, s):
    store = 0 #stores the values of currect location. a possative number is down and negative is up. 0 being sea level
    timer = 0 # stores number of runs in for loop
    valleys = 0 #stores the value to return. eg each time a valley is finished

    for paths in s: #loops all 'U' and 'D'
        timer += 1 
        if timer == n + 1:
            break #ends loop onces all U and D have been checked. it adds one to check if sea level at end

        print(store) #this is for testing. no real use

        if paths == "D": # if D add 1 to store
            store += 1
        elif paths == "U": #and if not D it -1. it shouldn't +/- anything on last run
            store -= 1

        if store == 0 and paths == "U": # checks store and if 0, sea level, then adds a valley. has to check with paths to make sure they didn't just add 1 to -1 which would mean they just came off a hill not a valley
            valleys += 1

    return valleys
