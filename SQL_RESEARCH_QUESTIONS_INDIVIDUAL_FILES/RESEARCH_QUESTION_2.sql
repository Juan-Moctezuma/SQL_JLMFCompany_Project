/*Question 2: What is the booking id, credit/debit card number, and transaction 
identifier linked to order number 95?*/

SELECT 
   CD.CARD_NO,
   UR.ORDER_NO,
   B.BOOKING_ID,
   UR.TRANSACTION_ID
FROM 
    BOOKINGS B 
    JOIN USER_RECORDS UR
        ON UR.BOOKING_ID = B.BOOKING_ID
    JOIN CARD_DETAILS CD 
        ON CD.USER_ID = UR.USER_ID
WHERE UR.ORDER_NO < 96 AND UR.ORDER_NO > 94
;





