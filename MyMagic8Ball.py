import random

ans1="괜찮아요. 그대로 해보세요."
ans2="됐네요, 이 사람아!"
ans3="다시 생각해보는 게 좋아요."
ans4="당신이 맞아요. 그대로 하는 게 제일 좋아요."
ans5="당신. 제 정신이 아니군요!"
ans6="잠시 쉬어가다 보면 답이 보일 거예요."
ans7="당신이라면 잘 할 수 있어요."
ans8="해도 그만 안 해도 그만 아니겠어요?"

print("MyMagic8Ball에 오신 것을 환영합니다.")

question=input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")
print("고민 중...\n"*3)

choice=random.randint(1,8)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
else:
    answer=ans8

print(answer)
input("\n\n마치려면 엔터 키를 누르세요.")
