# -*- coding: utf-8 -*-
A, B = map(int, input().split())  # map �Լ��� �־��� �Լ��� �ݺ� ������ ��ü�� ���ڷ� �޾� �ش� �Լ��� ��� ��ҿ� ����� ����� ��ȯ�ϴ� �Լ���
C = int(input())

total = B + C

share = total // 60  # ���� ������ # /�� �Ǽ������� ����
remainder = total % 60

A=A+share
B=remainder
A= A%24
print(A, B)