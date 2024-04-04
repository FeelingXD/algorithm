--  조건에 맞는 도서 리스트 출력하기

SELECT  BOOK_ID,DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY='인문' AND PUBLISHED_DATE like '2021%'
ORDER BY PUBLISHED_DATE