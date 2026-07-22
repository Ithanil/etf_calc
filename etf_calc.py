"""Calculate an ACWI/Europe/EM ETF allocation."""

# MSCI index data as of June 30, 2026, and World Bank GDP data for 2025.
DEVELOPED_ACWI = 0.878222
US_ACWI = 0.636300
EUROPE_ACWI = 0.138704
GDP_RATIO_US_EUROPE = 1.303429


def calculate_etf_ratios(
    target_developed,
    developed_acwi=DEVELOPED_ACWI,
    us_acwi=US_ACWI,
    europe_acwi=EUROPE_ACWI,
    gdp_ratio_us_europe=GDP_RATIO_US_EUROPE,
):
    """Return the ACWI, Europe, and EM weights for a developed-market target."""
    r_acwi = (
        gdp_ratio_us_europe
        * target_developed
        / (
            us_acwi
            + gdp_ratio_us_europe * (developed_acwi - europe_acwi)
        )
    )
    r_europe = target_developed - r_acwi * developed_acwi
    return r_acwi, r_europe, (1.0 - r_acwi - r_europe)


def main():
    target_ratio = float(
        input("Enter desired developed market share (in %): ")
    ) / 100.0
    weights = calculate_etf_ratios(target_ratio)

    if any(weight < 0 for weight in weights):
        print(
            "Error: One or more negative weights. "
            "Make sure your desired DM share is achievable."
        )
        return 1

    acwi, europe, emerging_markets = weights
    print(f"ACWI ETF: {acwi * 100:.3f}%")
    print(f"Europe ETF: {europe * 100:.3f}%")
    print(f"EM ETF: {emerging_markets * 100:.3f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
