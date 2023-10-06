SELECT senator.lastname AS sen_y_lastname, senator.firstname AS sen_y_firstname, COALESCE (number_of_disagreement, 0) as number_of_disagreement FROM
(SELECT sen_x.sen_id AS sen_x_id, sen_y.sen_id AS sen_y_id, COUNT(sen_x.vote) AS number_of_disagreement FROM
	(SELECT * FROM voted WHERE sen_id = 'S412') AS sen_x,
	(SELECT * FROM voted) AS sen_y
	WHERE sen_x.number = sen_y.number
	AND NOT sen_x.vote = sen_y.vote
	AND NOT sen_x.vote = 'A'
	AND NOT sen_y.vote = 'A'
 GROUP BY sen_y.sen_id) AS total_calculated
 RIGHT JOIN
 senator
 ON sen_y_id = senator.id;