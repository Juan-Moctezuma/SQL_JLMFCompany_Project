/*Question 1: Who are the users that opened an account but have not booked 
any flights or reserved any Airbnb listing through the company's platform - “EApp”?*/

SELECT 
    UA.USER_ID, 
    UA.FIRST_LAST_NAME, 
    UR.TRANSACTION_DATE, 
    UR.TRANSACTION_ID 
FROM 
    USER_ACCOUNT UA
    FULL OUTER JOIN USER_RECORDS UR
        ON UA.USER_ID = UR.USER_ID
    FULL OUTER JOIN CARD_DETAILS CD
        ON UA.USER_ID = CD.USER_ID
WHERE UR.TRANSACTION_DATE IS NULL AND UR.TRANSACTION_DATE IS NULL
;


