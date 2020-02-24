/*Question 3: Who are the users (account holders) and their respective phone numbers 
linked to every, and linked to every purchase or transaction that occurred after April 20, 2016?*/

SELECT 
    UA.FIRST_LAST_NAME,
    UA.USER_ID,
    UA.USER_PHONE 
FROM 
    USER_ACCOUNT UA
    INNER JOIN EXPEDIA_PASSENGER_DATA EPD 
        ON EPD.PASSENGER_NAME = UA.FIRST_LAST_NAME
    INNER JOIN USER_RECORDS UR 
        ON UR.USER_ID = UA.USER_ID 
WHERE UR.TRANSACTION_DATE > '4/20/2016'
;



