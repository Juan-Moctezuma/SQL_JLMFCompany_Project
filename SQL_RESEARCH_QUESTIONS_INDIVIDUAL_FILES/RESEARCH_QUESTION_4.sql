/*Question 4: What is the average overall rating for every Airbnb listing 
in each city within the United States?*/

SELECT 
    FORMAT(ROUND(AVG(ABD.RATING_OVERALL),2),'0.0#') AS AVG_RATING_X_CITY,
    HI.CITY
FROM 
    AIRBNB_BOOKING_DATA ABD
    JOIN 
        HOST_INFO HI
        ON HI.HOST_LOCATION_ID = ABD.HOST_LOCATION_ID
WHERE
    HI.COUNTRY LIKE '%UNITED STATES%'
GROUP BY 
    HI.CITY
ORDER BY 
    AVG_RATING_X_CITY DESC
;



