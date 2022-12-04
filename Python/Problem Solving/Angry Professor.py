def designerPdfViewer(k,a):
		l=[i for i in a if i<=0]
		return "NO" if len(l)>=k else "YES"
print(designerPdfViewer(3 ,[-1, -3, 4, 2]))
#----------------------------------------------------------------------------------------------------
def designerPdfViewer(k,a):
		return "NO" if len([i for i in a if i<=0])>=k else "YES"

print(designerPdfViewer(3 ,[-1, -3, 4, 2]))
		