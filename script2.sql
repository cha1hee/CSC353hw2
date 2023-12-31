-- 3 Who missed the votes strikes back
SELECT lastname, firstname, COALESCE (absences, 0) AS attendance
FROM (SELECT lastname, firstname, COUNT(vote) AS absences
	FROM (senator, voted)
	WHERE senator.id = voted.sen_id
		AND
	voted.vote = 'A'
	GROUP BY senator.id) AS joining
NATURAL RIGHT JOIN senator;