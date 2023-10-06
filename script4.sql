SELECT COUNT(sen_x.vote) AS number_of_disagreement FROM
	(SELECT * FROM voted WHERE sen_id = 'S412') AS sen_x,
	(SELECT * FROM voted WHERE sen_id = 'S221') AS sen_y
WHERE sen_x.number = sen_y.number
AND NOT sen_x.vote = sen_y.vote
AND NOT sen_x.vote = 'A'
AND NOT sen_y.vote = 'A';