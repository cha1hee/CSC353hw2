SELECT sen_y_lastname, sen_y_firstname, party, number_of_disagreements, number_of_agreements, ((number_of_agreements - number_of_disagreements) / (number_of_agreements + number_of_disagreements)) AS agreement_index
	FROM
		(SELECT senator.lastname AS sen_y_lastname, senator.firstname AS sen_y_firstname, senator.party, COALESCE(number_of_disagreements, 0) AS number_of_disagreements
			FROM
				(SELECT sen_x.sen_id AS sen_x_id, sen_y.sen_id AS sen_y_id, COUNT(sen_x.vote) AS number_of_disagreements
					FROM
						(SELECT * FROM voted WHERE sen_id = 'S355') AS sen_x, (SELECT * FROM voted) AS sen_y
							WHERE sen_x.number = sen_y.number
								AND NOT sen_x.vote = sen_y.vote
								AND NOT sen_x.vote = 'A'
								AND NOT sen_y.vote = 'A'
 							GROUP BY sen_y.sen_id
 				) AS total_disagreements
 				RIGHT JOIN senator
					ON sen_y_id = senator.id
		) AS disagreement_table
	NATURAL JOIN
		(SELECT senator.lastname AS sen_y_lastname, senator.firstname AS sen_y_firstname, COALESCE(number_of_agreements, 0) AS number_of_agreements
			FROM
				(SELECT sen_x.sen_id AS sen_x_id, sen_y.sen_id AS sen_y_id, COUNT(sen_x.vote) AS number_of_agreements
					FROM
						(SELECT * FROM voted WHERE sen_id = 'S355') AS sen_x, (SELECT * FROM voted) AS sen_y
							WHERE sen_x.number = sen_y.number
								AND sen_x.vote = sen_y.vote
								AND NOT sen_x.vote = 'A'
 							GROUP BY sen_y.sen_id
 				) AS total_agreements
 				RIGHT JOIN senator
					ON sen_y_id = senator.id
		) AS agreement_table
ORDER BY agreement_index;

-- Question Answer

-- There is a clear bipartisan division. When comparing agreement index against Ted Cruz, a Republican senator, 
-- all Republicans had a positive agreement index value
-- (except Kelly Loeffler, who voted in disagreement twice out of the 2 votes she participated in.) 
-- Conversely, all Democratcs had a negative agreement index value. 

-- This division is visually indicated in our web page, as Democrats have a light blue row color
-- and Republicans have a light red row color.
