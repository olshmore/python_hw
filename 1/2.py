s=int(input('Whats the time?'))

hours = s//3600
minutes= (s%3600)//60
seconds=(s%3600)%60
print(hours,'h' , minutes, 'm', seconds, 's')