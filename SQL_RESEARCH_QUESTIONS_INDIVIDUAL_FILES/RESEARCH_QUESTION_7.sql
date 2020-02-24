/*Question 7: What are the longest round-trips and nonstop flights that have been booked?*/

SELECT 
    FLIGHT_CONFIRMATION_ID, 
    DEPT_FIRST_FLIGHT_NO,
    DEPT_TRIP_DURATION_HR,
    RTRN_FIRST_FLIGHT_NO,
    RTRN_TRIP_DURATION_HR,
    FORMAT(SUM(DEPT_TRIP_DURATION_HR) + SUM(RTRN_TRIP_DURATION_HR),'0.0#') AS TOTAL_TRIP_DURATION

FROM 
    EXPEDIA_TRIP_DETAILS
WHERE 
    RTRN_FLIGHT_TYPE != 'NA' AND RTRN_FLIGHT_TYPE != 'LAYOVER'
GROUP BY 
    FLIGHT_CONFIRMATION_ID, 
    DEPT_FIRST_FLIGHT_NO, 
    RTRN_FIRST_FLIGHT_NO, 
    DEPT_TRIP_DURATION_HR, 
    RTRN_TRIP_DURATION_HR
HAVING
    COUNT(DEPT_FIRST_FLIGHT_NO) = 1 AND COUNT(DEPT_SECOND_FLIGHT_NO) = 0 AND COUNT(DEPT_THIRD_FLIGHT_NO) = 0
ORDER BY RTRN_TRIP_DURATION_HR DESC
;





