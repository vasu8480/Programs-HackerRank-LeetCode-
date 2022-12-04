def designerPdfViewer(k,a):
		return max(k[ord(i)-97] for i in a)*len(a)


print(designerPdfViewer(3 ,[-1, -3, 4, 2]))
		