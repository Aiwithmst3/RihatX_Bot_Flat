
def generate_report(signal, strategy, timeframe="1 minute", win_rate="90%"):
    return f"""
    📡 Signal: {signal}
    🧠 Strategy: {strategy}
    ⏱️ Timeframe: {timeframe}
    🏆 Estimated Win Rate: {win_rate}
    """
