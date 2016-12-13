#A Dictionary of movie critics and their ratings of a small 
#set of movies
from math import sqrt 
critics = {
    'Lisa Rose':{
    'Lady In The Water':2.5,
    'Snakes on a Plane':3.5,
    'Just My Luck':3.0,
    'Superman Returns':3.5,
    'You, Me, and Dupree':2.5,
    'The Night Listener':3.0
    },
    'Gene Seymour':{
    'Lady In The Water':3.0,
    'Snakes on a Plane':3.5,
    'Just My Luck':1.5,
    'Superman Returns':5.0,
    'The Night Listener':3.0,
    'You, Me, and Dupree':3.5
    },
    'Michael Phillips':{
    'Lady In The Water':2.5,
    'Snakes on a Plane':3.0,
    'Superman Returns':3.5,
    },
    'Mick Lasalle':{
    'Lady In The Water':3.0,
    'Snakes on a Plane':4.0,
    'Just My Luck':2.0,
    'Superman Returns':3.0,
    'The Night Listener':3.0,
    'You, Me, and Dupree':2.0
    },
    'Jack Matthews':{
    'Lady In The Water':3.0,
    'The Night Listener':3.0,
    'Superman Returns':5.0,
    'You, Me, and Dupree':3.5
    },
    'Toby':{
    'Snakes on a Plane':3.5,
    'The Night Listener':4.0,
    'You, Me, and Dupree':3.5,
    'Superman Returns':5.0 
    }
}

#Returns a distance-based similarity score for person1 and person2 
def sim_distance(prefs,person1, person2):
    #Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    #If they have no ratings in common, return 0
    if len(si)==0:
        return 0

    #Add Up the square of all the differences
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
                            for item in prefs[person1] if item in prefs[person2]])

    print(si)
    
    return 1/(1+sum_of_squares)


#Returns the Pearson Correlation Coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
    #Get the list of mutuaully rated items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    
    #Find the number of of elements that are mutually rated
    n = len(si)
    if n == 0:
        return 0

    #Add Up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    #Sum up the squares
    sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])

    #Sum up the Products 
    pSum = sum([prefs[p1][it]*prefs[p2][it]for it in si])

    #Calculate the Pearson Score
    num = pSum-(sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den == 0: return 0 

    r = num/den
    return r


print(sim_distance(critics,'Lisa Rose','Gene Seymour'))
print(sim_pearson(critics,'Lisa Rose','Gene Seymour'))