import numpy as np
import pandas as pd

shots = pd.read_csv('shots_data.csv')

#getting total shots of each team
teamA = shots['team'][shots['team'] == 'Team A'].count()
teamB = shots['team'][shots['team'] == 'Team B'].count()

#filtering into different zones: rc/lc = right/left corner, nc3 = non-corner 3,shots(with others removed) = 2pt
bigy = shots[shots['y'] <= 7.8]
rc = bigy[bigy['x']>22.0]
lc = bigy[bigy['x']<-22.0]
shots.drop(rc.index, inplace = True)
shots.drop(lc.index, inplace = True)
nc3 = shots[shots['x'].pow(2) + shots['y'].pow(2) > 564.0625] #564.0625 is 23.75^2
shots.drop(nc3.index, inplace = True)

# for the tiny area where y > 7.8 and x > 22 or x< -22 and sqrt(x^2 + y^2) < 23.75ft
# technically a 3-point shot but not defined to any zone
# commented out for efficiency since there are none in this dataset
# other = shots[shots['y'] > 7.8]
# o2 = other[other['x'] < -22.0]
# o3 = other[other[x] > 22.0]


#counting the amount of shots in each zone for each team
ac3 = (rc['team'][rc['team'] == 'Team A'].count() + lc['team'][lc['team'] == 'Team A'].count())
bc3 = (rc['team'][rc['team'] == 'Team B'].count() + lc['team'][lc['team'] == 'Team B'].count())
anc3 = nc3['team'][nc3['team'] == 'Team A'].count()
bnc3 = nc3['team'][nc3['team'] == 'Team B'].count()
a2 = shots['team'][shots['team'] == 'Team A'].count()
b2 = shots['team'][shots['team'] == 'Team B'].count()

#counting number shots made in each zone for each team 
ac3m = (rc['fgmade'][rc['team'] == 'Team A'][rc['fgmade'] == 1].count() + lc['fgmade'][lc['team'] == 'Team A'][lc['fgmade'] == 1].count())
bc3m = (rc['fgmade'][rc['team'] == 'Team B'][rc['fgmade'] == 1].count() + lc['fgmade'][lc['team'] == 'Team B'][lc['fgmade'] == 1].count())
anc3m = nc3['fgmade'][nc3['team'] == 'Team A'][nc3['fgmade'] == 1].count()
bnc3m = nc3['fgmade'][nc3['team'] == 'Team B'][nc3['fgmade'] == 1].count()
a2m = shots['fgmade'][shots['team'] == 'Team A'][shots['fgmade'] == 1].count()
b2m = shots['fgmade'][shots['team'] == 'Team B'][shots['fgmade'] == 1].count()

#calculating eFG% for each zone and team
acefg = (1.5 * ac3m) / ac3
bcefg = (1.5 * bc3m) / bc3
ancefg = (1.5 * anc3m) / anc3
bncefg = (1.5 * bnc3m) / bnc3
a2efg = a2m / a2
b2efg = b2m / b2

#calculating shot distribution for each zone and team
acsd = ac3 * 100 / teamA
bcsd = bc3 * 100 / teamB
ancsd = anc3 * 100 / teamA
bncsd = bnc3 * 100 / teamB
a2sd = a2 * 100 / teamA
b2sd = b2 * 100 / teamB
print("For team A, the shot distribution is " + str(round(acsd,3)) + "% from"\
     "corner 3's, " + str(round(ancsd,3)) + "% from non-corner 3's,"\
        " and " + str(round(a2sd,3)) + "% for 2 point shots")
print("The eFG% from each zone for team A is " + str(round(acefg,3)) + " from "\
    "corner 3's, " + str(round(ancefg,3)) + " from non-corner 3's, "\
        "and " + str(round(a2efg,3)) + " for 2 point shots")
print("For team B, the shot distribution is " + str(round(bcsd,3)) + "% from "\
    "corner 3's, " + str(round(bncsd,3)) + "% from non-corner 3's, "\
        "and " + str(round(b2sd,3)) + "% for 2 point shots")
print("The eFG% from each zone for team B is " + str(round(bcefg,3)) + " from "\
    "corner 3's, " + str(round(bncefg,3)) + " from non-corner 3's, "\
        "and " + str(round(b2efg,3)) + " for 2 point shots")