def designerPdfViewer(k,a):
		return "NO" if len([i for i in a if i<=0])>=k else "YES"
		
print(designerPdfViewer(3 ,[-1, -3, 4, 2]))
		