import subprocess
process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print ('.')
print('.')
print ('ths is just for learning purposes')  #only for use case
print("Line A \n Line B")
open("log.txt", "abc")
