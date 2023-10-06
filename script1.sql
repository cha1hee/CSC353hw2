-- 2 Who missed the votes?
SELECT lastname, firstname, COUNT(vote) AS absences FROM (senator, voted)
WHERE senator.id = voted.sen_id
	AND
voted.vote = 'A'
GROUP BY senator.id;

-- we might have done this wrong - might want to include kamala and kelly as having missed all the votes they weren't technically present for
-- b/c they left the senate (?)

-- Question Answer

-- Kelly Loeffler and Kamala Harris were absent the most – they only participated in 2 votes.
-- This is because they were not re-elected during the 2020 election, so their term ended in January 2021.