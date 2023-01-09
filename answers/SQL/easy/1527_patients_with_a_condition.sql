SELECT patient_id, patient_name, conditions
FROM Patients
WHERE REGEXP_LIKE(conditions, '(^|[:blank:])DIAB1')