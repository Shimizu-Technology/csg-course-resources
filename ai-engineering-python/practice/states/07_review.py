def review_supply(proposed, chosen):
    if not isinstance(chosen,str) or chosen not in {'paper','marker'}:
        raise ValueError('Reviewer must choose an allowed item')
    return {'status':'human_reviewed','item':chosen,'changed':proposed.get('item') != chosen}

print(review_supply({'item':'marker'},'paper'))
print('A human choice records a decision. No order has been placed.')
