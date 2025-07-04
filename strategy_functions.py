
# RihatX Bot - Strategy Functions (Summary for example)

def match_candle_wick_trap(candles):
    if len(candles) < 2:
        return False
    last = candles[-1]
    return last['wick'] > last['height'] and last['height'] < 25

def match_order_block_liquidity_grab(candles):
    if len(candles) < 3:
        return False
    c1, c2, c3 = candles[-3:]
    return c1['color'] == c3['color'] and c2['wick'] > c2['height'] * 1.2 and c3['height'] > 30

def match_bos_retest(candles):
    if len(candles) < 3:
        return False
    c1, c2, c3 = candles[-3:]
    return c1['height'] < c2['height'] and c2['height'] > c3['height'] and c2['color'] != c3['color']

# ... (remaining strategies should be added here by user or as per full list)

strategies = [
    ("#1 Candle + Wick Trap", match_candle_wick_trap),
    ("#2 OB Liquidity Grab", match_order_block_liquidity_grab),
    ("#3 BoS + Retest", match_bos_retest),
    # ... Add remaining 47 strategies here
]

def detect_strategy(candles):
    for name, func in strategies:
        if func(candles):
            return name
    return None

def get_signal_from_strategy(name):
    if any(x in name for x in ["Green", "Sniper", "CALL"]):
        return "CALL"
    elif any(x in name for x in ["Red", "PUT", "Reversal"]):
        return "PUT"
    return "CALL"
