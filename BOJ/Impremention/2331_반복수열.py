# -*- coding: utf-8 -*-

A,P=map(int,input().split())

un_map={} # unordered_map�� ���� ������ �ϴ� Python dict

un_map[A] = 0

while un_map[A]<2:
    un_map[A]+=1
    num=0
    while (A/10) !=0:
        num+=(A%10)**P #������ **������ ���
        A //=10 #���� ������
    if A != 0:
        num += A ** P
        
    A=num
    if A in un_map:
        continue
    else:
        un_map[A]=0

ans=0
for key, value in un_map.items():
    if value == 1:
        ans+=1

print(ans)

