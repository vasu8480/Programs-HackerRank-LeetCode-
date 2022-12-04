def designerPdfViewer(h, word):
		tallest = 0
		for letter in word:   #ord() returns the unicode of a character
				if h[ord(letter) - 97] > tallest: # ord(letter) - 97 is the index of the letter in the list
						tallest = h[ord(letter) - 97] # if the height of the letter is greater than the current tallest, set it as the tallest
		return tallest * len(word) # return the area of the word
print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5], 'zbc'))
#---------------------------------------------------------------------------------------------------
def designerPdfViewer(k,a):
		return max(k[ord(i)-97] for i in a)*len(a)
print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5], 'zbc'))