#P2M4MatthewLane
import os

os.system ("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o ""mean_temp.txt")



mean_temp_text = open("mean_temp.txt","a+")
mean_temp_text.write("Rio de Janeiro,Brazil,30.0,18.0\n")

mean_temp_text.seek(0)
headings = mean_temp_text.readline()
headings = headings.split(",")

city_temp = mean_temp_text.readline()

while city_temp:
    city_temp = city_temp.split(",")
    print(headings[2].capitalize(),"for",city_temp[0].title(),"is",city_temp[2],"celsius.")
    city_temp = mean_temp_text.readline()

