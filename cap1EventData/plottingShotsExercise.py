import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen, VerticalPitch

parser = Sbopen()
df, related, freeze, tactics = parser.event(69301)
team1, team2 = df.team_name.unique()

pitch = Pitch(line_color = "black")
fig, ax = pitch.draw(figsize=(10, 7))
pitchLengthX = 120
pitchWidthY = 80

#Plotting the passes (plottingShots exercise)
passes = df.loc[df['type_name'] == 'Pass'].loc[df['sub_type_name'] != 'Throw-in'].set_index('id')

for i,passe in passes.iterrows():
    if(passe['team_name']==team2):
        x=passe['x']
        y=passe['y']
        passLenght = passe['pass_length']
        team_name=passe['team_name']
        playerName = passe['player_name']
        circleSize = 2
        if(playerName != 'Sara Caroline Seger'):
            passCircle = plt.Circle((x, y), circleSize, color="blue")
            passCircle.set_alpha(0.5)
        else:
            passCircle = plt.Circle((x, y), circleSize, color="gold")
            passArrow = plt.Arrow(x,y, passe['end_x'] - x, passe['end_y'] -y, width = 1.5 )
            ax.add_patch(passArrow)

        ax.add_patch(passCircle)

#set title
fig.suptitle("Sweden passes (blue) with Sara Caroline Seger's (gold) passes direction", fontsize = 24)
fig.set_size_inches(10, 7)
plt.show()
