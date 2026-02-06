def get_industry_benchmark(industry: str):
    
    benchmarks = {
        "retail": {
            "profit_margin": 12,
            "expense_ratio": 65,
            "growth_rate": 10
        },
        "manufacturing": {
            "profit_margin": 18,
            "expense_ratio": 55,
            "growth_rate": 8
        },
        "saas": {
            "profit_margin": 25,
            "expense_ratio": 70,
            "growth_rate": 20
        },
        "agriculture": {
            "profit_margin": 10,
            "expense_ratio": 60,
            "growth_rate": 6
        }
    }

    return benchmarks.get(industry.lower(), benchmarks["retail"])
