import numpy as np
import re

# 데이터를 읽어오기
negative = '/Users/jungwon-c/Documents/ML구현/processed_acl/books/negative.review'
positive = '/Users/jungwon-c/Documents/ML구현/processed_acl/books/positive.review'

with open(negative) as ne, open(positive) as po:
	for ix, line in enumerate(ne):
		print(line)
		if ix > 10:
			break

# 읽어온 데이터 프린트
# 일단 작은 차원수로 데이터를 작게 만듦
# 로지스틱 회귀 이진분류기 모델
# 대규모화
