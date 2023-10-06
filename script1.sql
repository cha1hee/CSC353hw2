-- 2 Who missed the votes?
SELECT lastname, firstname, COUNT(vote) AS absences FROM (senator, voted)
WHERE senator.id = voted.sen_id
	AND
voted.vote = 'A'
GROUP BY senator.id;

-- we might have done this wrong - might want to include kamala and kelly as having missed all the votes they weren't technically present for
-- b/c they left the senate (?)

-- Question Answer

-- Mike Rounds was most absent due to illness of his wife.
-- Dan Sullivan was next for the most absences due to a family death.