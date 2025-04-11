def calculate_etf_ratios(target_developed, developed_acwi, us_acwi, eu_acwi, gdpr_us_eu):
    r_acwi = gdpr_us_eu * target_developed / (us_acwi + gdpr_us_eu*(developed_acwi - eu_acwi))
    r_eu = target_developed - r_acwi * developed_acwi
    return r_acwi, r_eu, (1. - r_acwi - r_eu)

target_ratio = float(input("Enter desired developed market share (in %): ")) / 100.
x, y, z = calculate_etf_ratios(target_ratio, 0.9, 0.65, 0.11, 1.5)
if x < 0 or y < 0 or z < 0:
    print("Error: One or more negative weights. Make sure your desired DM share is achievable.")
    exit(1)
print(f"ACWI ETF: {x*100:.3f}%")
print(f"EU ETF: {y*100:.3f}%")
print(f"EM ETF: {z*100:.3f}%")
