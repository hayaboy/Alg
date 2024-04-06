#  입력
length=int(input())

#리스트로 변환
arr=list(map(int, input().split()))
#print(arr)
#help(arr)
arr.sort(reverse=True)
print(arr)



