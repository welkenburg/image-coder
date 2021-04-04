class Image:

	def __init__(self,imagePath):
		with open(imagePath, "r") as inputImage:
			lines = inputImage.readlines()
			self.pixels = [int(i) for i in lines[1:]] if int(lines[1][0]) else [ord(i) for i in lines[1:]]
			self.width = int(lines[0].split(" ")[1])
			self.height = int(lines[0].split(" ")[2])
			self.color = int(lines[0].split(" ")[3])
			self.imagePath = imagePath

	def code(self,message,start=0):
		for i in range(len(message)):
			char = ord(message[i])
			for j in range(8):
				firstBit = char >> 7 - j
				self.pixels[start + i * 8  + j] = ((self.pixels[start + i * 8  + j] >> 1) << 1) + firstBit
				char -= firstBit << 7 - j

	def decode(self,start=0):
		message = ""
		char, i = 0,0
		for pixel in self.pixels:
			i += 1
			char <<= 1
			char += int(bin(pixel)[-1])

			if i >= 8:
				message += chr(char)
				char,i = 0,0

			if len(message) > 0 and message[-1] == "\0":
				return message

	def export(self,path = None):
		path = f"new {self.imagePath}" if path == None else path
		with open(path,"a") as newImage:
			newImage.write(f"P2 {self.width} {self.height} {self.color}\n")
			for pixel in self.pixels:
				newImage.write(f"{pixel}\n")

image = Image("secret.pgm")
image.code("hello my friend\0")
#print(image.decode())
image.export()