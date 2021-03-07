print("몇 번째 소수까지 더해야 100보다 큰 수가 될까요?")

sum=2 # 소수들의 합
a=3
num=1 # 몇 번째 소수인지 카운팅

while sum<=100:
    for i in range(2,a):
      if (a%i==0):
          a+=1 # if문을 통해, 소수가 아닌 수에 +1 하기!

    sum+=a # 소수를 sum에 더하기
    a+=1
    num+=1

print("정답은 ",num,"번째입니다!", sep="") # 결과 출력하기
