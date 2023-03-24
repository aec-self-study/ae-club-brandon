WITH
  pageview_with_stiched_user_id AS (
  SELECT
    id,
    COALESCE (FIRST_VALUE(customer_id IGNORE NULLS) OVER (PARTITION BY visitor_id ORDER BY visitor_id ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING),visitor_id) AS user_id,
    device_type,
    timestamp,
    page
  FROM
    `analytics-engineers-club.web_tracking.pageviews` ),
  pageview_sessionised AS(
  SELECT
    id,
    user_id,
    device_type,
    timestamp,
    page,
    1 + SUM(
    IF
      (TIMESTAMP_DIFF(timestamp, lag, SECOND) > 1800, 1, 0)) OVER (PARTITION BY user_id ORDER BY timestamp ) AS session_id
  FROM (
    SELECT
      *,
      LAG(timestamp) OVER (PARTITION BY user_id ORDER BY timestamp ) AS lag
    FROM
      pageview_with_stiched_user_id ))
SELECT
  *,
  MIN(timestamp) OVER (PARTITION BY user_id, session_id) AS session_start_time,
  MAX(timestamp) OVER (PARTITION BY user_id, session_id) AS session_end_time,
FROM
  pageview_sessionised
  ORDER BY user_id, session_id