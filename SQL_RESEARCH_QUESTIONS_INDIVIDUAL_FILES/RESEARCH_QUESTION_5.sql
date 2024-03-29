/*Question 5: What is the percentage of guests per category (adults, minors and children) in each Airbnb 
reservation (AIR_CONFIRMATION_ID)? What are the host names and arrival dates linked to every reservation?*/

SELECT 
    HI.HOST_NAME, 
    ARD.AIR_CONFIRMATION_ID,
    ARD.START_DATE,
    ARD.END_DATE, 
    FORMAT(ROUND(SUM(ARD.GUEST_ADULT_NO) * 100.0 / SUM(ABD.TOTAL_GUESTS),3),'0.0#') AS GUEST_ADULT_PERCENT,
    FORMAT(ROUND(SUM(ARD.GUEST_CHILDREN_NO) * 100.0 / SUM(ABD.TOTAL_GUESTS),3),'0.0#') AS GUEST_CHILDREN_PERCENT,
    FORMAT(ROUND(SUM(ARD.GUEST_INFANT_NO) *100.0 / SUM(ABD.TOTAL_GUESTS),3),'0.0#') AS GUEST_INFANT_PERCENT
FROM 
    AIRBNB_RESERVATION_DETAILS ARD
    JOIN 
        AIRBNB_BOOKING_DATA ABD
        ON ABD.AIR_CONFIRMATION_ID = ARD.AIR_CONFIRMATION_ID 
    JOIN 
        HOST_INFO HI
        ON HI.HOST_ID = ABD.HOST_ID 
WHERE 
    ARD.START_DATE > '12/31/2018' AND ARD.START_DATE < '1/1/2020'
GROUP BY 
    ARD.AIR_CONFIRMATION_ID, HI.HOST_NAME, ARD.START_DATE, ARD.END_DATE
ORDER BY 
    HI.HOST_NAME ASC
;






