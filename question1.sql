-- 2 Who missed the votes?
SELECT lastname, firstname, COUNT(vote) AS absences FROM (senator, voted)
WHERE senator.id = voted.sen_id
	AND
voted.vote = 'A'
GROUP BY senator.id;