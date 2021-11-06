text = 'Text file to save\nNew File!'

saveFile = open('example.txt', 'w')
saveFile.write(text)
saveFile.close()
