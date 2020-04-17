import subprocess
process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print ('.')
print('.')
print ('ths is just for learning purposes')  #only for use case
print("Line A \n Line B")
<<<<<<< HEAD
open("log.txt", "abc")
=======
open("log.txt", "abcde")
>>>>>>> b2b850e0d3ab2eaab83fc54867e97a8906d336d8
