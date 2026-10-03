def summarize(rows):
    if not rows:
        raise ValueError('Need attempts')
    return {'attempts':len(rows), 'fallbacks':sum(row['status'] != 'proposed' for row in rows), 'known_estimated_usd':round(sum(row.get('estimated_usd',0) for row in rows),8), 'unknown_cost_attempts':sum('estimated_usd' not in row for row in rows), 'mean_latency_ms':sum(row['latency_ms'] for row in rows)/len(rows)}

rows = [{'status':'proposed','estimated_usd':0.000045,'latency_ms':80}, {'status':'review_needed','latency_ms':120}]
print(summarize(rows))
print('Missing provider usage is unknown, not evidence of a free failed call.')
